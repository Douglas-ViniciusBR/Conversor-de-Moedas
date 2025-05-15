taxas = {

    "BRL" : 1.00,
    "USD" : 5.61,
    "EUR" : 6.29,
    "GBP" : 7.43,
    "JPY" : 0.038,
} 
            
moeda_quantia = float(input("Qual é o valor que deseja converter?:"))
moeda_origem = input("Qual é a origem da moeda? EX: BRL, USD, EUR e etc..):")
converter = input("Deseja converter pra qual moeda?")

if moeda_origem in taxas and converter in taxas:
    valor_Real = moeda_quantia * taxas[moeda_origem] 
    valorFinal = valor_Real / taxas[converter]
    print("O valor convertido da", moeda_origem ,":", moeda_quantia , "É" , round(valorFinal, 2), converter)
else : 
    print("Moeda inválida. Porque não tente novamnete??")
