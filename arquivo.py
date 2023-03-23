from calc import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKilobyte, KilobyteParabyte, KilobyteParaMegabyte, MegabyteParaKilobyte, MegabyteParaGigabyte, GigabyteParaMegabyte, GigabyteParaTerabyte, TerabyteParaGigabyte, TerabyteParaPetabyte, PetabyteParaTerabyte

print(' Digite 1 para bitParabyte \n 2 para byteParaBit \n 3 para byteParaKilobyte \n 4 para KilobyteParabyte \n 5 para KilobyteParaMegabyte \n 6 para MegabyteParaKilobyte \n 7 para MegabyteParaGigabyte \n 8 para GigabyteParaMegabyte \n 9 para Gigabyte para Terabyte \n 10 para Terabyte para Gigabyte \n 11 para Terabyte para Petabyte \n 12 para Petabyte para Terabyte ')
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

elif(FuncEscolha == '7'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = MegabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '8'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = GigabyteParaMegabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '9'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = GigabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '10'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = TerabyteParaGigabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '11'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = TerabyteParaPetabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(FuncEscolha == '12'):
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = PetabyteParaTerabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)