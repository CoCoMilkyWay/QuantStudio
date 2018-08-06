x = sdpvar(nVar,1);
genYalmipConstraint;% ����Լ������
%% �趨�Ż�Ŀ��
if isequal(Objective.type,'Linear')
    OptObjective = (Objective.f' * x);
elseif isequal(Objective.type,'Quadratic')
    if isfield(Objective,'X')
        OptObjective = (x'*(Objective.X*Objective.F*Objective.X'+diag(Objective.Delta))*x + Objective.Mu'*x);
    else
        OptObjective = (x'*Objective.Sigma*x + Objective.Mu'*x);
    end
elseif isequal(Objective.type,'L1_Linear')
    OptObjective = (Objective.f' * x + Objective.lambda * norm(x-Objective.c,1));
elseif isequal(Objective.type,'L1_Quadratic')
    if isfield(Objective,'X')
        OptObjective = (x'*(Objective.X*Objective.F*Objective.X'+diag(Objective.Delta))*x + Objective.Mu'*x + Objective.lambda*norm(x-Objective.c,1));
    else
        OptObjective = (x'*Objective.Sigma*x + Objective.Mu'*x + Objective.lambda*norm(x-Objective.c,1));
    end
end
%% �����Ż�ѡ��
OptimOptions = sdpsettings();
if isfield(Options,'Display') && (~isequal(Options.Display,'Default'))
    OptimOptions.verbose = str2double(Options.Display);
end
if isfield(Options,'Solver') && (~isequal(Options.Solver,'Default'))
    OptimOptions.solver = Options.Solver;
end
%% ���
ResultInfo = optimize(Constraints,OptObjective,OptimOptions);
if ResultInfo.problem==0
    ResultInfo.Status = 1;
else
    ResultInfo.Status = 0;
end
ResultInfo.ErrorCode = ResultInfo.problem;
ResultInfo.Msg = ResultInfo.info;
x = value(x);
yalmip('clear');