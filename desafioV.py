def inverter_string(s):
    resultado = ""
    
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

entrada = input("Digite a nome para inverter: ")

string_invertida = inverter_string(entrada)
print("O nome invertido:", string_invertida)
