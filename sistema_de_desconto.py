total = float(input("Insira o valor do produto: "))
desconto = float(input("Insira o valor do desconto: "))

num_desconto = (desconto * 100)/100 #transformando ele em porcentagem

quanto_representa = total * (num_desconto/100) #calculando quanto a porcentagem do produto representa dele

resultado = total - quanto_representa

print(f"O produto com desconto de {num_desconto}% é igual a {resultado}")