def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8.0
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8.0
    return bitsCalculado

def byteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    KilobytesCalculado = valorASerConvertido * 1024.0
    return KilobytesCalculado

def KilobyteParabyte(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 1024.0
    return bitsCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaKilobyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)