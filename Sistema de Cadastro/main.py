# Programa de cadastro de Pacientes em um hospital psiquiátrico, unsando uma função
# lambda, cadastre as informações do paciente em um dicionario, além do cadastramento
# deve ter uma opção de ver todos os pacientes cadastrados, uma opção de apagar um
# cadastro, e uma de sair. No ato do cadastro peça as seguinte informações:
# Nome, data de nascimento, peso, altura e motivo do internamento, mas, o que será
# cadastrado é: nome, idade, IMC e motivo do internamento.
# obs: IMC = peso / altura²
# obs2: o IMC deve ser calculado usando uma função lambda
# obs3: o programa deve ser feito usando funções
# obs4: use a biblioteca datetime para calcular a idade

paciente = dict()
id = 1

escolha = input(
    "Escolha uma das opções:\n"
    "1 - Cadastrar um novo paciente.\n"
    "2 - Apagar um paciente da lista.\n"
    "3 - Ver todos os pacientes.\n"
    "Opção: "
)

match escolha:
    case "1":
        nome = input("Digite o nome completo do(a) paciente: ")
        idade = int(input("Digite a idade: "))
        nascimento = input("Digite o dia do nascimento, no formato DDMMYYYY: ")
        while len(nascimento) != 8:
            nascimento = input(f"Não entendi a data de nascimento fornecida ({nascimento})\n"
                        "Digite o dia do nascimento, no formato DDMMYYYY: ")
        peso = input("Digite o peso em quilogramas: ").replace(',', '.') # Replace permite o uso da vírgula
        altura = input("Digite a altura, em metros: ").replace(',', '.')
        while len(altura) > 4:
            altura = input("Não entendi o que você quis dizer.\n"
                            "Digite a altura, em metros: ").replace(',', '.')
        motivoInternacao = input("Digite o motivo da internação: ")
        print("Dados do paciente:\n"
                f"Nome: {nome}\n"
                f"Idade: {idade}\n"
                f"Data de nascimento: {nascimento[0:2]}/{nascimento[2:4]}/{nascimento[4:8]}\n"
                f"Peso: {peso} kg\n"
                f"Altura: {altura} metros.\n"
                f"Motivo da internação: {motivoInternacao}")
        conf = input("Os dados estão corretos?\n"
                    "s/n: ")
        if conf[0] == "s":
            paciente[id] = {
            "Nome": nome,
            "Idade":  idade,
            "Data de Nascimento": nascimento,
            "Peso":  peso,
            "Altura":  altura,
            "Motivo da Internação":  motivoInternacao
        }
        # configurar o else
        print(f"Paciente {nome} cadastrado com sucesso com o registro {id}.")
        id += 1

    case "2":
        idExclusao = int(input("Qual o ID do paciente que você deseja excluir?\n"
                  "ID: "))
        for id in idExclusao:
        