from deep_translator import GoogleTranslator

texto = input("Digite a frase: ")
traducao = GoogleTranslator(source='auto', target='en').translate(texto)
print(traducao)
