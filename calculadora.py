salario = float(input("Digite aqui o valor bruto de seu salário. Utilize '.', e não vírgula:\n"))
desconto = float(input("Digite aqui o valor dos descontos em seu holerite. Utilize '.', e não vírgula:\n"))

bonus_setembro = 200
salario_liquido = salario - desconto

if salario <= 3000:
    salario_liquido += bonus_setembro
    print("Parabéns! Você recebeu um bônus de R$ 200! Aqui está o cálculo do seu salário.")
else:
    print("Aqui está o cálculo do seu salário")

total_anual = salario_liquido * 12
salario_por_dia = salario_liquido / 30

print("Seu salário líquido do mês de setembro é de:", salario_liquido)
print("Seu salário anual é de:", total_anual)
print("Esse é o valor que você recebe por dia:", salario_por_dia)
