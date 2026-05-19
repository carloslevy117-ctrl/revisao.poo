class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Medico(Pessoa):
    def __init__(self, nome, endereco, especialidade, crm):
        super().__init__(nome, endereco)
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f"Médico: {self.nome} | Especialidade: {self.especialidade} | CRM: {self.crm}"


class MedicoEspecialista(Medico):
    def __init__(self, nome, endereco, especialidade, crm, registro_especialidade):
        super().__init__(nome, endereco, especialidade, crm)
        self.registro_especialidade = registro_especialidade

    def apresentar_medico(self):
        return f"Médico Especialista: {self.nome} | Especialidade: {self.especialidade} | CRM: {self.crm} | RQE: {self.registro_especialidade}"


class Paciente(Pessoa):
    def __init__(self, nome, endereco, cpf, contato, data_nascimento=None):
        super().__init__(nome, endereco)
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


medico_geral = Medico("Dr. Marcio Erick", "Av. Sao Jose, 117", "Dentista", "CRM/RN 123456")
medico_especialista = MedicoEspecialista("Dra. Maria d Lourdes", "Rua das Flores, 456", "Pediatria", "CRM/SP 987654", "RQE 4433")

corpo_clinico = [medico_geral, medico_especialista]

for medico in corpo_clinico:
    print(medico.apresentar_medico())