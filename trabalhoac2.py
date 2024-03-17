


ano = int(input("digite o ano que voce quer analisar"))

bissexto = (ano % 4 == 00 and (ano %  100 != 00 or ano % 400 == 00))


def bissexto(ano):
     if ano == bissexto:
       print("seu ano bissexto é", True) 
     else:
      print("seu ano bissexto é", False)

bissexto(ano)





# DADOS

valor_hora = float(input("insira o salrio recebido por hora:"))
num_horas =  float(input("insira o numero de horas trabalhadas:"))
imposto = 0.275

# desenvolvendo a funcao calcula salario
def calcula_salario(valor_hora, num_horas, imposto):
     return valor_hora * num_horas - imposto

# calcular o imposto de renda
def main():
     print("o salario sera", calcula_salario(valor_hora, num_horas, imposto))
main()



# criando funcao para eq de segundo grau

a  = float(input("digite o valor do coeficiente a: "))
b  = float(input("digite o valor do coeficiente b: "))
c  = float(input("digite o valor do coeficiente c: "))
delta = b**2 - 4*a*c

def eq_seg_grau(a ,b ,c ):
    return (-b - delta**0.5) / (2*a) or (-b + delta**0.5) / (2*a)
print(eq_seg_grau(a, b, c))