# ------------------------------------------------------------
# Algoritmo:
# Receber o número de horas trabalhadas e o valor do salário mínimo.
# Calcular e mostrar o salário a receber seguindo as regras:
#
# a) O valor da hora trabalhada vale a metade do salário mínimo.
# b) O salário bruto equivale ao número de horas trabalhadas
#    multiplicado pelo valor da hora trabalhada.
# c) O imposto equivale a 3% do salário bruto.
# d) O salário a receber equivale ao salário bruto menos o imposto.
# ------------------------------------------------------------

horas = int(input("Informe o número de horas trabalhadas:  "))
salario_min = float(input("Informe o valor do salario minimo: "))

valor_hora = salario_min / 2

bruto_ = horas * valor_hora

imposto = bruto_ * 0.03

valor_receber = bruto_ - imposto

print(valor_receber)