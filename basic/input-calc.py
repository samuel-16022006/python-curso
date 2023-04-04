def sum(val1,val2):
    result = float(val1) + float(val2)
    return str(result)

def multiply (val1, val2):
    result = float(val1) * float(val2)
    return str(result)
    
print("\n\t| Calculadora |\n")
value_1 = input("| Digite o 1º valor: ")
value_2 = input("| Digite o 2º valor: ")
# result = sum(value_1,value_2) 
result = multiply(value_1,value_2)
# result = subtract(value_1,value_2)
# result = divide(value_1,value_2)
print("| Resultado: "+result+"\n\n")


