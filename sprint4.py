def exibir_cabecalho():
    print("Bem-vindo ao Sistema de Agricultura Inteligente!")
    print("-----------------------------------------------------------")

def capturar_dados_usuario():
    while True:
        nome = input("Digite seu nome completo: ").strip()
        if nome:
            break
        else:
            print("Nome inválido. Por favor, tente novamente.")

    while True:
        cpf = input("Digite seu CPF (apenas números): ").strip()
        if len(cpf) == 11 and cpf.isdigit():
            break
        else:
            print("CPF inválido. Deve conter 11 números.")

    return nome, cpf

def exibir_menu():
    print("\n")
    print("1 - Escolher Tipo de Vegetal ou Fruta para Plantio")
    print("2 - Verificar Tipo de Solo")
    print("3 - Verificar Condições Climáticas")
    print("4 - Escolher Tipo de Fertilizante")
    print("5 - Tempo Aproximado de Plantio")
    print("6 - Prever Produtividade da Colheita")
    print("-----------------------------------------------------------")

def processar_escolha(escolha, opcoes_selecionadas):
    if escolha == 1:
        tipo_vegetal = input("Digite o tipo de vegetal ou fruta que deseja plantar: ").strip()
        print(f"Recomendação: O vegetal {tipo_vegetal} é adequado para sua região.")
        opcoes_selecionadas['Tipo de vegetal ou fruta'] = tipo_vegetal

    elif escolha == 2:
        tipo_solo = input("Digite o tipo de solo do seu terreno (argiloso, arenoso, etc.): ").strip().lower()
        print(f"Seu terreno possui solo do tipo {tipo_solo}. Recomendação: Adequado para cultivos como milho e soja.")
        opcoes_selecionadas['Tipo de solo'] = tipo_solo

    elif escolha == 3:
        clima = input("Digite as condições climáticas da região (seco, úmido, etc.): ").strip().lower()
        print(f"A região possui condições climáticas {clima}. Recomendação: Adequado para plantas resistentes ao calor.")
        opcoes_selecionadas['Condições climáticas'] = clima

    elif escolha == 4:
        fertilizante = input("Escolha o tipo de fertilizante que deseja utilizar: ").strip()
        print(f"Você escolheu o fertilizante do tipo {fertilizante}. Recomendação: Esse fertilizante é ótimo para plantas de crescimento rápido.")
        opcoes_selecionadas['Tipo de fertilizante'] = fertilizante

    elif escolha == 5:
        tempo_plantio = input("Digite o tempo aproximado de duração do plantio (em dias): ").strip()
        print(f"O plantio levará aproximadamente {tempo_plantio} dias.")
        opcoes_selecionadas['Tempo de plantio aproximado'] = tempo_plantio

    elif escolha == 6:
        if 'Tipo de vegetal ou fruta' in opcoes_selecionadas and 'Tipo de solo' in opcoes_selecionadas and 'Condições climáticas' in opcoes_selecionadas:
            previsao = prever_colheita(opcoes_selecionadas['Tipo de vegetal ou fruta'], opcoes_selecionadas['Tipo de solo'], opcoes_selecionadas['Condições climáticas'])
            print(f"Previsão de produtividade: {previsao}")
            opcoes_selecionadas['Previsão de produtividade'] = previsao
        else:
            print("Você precisa inserir o tipo de vegetal, tipo de solo e condições climáticas antes de prever a colheita.")
    else:
        print("Opção inválida!")

def exibir_opcoes_selecionadas(opcoes_selecionadas):
    print("\nOpções selecionadas:")
    for chave, valor in opcoes_selecionadas.items():
        print(f"{chave}: {valor}")

def prever_colheita(tipo_vegetal, tipo_solo, clima):
    # Simulação simples para prever o sucesso da colheita
    if tipo_solo == "argiloso" and clima == "seco":
        return "Baixa produtividade"
    elif tipo_vegetal == "milho" and tipo_solo == "arenoso":
        return "Produtividade média"
    else:
        return "Alta produtividade"

def main():
    exibir_cabecalho()
    nome, cpf = capturar_dados_usuario()

    opcoes_selecionadas = {}
    resp = 1

    while resp != 0:
        exibir_menu()
        escolha = int(input("Digite o número referente à informação que deseja acessar (1 - 6): "))
        processar_escolha(escolha, opcoes_selecionadas)

        print("\n")
        resp = int(input("Deseja continuar (1 - SIM, 0 - NÃO)? "))

    exibir_opcoes_selecionadas(opcoes_selecionadas)

    print("\n[Análise da Arquitetura de IA]")
    print("O sistema será projetado para integrar inteligência artificial, utilizando redes neurais para analisar tipos de solo, clima e prever colheitas.")
    print("A IA será treinada com dados históricos e condições locais para fornecer recomendações otimizadas para o agricultor.")

    print("\n[Base de Dados Utilizada]")
    print("A base de dados será composta por informações de clima e solo de fontes agrícolas locais e globais.")
    print("Esses dados alimentarão o modelo de IA para gerar previsões e recomendações adequadas para cada tipo de cultivo.")

if __name__ == "__main__":
    main()
