import cvxpy as cp

x_M = cp.Variable(nonneg=True)

x_S = cp.Variable(nonneg=True)

objective = cp.Maximize(160*x_M + 100*x_S)

constraints = [
    2 * x_M + 2* x_S <=8,
    2*x_M + x_S <= 6
]

problem = cp.Problem(objective, constraints)
problem.solve()

print(f"Estado: {problem.status}")
print(f"Valor optimo: {round(problem.value)}")
print(f"x_M: {round(x_M.value)}")
print(f"x_S: {round(x_S.value)}")