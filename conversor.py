#Conversor de Moedas - Estrutura Inicial + Validações

# Tabela de taxas de conversão em relação ao Real (BRL)
taxas = {
    "BRL": 1.00,   # Real Brasileiro (referência base)
    "USD": 5.61,   # Dólar Americano
    "EUR": 6.29,   # Euro
    "GBP": 7.43,   # Libra Esterlina
    "JPY": 0.038,  # Iene Japonês
}

# Função para exibir as moedas suportadas
def exibir_moedas_disponiveis():
    print("\nMoedas disponíveis:")
    for moeda in taxas:
        print(f" - {moeda}")

#Cabeçalho do programa
print("=== CONVERSOR DE MOEDAS ===")
exibir_moedas_disponiveis()

# ntrada de dados do usuário
try:
    moeda_quantia = float(input("\nDigite o valor que deseja converter: "))
except ValueError:
    print("Erro: Valor inválido! Digite apenas números.")
    exit()

moeda_origem = input("Digite o código da moeda de origem: ").upper()
moeda_destino = input("Digite o código da moeda de destino: ").upper()

# Validação das moedas digitadas
if moeda_origem not in taxas or moeda_destino not in taxas:
    print("Moeda inválida. Verifique os códigos e tente novamente.")
    exit()
