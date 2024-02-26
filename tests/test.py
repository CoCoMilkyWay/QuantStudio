# -*- coding: utf-8 -*-
import os
import datetime as dt
import unittest

import numpy as np
import pandas as pd

import QuantStudio.api as QS

TSDB = QS.FactorDB.TushareDB()
TSDB.connect()
print(TSDB.TableNames)
FT = TSDB.getTable(table_name="A股日线行情")
High, Low = FT.getFactor("最高价"), FT.getFactor("最低价")
Mid = QS.FactorDB.Factorize((High + Low) / 2, factor_name="中间价")

DTs = High.getDateTime(start_dt=dt.datetime(2018, 9, 1), end_dt=dt.datetime(2018, 9, 5))
IDs = High.getID()[:5]
Data = {"最高价": High.readData(ids=IDs, dts=DTs),
           "最低价": Low.readData(ids=IDs, dts=DTs),
           "中间价": Mid.readData(ids=IDs, dts=DTs)}
HDB = QS.FactorDB.HDF5DB(sys_args={"主目录":"/home/work/trade/QuantStudio/HDF5Data"})
HDB.connect()
print(HDB.TableNames)
HDB.writeData(data=pd.Panel(Data), table_name="TestTable")

from QuantStudio import __QS_ConfigPath__
print(__QS_ConfigPath__)