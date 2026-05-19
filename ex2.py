class Medico:
    def __init__(self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f"Médico: {self.nome} | Especialidade: {self.especialidade} | CRM: {self.crm}"


class Paciente:
    def __init__(self, nome, cpf, contato, data_nascimento=None):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        data_na_string = self.data_nascimento if self.data_nascimento else "Não informada"
        return f"Paciente: {self.nome} | CPF: {self.cpf} | Data de Nascimento: {data_na_string}"


class Clinica:
    def __init__(self, nome_unidade):
        self.nome_unidade = nome_unidade
        self.__corpo_clinico = []
        self.__lista_pacientes = []

    def adicionar_medico(self, medico):
        self.__corpo_clinico.append(medico)

    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)


class Agendamento:
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora


medico1 = Medico("Dr. Marcio erick", "Dentista", "CRM/RN 123456")
paciente1 = Paciente("Levy", "017.119.564-65", "(11) 99999-8888", "16/03/2001")

clinica = Clinica("Unidade Central")
clinica.adicionar_medico(medico1)
clinica.adicionar_paciente(paciente1)

agendamento1 = Agendamento(medico1, paciente1, "29/05/2025 10:30")

print(medico1.apresentar_medico())
print(paciente1.exibir_informacoes())
print(f"Clinica: {clinica.nome_unidade}")
print(f"Agendamento confirmado para {agendamento1.paciente.nome} com o {agendamento1.medico.nome} em {agendamento1.data_hora}.")