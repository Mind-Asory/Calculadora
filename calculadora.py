print ("****Calculadora****")

n1 = input ("Entre com o primeiro número: ")
n2 = input ("Entre com o segundo número: ")

n1 = int(n1)
n2 = int(n2)

print ("DIGITE A OPERAÇÃO DESEJADA")
operacao = input ("Digite 1 para somar;\nDigite 2 para subtrair;\nDigite 3 para multiplicação;\nDigite 4 para dividir\n").

if operacao == "1":
    print (" A soma é:",n1+n2)
elif operacao == "2":
    print (" A subtração é:",n1-n2)
elif operacao == "3":
    print (" A multiplicação é:",n1*n2)
elif operacao == "4":
    print (" A divisão é:",n1/n2)
else:
    print ("operação inválida, por favor tente novamente")