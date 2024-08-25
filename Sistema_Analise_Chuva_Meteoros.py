import math
fim = False
cont_op = 0
propriedade = False
upmcc = False
meteoro = False
registros = False
while not fim:

# Menu
  print("-:: Sistema para Análise de Chuva de Meteoros ::-")
  op = int(input(" 1. Definir perímetro da propriedade e da edificação de interesse\n 2. Unificar sistemas de coordenadas de referência \n 3. Processar registros de chuva de meteoros \n 4. Apresentar estatísticas \n 5. Sair \n Opção: "))

# Define o perímetro da propriedade e da sede
  if op == 1:
    print("\n -::Definir perímetro da propriedade e da sede::-")
    print("Propriedade:")
    menor_x_propriedade = float(input("Digite o menor x: "))
    menor_y_propriedade = float(input("Digite o menor y: "))
    maior_x_propriedade = float(input("Digite o maior x: "))
    maior_y_propriedade = float(input("Digite o maior y: "))
    print("\nSede:")
    menor_x_sede = float(input("Digite o menor x: "))
    menor_y_sede = float(input("Digite o menor y: "))
    maior_x_sede = float(input("Digite o maior x: "))
    maior_y_sede = float(input("Digite o maior y: "))
    propriedade = True
    print("\n")    
    
# Unifica os sistemas de coordenadas de referência
  elif op == 2:
    print("\n-:: Unificar sistemas de coordenadas de referência ::-")
    print("UPMCC:")
    x_upmcc = float(input("Digite o x: "))
    y_upmcc = float(input("Digite o y: "))
    print("\n")
    upmcc = True

# Registra a chuva de meteoros
  elif op == 3:
    quadranteNO = 0
    quadranteNE = 0
    quadranteSO = 0
    quadranteSE = 0
    if propriedade == False:
      print("\nImpossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada.\n")
    elif upmcc == False:
      print("\nImpossível processar qualquer registro de queda no momento: não foi feita a unificação dos sistemas referenciais usados nos cálculos.\n")
    else:
      meteoros_sede = 0
      meteoros_propriedade = 0
      meteoros_total = 0
      cont = 1
      while not registros:
        print(f"\n-:: Registro #{cont} ::-")
        r = float(input("-> Distância: "))
        if r <= 0:
          registros = True
        else:
          theta = float(input("-> Ângulo: "))
          meteoro = True 
          meteoros_total = meteoros_total + 1
          cont = 1 + cont
          x_unificado = (math.cos(theta * ((2 * math.pi ) / 360)) * r) + x_upmcc
          y_unificado = (math.sin(theta * ((2 * math.pi ) / 360)) * r) + y_upmcc

          
        if x_unificado >= menor_x_propriedade and x_unificado <= maior_x_propriedade and y_unificado >= menor_y_propriedade and y_unificado <= maior_y_propriedade:
          meteoros_propriedade = meteoros_propriedade + 1
    
          if x_unificado <= 0 and y_unificado >= 0:
            quadranteNE += 1
          elif x_unificado >= 0 and y_unificado >= 0:
            quadranteNO += 1
          elif x_unificado <= 0 and y_unificado <= 0:
            quadranteSO += 1
          elif x_unificado >= 0 and y_unificado <= 0:
            quadranteSE += 1

        elif x_unificado >= menor_x_sede and x_unificado <= maior_x_sede and y_unificado >= menor_y_sede and y_unificado <= maior_y_sede:
          meteoros_sede = meteoros_sede + 1
          meteoros_sede == True
          
      print(f"\nFim da coleta de registros: {meteoros_total} queda(s) informada(s).\n")

# Apresenta as estatísticas do menu
  elif op == 4:
        if propriedade == False:
          print("\nImpossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada.\n")
        elif upmcc == False:
          print("\nImpossível processar qualquer registro de queda no momento: não foi feita a unificação dos sistemas referenciais usados nos cálculos.\n")
        elif meteoro == False: 
          print("\nImpossível processar qualquer registro de queda no momento: não foram feitos os registros de meteoros.\n")
        else:
          quedas_propriedade = (meteoros_propriedade * 100) / meteoros_total 
          porcentagem_total = (meteoros_total * 100) / meteoros_total 
          porcentagem_quadranteNE = (quadranteNE * 100) / meteoros_total
          porcentagem_quadranteNO = (quadranteNO * 100) / meteoros_total
          porcentagem_quadranteSO = (quadranteSO * 100) / meteoros_total
          porcentagem_quadranteSE = (quadranteSE * 100) / meteoros_total
          print(f"\nTotal de quedas registradas: {meteoros_total} ({porcentagem_total}%)")
          print(f"Quedas dentro da propriedade: {meteoros_propriedade} ({quedas_propriedade:.2f}%)")
          print(f"-> Quadrante NE: {quadranteNE} ({porcentagem_quadranteNE:.2f}%)")
          print(f"-> Quadrante NO: {quadranteNO} ({porcentagem_quadranteNO:.2f}%)")
          print(f"-> Quadrante SO: {quadranteSO} ({porcentagem_quadranteSO:.2f}%)")
          print(f"-> Quadrante SE: {quadranteSE} ({porcentagem_quadranteSE:.2f}%)")
          if meteoros_sede == True:
            caiu_sede = "SIM"
          else:
            caiu_sede = "NÃO"
          print(f"A edificação principal foi atingida? {caiu_sede}\n")

# Finaliza o programa
  elif op == 5:
      fim = True
  else:
    print("\nOpção inválida!\n")
print("Programa finalizado, obrigado! :)")
