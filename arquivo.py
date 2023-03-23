from calc import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKilobyte, KilobyteParabyte, KilobyteParaMegabyte, MegabyteParaKilobyte, MegabyteParaGigabyte, GigabyteParaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParaPetabyte, P

print(' Digite 1 para bitParabyte \n 2 para byteParaBit \n 3 para byteParaKilobyte \n 4 para KilobyteParabyte \n 5 para KilobyteParaMegabyte \n 6 para MegabyteParaKilobyte \n 7 para MegabyteParaGigabyte \n 8 para GigabyteParaMegabyte \n 9 para  ')
FuncEscolha = input()
if(FuncEscolha == '1'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '2'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '3'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = byteParaKilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '4'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = KilobyteParabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '5'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = KilobyteParaMegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '6'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = MegabyteParaKilobyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)