import pulp

def readInput():
    global t, p, max_production, toys, packages
    t, p, max_production = [int(num) for num in input().split()]
    toys = [list(map(int, input().split())) for i in range(t)]
    packages = [list(map(int, input().split())) for i in range(p)]
    return 0

def main():
    readInput()
    

    prob = pulp.LpProblem("Lucro Máximo", pulp.LpMaximize)

    # Variáveis de Decisão
    x = []
    for i in range(t):
        x.append(pulp.LpVariable(f"x{i}", lowBound= 0, cat= 'Integer'))
    y = []
    for j in range(p):
        y.append(pulp.LpVariable(f"y{j}", lowBound= 0, cat= 'Integer'))

    # Função Objetivo
    prob += pulp.lpSum([toys[i][0]*x[i] for i in range(t)]) + pulp.lpSum([packages[j][3] * y[j] for j in range(p)])

    # Restrições
    # Capacidade de cada brinquedo
    for i in range(t):
        prob += x[i] <= toys[i][1]

    # Quantidade máxima total
    prob += pulp.lpSum(x) + 3* pulp.lpSum(y) <= max_production

    prob.solve()

    return 0

if __name__ == "__main__":
    main()