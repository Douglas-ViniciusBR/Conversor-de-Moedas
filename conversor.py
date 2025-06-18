from datetime import datetime

# Dicionário de taxas fixas de câmbio (base: BRL)
taxas = {
    "BRL": 1.00,
    "USD": 5.61,
    "EUR": 6.29,
    "GBP": 7.43,
    "JPY": 0.038,
}

# Exibe as moedas disponíveis
def exibir_moedas_disponiveis():
    print("\n💱 Moedas disponíveis para conversão:")
    for moeda in taxas:
        print(f" - {moeda}")

# Função que realiza a conversão
def converter_moeda(valor, origem, destino):
    valor_em_reais = valor * taxas[origem]
    valor_convertido = valor_em_reais / taxas[destino]
    return round(valor_convertido, 2), valor_em_reais

# Lista para armazenar histórico local
historico = []

print("🌐 === CONVERSOR DE MOEDAS ===")

# Loop principal do sistema
while True:
    exibir_moedas_disponiveis()
    
    try:
        entrada = input("\n🧮 Digite o valor que deseja converter: ").replace(",", ".")
        valor = float(entrada)
        if valor <= 0:
            print("⚠️ O valor deve ser maior que zero.")
            continue
    except ValueError:
        print("❌ Valor inválido! Digite apenas números.")
        continue

    origem = input("🔁 Digite o código da moeda de origem: ").strip().upper()
    destino = input("➡️ Digite o código da moeda de destino: ").strip().upper()

    if origem not in taxas or destino not in taxas:
        print("❌ Moeda inválida. Verifique os códigos disponíveis.")
        continue

    resultado, valor_em_reais = converter_moeda(valor, origem, destino)

    # Captura data e hora atual
    agora = datetime.now()
    timestamp = agora.strftime("%d/%m/%Y %H:%M:%S")

    # Resultado da conversão
    print(f"\n✅ Conversão realizada com sucesso em {timestamp}")
    print(f"🔎 {valor} {origem} → {valor_em_reais:.2f} BRL → {resultado} {destino}")
    print(f"💹 Taxa utilizada: 1 {origem} = {taxas[origem]} BRL")
    print(f"💹 Taxa destino: 1 {destino} = {taxas[destino]} BRL")

    # Salva no histórico da sessão
    historico.append(f"[{timestamp}] {valor} {origem} → {resultado} {destino}")

    # Exibe últimas 5 conversões feitas
    if historico:
        print("\n🧾 Histórico de conversões nesta sessão:")
        for item in historico[-5:]:
            print(f" - {item}")

    # Pergunta se deseja continuar
    repetir = input("\n🔄 Deseja fazer outra conversão? (S/N): ").strip().upper()
    if repetir != "S":
        print("\n👋 Encerrando o conversor... Obrigado por usar! 💱")
        break

