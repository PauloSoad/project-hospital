class Medico:
    def __init__(self, nome_medico, especialidade_medico, telefone_medico, status_medico):
        self.nome_medico = nome_medico
        self.especialidade_medico = especialidade_medico
        self.telefone_medico = telefone_medico
        self.status_medico = status_medico

    def __str__(self) -> str:
        
        return f'Medico: {self.nome_medico} | Especialidade: {self.especialidade_medico}'

    def exibir_local_medico(self):
        if self.status_medico == 1:
            print(f" 💚 O Médico {self.nome_medico} se encontra no hospital.")
        elif self.status_medico == 2:
            print(f" 💛 O Médico esta de férias {self.nome_medico}")        
        else:
            print(f" ❤️️ Alerta! O medico {self.nome_medico} encontra-se ausente. Informe o medico de plantao para que ele alinhe com o titutar.")
        print(f"Telefone do medico: {self.telefone_medico}")



        