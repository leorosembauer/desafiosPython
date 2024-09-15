def calcular_percentuais(faturamento_por_estado):
    valor_total = sum(faturamento_por_estado.values())

    percentuais = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / valor_total) * 100
        percentuais[estado] = percentual
    
    return percentuais

faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentuais(faturamento_por_estado)

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
