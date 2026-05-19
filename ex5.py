from abc import ABC, abstractmethod


class PacienteNaoCadastradoError(Exception):
    def __init__(self, cpf):
        self.cpf = cpf
        super().__init__(f"Erro: O paciente com CPF {cpf} não está cadastrado na clínica.")


class DocumentoSaude(ABC):
    @abstractmethod
    def gerar_relatorio(self):
        pass


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

    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.__lista_pacientes:
            if paciente.cpf == cpf:
                return paciente
        raise PacienteNaoCadastradoError(cpf)


class Agendamento(DocumentoSaude):
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora

    def gerar_relatorio(self):
        return (
            f"--- RELATÓRIO DE AGENDAMENTO ---\n"
            f"Horário: {self.data_hora}\n"
            f"Médico: {self.medico.nome} ({self.medico.especialidade})\n"
            f"Paciente: {self.paciente.nome} (CPF: {self.paciente.cpf})\n"
            f"--------------------------------"
        )


medico1 = Medico("Dr. Marcio Erick", "Av. Sao Jose, 117", "Dentista", "CRM/RN 123456")
paciente1 = Paciente("Levy", "017.119.564-65", "(84) 99910-8817", "16/03/2001")

clinica = Clinica("Unidade Central")
clinica.adicionar_medico(medico1)
clinica.adicionar_paciente(paciente1)

agendamento1 = Agendamento(medico1, paciente1, "29/05/2026 10:30")
print(agendamento1.gerar_relatorio())

print("\n---  Buscando Paciente ---")
try:
    paciente_encontrado = clinica.buscar_paciente_por_cpf("017.119.564-65")
    print(f"Paciente encontrado com sucesso: {paciente_encontrado.nome}")
except PacienteNaoCadastradoError as erro:
    print(erro)

try:
    paciente_encontrado = clinica.buscar_paciente_por_cpf("117.017.295-10")
    print(f"Paciente encontrado com sucesso: {paciente_encontrado.nome}")
except PacienteNaoCadastradoError as erro:
    print(erro)