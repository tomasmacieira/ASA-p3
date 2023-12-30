from pulp import *

def readInput():
    global t, p, max_production, toys, packages
    t, p, max_production = [int(num) for num in input().split()]
    toys = [list(map(int, input().split())) for i in range(t)]
    packages = [list(map(int, input().split())) for i in range(p)]

def main():
    readInput()

    prob = pulp.LpProblem("Lucro_Máximo", LpMaximize)

    # Variáveis de Decisão
    var_toys = [pulp.LpVariable(f"var_toys_{i}", lowBound=0,cat='Continuous') for i in range(t)]
    
    var_pack = [pulp.LpVariable(f"var_pack_{j}", lowBound=0,cat='Continuous') for j in range(p)]
    
    # Função Objetivo
    prob += pulp.lpSum([toys[i][0]*var_toys[i] for i in range(t)]) + pulp.lpSum([packages[j][3]*var_pack[j] for j in range(p)])

    # Restrições
    # Capacidade de cada brinquedo
    for i in range(t):
        prob += var_toys[i] + pulp.lpSum(var_pack[j] for j in range(p) if i+1 in packages[j][:3]) <= toys[i][1]

    # Quantidade máxima total
    prob += pulp.lpSum(var_toys) + (3 * pulp.lpSum(var_pack)) <= max_production

    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    print(round(pulp.value(prob.objective)))

if __name__ == "__main__":
    main()
