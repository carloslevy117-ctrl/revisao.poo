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
        self.__cpf = None
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        cpf_limpo = "".join(caractere for caractere in novo_cpf if caractere.isdigit())
        if len(cpf_limpo) == 11:
            self.__cpf = novo_cpf
        else:
            print(f"Erro: O CPF '{novo_cpf}' é inválido. Deve conter exatamente 11 dígitos.")

    def exibir_informacoes(self):
        data_na_string = self.data_nascimento if self.data_nascimento else "Não informada"
        return f"Paciente: {self.nome} | CPF: {self.cpf} | Data de Nascimento: {data_na_string}"

    def __str__(self):
        return f"Paciente: {self.nome} (CPF: {self.cpf})"


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
paciente1 = Paciente("Levy", "017.119.564-65", "(11) 99910-8817", "16/03/2001")

clinica = Clinica("Unidade Central")
clinica.adicionar_medico(medico1)
clinica.adicionar_paciente(paciente1)

agendamento1 = Agendamento(medico1, paciente1, "29/05/2026 10:30")

print(medico1.apresentar_medico())
print(paciente1)

paciente1.cpf = "017"
print(paciente1)

paciente1.cpf = "987.654.321-00"
print(paciente1)