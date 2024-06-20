class Paciente:
    def __init__(self, nome_paciente, status_Paciente, setor_paciente):
        self.paciente = nome_paciente
        self.status_Paciente = status_Paciente
        self.setor_paciente = setor_paciente
        
    
    def exibir_status_paciente(self):
        if self.status_Paciente:
            print(f" 💛 O paciente {self.nome_Paciente} segue repousando e em tratamento no setor {self.setor_paciente}.")
        elif self.status_Paciente:
            print(f" 💚 O paciente {self.nome_Paciente} esta de alta do {self.setor_paciente}")
        else:
            print(f" ❤️ ️O quadro do paciente {self.nome_Paciente} Nao esta ok. Estado de alerta. Informe o medico responsovel para que ele alinhe com o titular.")
        print(f"Setor do paciente: {self.setor_paciente}")