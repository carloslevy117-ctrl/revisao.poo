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
#testando o codigo:
class Medico:
    def __init__(self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f"Médico: {self.nome} | Especialidade: {self.especialidade} | CRM: {self.crm}"


class Paciente:
    def __init__(self, nome, cpf, contato, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento

    def exibir_informacoes(self):
        data_na_string = self.data_nascimento if self.data_nascimento else "Não informada"
        return f"Paciente: {self.nome} | CPF: {self.cpf} | Data de Nascimento: {data_na_string}"

#testando:
medico_teste = Medico("Dr. Marcio erick", "Dentista", "CRM/RN 123456")
print(medico_teste.apresentar_medico())

paciente_teste = Paciente("Ceica", "017.119.564-65", "(11) 99999-8888", "16/03/2001")
print(paciente_teste.exibir_informacoes())
