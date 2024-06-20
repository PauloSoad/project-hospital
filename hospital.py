class Hospital:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self._medicos = []

    def __str__(self) -> str:
        pass

    def adicionar_medico(self, medico):
        self._medicos.append(medico)

    def exibir_medicos(self):
        print(f'Os médicos do hospital: {self.nome}')
        for i, medico in enumerate(self._medicos, start=1):            
            mensagem = f'{i} | Nome: {medico.nome_medico} | Categoria: {medico.especialidade_medico}'
            print(mensagem)

    def adicionar_hospital(self, hospital):
        self._medicos.append(hospital)

    

    



            
