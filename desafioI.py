def sum_result():
    i = 13  
    soma = 0  
    k = 0  

    while k < i:
        k += 1  
        soma += k 
    return soma

resultado = sum_result()
print(f"soma: {resultado}")