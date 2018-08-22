
sexoMas = sexoFem = peso = anoutili = 0
criancaANC = altura = dia = ano = mes = 0
totalcardio= totalmicro= totalplano= totalDiabete = 0
percentMicro = percentcardio= percentplano= percentMas= percentFem= percentDiabete = 0
percentImc = totalIMC = opcao = 0
opcaoPerguntas = ""
sexos = "sexo"
imc = 0
opcaoLaco = True
print("Hello World !!!")
print("\n")
print("Bem Vindo ao programa de cadastro de crianças")
print("\n")
print("Digite o ano que está utilizando o aplicativo ?")

anoutili = int(input())

while (anoutili > 2018) or (anoutili == 0):
  print("Digite um ano valido ")
  anoutili = int(input())


while(opcaoLaco == True):

  print("Digite 1 para cadastro")
  print("Digite 2 para relatório")
  print("Digite 0 para finalizar o programa")
  opcao = int(input())

  if opcao == 1:
    print("CADASTRO DE CRIANÇAS")
    dia = int(input("Informe a dia de nascimento: "))
    mes = int(input("Informe a mes de nascimento: "))
    ano = int(input("Informe a ano de nascimento: "))

    while (dia > 31) or (dia < 1) or (mes > 12) or (mes < 0) or (ano > anoutili) or (ano == 0) or ((anoutili - ano) > 12):
      print("Dados inválidos !")
      dia = int(input("Informe a dia de nascimento: "))
      mes = int(input("Informe a mes de nascimento: "))
      ano = int(input("Informe a ano de nascimento: "))
    
    if ano == anoutili:
      criancaANC+=1
    
    peso = int(input("Digite o peso da criança: "))
    altura = float(input("Digite a altura da criança: "))

    if altura or peso == 0:
      peso = int(input("Digite novamente o peso da criança: "))
      altura = float(input("Digite novamente a altura da criança: "))

    sexo = input("Digite o sexo da criança: ")
    if sexo == 'Masculino' or sexo == 'masculino':
       sexoMas+=1
    if sexo == 'Feminino' or sexo == 'feminino':
      sexoFem+=1

    opcaoPerguntas = input("A criança possui microcefalia ?")

    while opcaoPerguntas != 'sim' or opcaoPerguntas != 'não':

     opcaoPerguntas = input("Dado inválido ! A criança possui microcefalia ?")
    
    if opcaoPerguntas == 'Sim' or opcaoPerguntas == 'sim':
      totalmicro+=1
    
    opcaoPerguntas = input("A criança possui problema cardiaco ?")

    while opcaoPerguntas != "sim" or opcaoPerguntas != "não":
      
      opcaoPerguntas = input("Dado inválido ! A criança possui problema cardiaco ?")
    
    if opcaoPerguntas == 'Sim' or opcaoPerguntas == 'sim':
      totalcardio+=1

    opcaoPerguntas = input("A criança possui diabetes ?")

    while opcaoPerguntas != "sim" or opcaoPerguntas != "não":
      
      opcaoPerguntas = input("Dado inválido ! A criança possui diabetes ?")
    
    if opcaoPerguntas == 'Sim' or opcaoPerguntas == 'sim':
      totalDiabete+=1

    opcaoPerguntas = input("A criança possui plano de saude ?")

    while opcaoPerguntas != "sim" or opcaoPerguntas != "não":
      
      opcaoPerguntas = input("Dado inválido ! A criança possui plano de saude ?")
    
    if opcaoPerguntas == 'Não' or opcaoPerguntas == 'não':
      totalplano+=1

    
    criancaANC = criancaANC + 1
    percentcardio = (totalcardio * 100)/criancaANC
    percentDiabete = (totalDiabete * 100)/criancaANC
    percentplano = (totalplano * 100)/criancaANC
    percentcardio = (totalcardio * 100)/criancaANC
    percentFem = (sexoFem * 100)/criancaANC
    percentMas = (sexoMas * 100)/criancaANC
    imc = (altura * altura)/peso
    if imc > 25:
      totalIMC+=1
    percentImc = (totalIMC *100)/criancaANC

  if opcao == 2:
    print("Relatório Parcial")
    print("/n")
    print("Crianças cadastradas: "+ criancaANC)
    print("Percentual de crianças com microcefalia: "+ percentMicro)
    print("Percentual de crianças com diabetes : "+ percentDiabete)
    print("Percentual de crianças sem plano e saude: "+ percentplano)
    print("Percentual de meninos: "+percentMas)
    print("Percentual de meninas: "+percentFem)
    print("Percentual de crianças acima do peso: "+percentImc)
  
  if opcao == 0:
    opcaoLaco = False

