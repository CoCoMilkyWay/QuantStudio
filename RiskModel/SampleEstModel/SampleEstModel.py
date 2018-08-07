# coding=utf-8
"""基于样本估计的风险模型"""
import time

import pandas as pd
import numpy as np
from progressbar import ProgressBar

import DataSource
import RiskModelFun

# 估计协方差矩阵
def CovarianceGeneration(args,qs_env):
    ReturnDates = pd.Series(args["DS"].getDateTime())
    args["DS"].start()
    iReturn = None
    iReturnDates = []
    if args["ModelArgs"]['运行模式']=='串行':# 运行模式为串行
        ProgBar = ProgressBar(max_value=len(args["RiskESTDates"]))
        ProgBar.start()
    else:
        ProgBar = None
    for i,iDate in enumerate(args["RiskESTDates"]):
        iInd = (ReturnDates<=iDate).sum()-1
        if iInd<args["CovESTArgs"]["样本长度"]-1:# 样本不足, 跳过
            if ProgBar is not None:
                ProgBar.update(i+1)
            else:
                args['Sub2MainQueue'].put((qs_env.PID,1,None))
            continue
        args["DS"].MoveOn(iDate)
        iLastDates = iReturnDates
        iReturnDates = list(ReturnDates.iloc[iInd-args["CovESTArgs"]["样本长度"]+1:iInd+1])
        iNewDates = list(set(iReturnDates).difference(set(iLastDates)))
        iNewDates.sort()
        if iReturn is not None:
            iReturn = pd.concat([iReturn,args["DS"].getFactorData(ifactor_name=args["ModelArgs"]["收益率因子"],dates=iNewDates)]).loc[iReturnDates,:]
        else:
            iReturn = args["DS"].getFactorData(ifactor_name=args["ModelArgs"]["收益率因子"],dates=iNewDates).loc[iReturnDates,:]
        iCov = RiskModelFun.estimateFactorCov_CHE2(iReturn,forcast_num=args["CovESTArgs"]["预测期数"],
                                                   auto_corr_num=args["CovESTArgs"]["自相关滞后期"],
                                                   half_life_corr=args["CovESTArgs"]["相关系数半衰期"],
                                                   half_life_vol=args["CovESTArgs"]["波动率半衰期"])
        args["RiskDB"].saveData(args["TargetTable"],iDate,cov=iCov)
        if ProgBar is not None:
            ProgBar.update(i+1)
        else:
            args['Sub2MainQueue'].put((qs_env.PID,1,None))
    if ProgBar is not None:
        ProgBar.finish()
    args["DS"].endDS()
    if args["ModelArgs"]['运行模式']!='串行':
        qs_env.closeResource()
    return 0


class SampleEstModel(object):
    """基于样本估计的风险模型"""
    def __init__(self,name,config_file=None,qs_env=None):
        self.ModelType = "基于样本估计的风险模型"
        # 需要预先指定的属性
        self.Name = name
        self.QSEnv = qs_env
        self.Config = self.QSEnv.loadConfigFile(config_file)
        self.RiskESTDates = []# 估计风险的日期序列
        # 模型的其他属性
        self.RiskDB = None# 风险数据库
        self.TargetTable = None# 风险数据存储的目标表
        self.DS = None# 提供因子数据的数据源
        return
    # 设置计算风险估计的日期序列
    def setRiskESTDate(self,dates):
        self.RiskESTDates = dates
        self.RiskESTDates.sort()
        return 0
    # 初始化
    def initInfo(self):
        if self.RiskESTDates==[]:
            self.QSEnv.SysArgs['LastErrorMsg'] = "没有设置计算风险数据的日期序列!"
            return 0
        # 获得风险数据库
        self.RiskDB = getattr(self.QSEnv,self.Config.SaveArgs["风险数据库"])
        self.TargetTable = self.Config.SaveArgs["风险数据表"]
        # 创建数据源
        FactorDB = getattr(self.QSEnv,self.Config.ModelArgs['因子数据库'])
        self.DS = DataSource.DataSource("MainDS",FactorDB,self.QSEnv)
        self.DS.prepareData(self.Config.DSTableFactor)
        self.DS.setIDFilter(self.Config.ModelArgs["ID过滤条件"])
        self.DS.SysArgs.update(getattr(self.Config,"DSSysArgs",{}))
        if self.RiskESTDates==[]:
            self.QSEnv.SysArgs['LastErrorMsg'] = "可以计算风险数据的日期序列为空!"
            return 0
        else:
            return 0
    # 生成协方差矩阵
    def _genCovariance(self):
        Args = {"RiskDB":self.RiskDB,
                "DS":self.DS,
                "RiskESTDates":self.RiskESTDates,
                "TargetTable":self.TargetTable,
                "ModelArgs":self.Config.ModelArgs,
                "CovESTArgs":self.Config.CovESTArgs}
        if Args["ModelArgs"]['运行模式']=='串行':
            CovarianceGeneration(Args,self.QSEnv)
        else:
            nTask = len(self.RiskESTDates)
            nPrcs = min((nTask,self.Config.ModelArgs["子进程数"]))
            ProgBar = ProgressBar(max_value=nTask)
            Procs,Main2SubQueue,Sub2MainQueue = self.QSEnv.startMultiProcess(n_prc=nPrcs, target_fun=CovarianceGeneration,
                                                                             arg=Args, partition_arg="RiskESTDates",
                                                                             main2sub_queue="None", sub2main_queue="Single")
            iProg = 0
            ProgBar.start()
            while (iProg<nTask):
                iPID,iErrorCode,iMsg = Sub2MainQueue.get()
                if iErrorCode==-1:
                    for iProc in Procs:
                        if iProc.is_alive():
                            iProc.terminate()
                    print('进程 '+iPID+' :运行失败:'+str(iMsg))
                    break
                else:
                    iProg += 1
                    ProgBar.update(iProg)
            ProgBar.finish()
            for iPID,iPrcs in Procs.items():
                iPrcs.join()
        return 0
    # 生成数据
    def genData(self):
        print("风险数据计算中...")
        StartT = time.clock()
        self._genCovariance()
        print("风险数据计算完成, 耗时 : %.2f" % (time.clock()-StartT))
        self.RiskDB.connect()
        return 0