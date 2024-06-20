from modelos.medico import Medico
from modelos.hospital import Hospital
from modelos.paciente import Paciente

med_beatriz = Medico("Dra. Ana", "Urologia", "159263478", 3)
med_antonio =  Medico("Dr. Carlos", "Cardiologia", "45656444", 1)
med_ana = Medico("Dra. Ana", "Pediatria", "987654321", 2)
med_maria = Medico("Dr. Maria", "Neurologia", "456789123", 2)
med_joana = Medico("Dra. Joana", "Dermatologia", "321654987", 2)
med_jose = Medico("Dr. Jose", "Ortopedia", "789123456", 1)
med_pedro = Medico("Dr. Pedro", "Oncologia", "654987321", 1)

hospital_clinicas_itajuba = Hospital('Hospital das clínicas de Itajubá', 'Morro Chic', 359999999)
unimed = Hospital ('Unimed', 'BPS', 359955999) 

paciente_carlos = Paciente("Carlos", "UTI", "159263478", 3)
paciente_messias =  Paciente("Messias", "ALA-1", "45656444", 1)
paciente_josé = Paciente("José", "ALA-2", "987654321", 2)

hospital_clinicas_itajuba.adicionar_medico(med_beatriz)
hospital_clinicas_itajuba.adicionar_medico(med_ana)
hospital_clinicas_itajuba.adicionar_medico(med_maria)
hospital_clinicas_itajuba.adicionar_medico(med_maria)
hospital_clinicas_itajuba.adicionar_medico(med_maria)

unimed.adicionar_medico(med_pedro)
unimed.adicionar_medico(med_joana)


def main():
    hospital_clinicas_itajuba.exibir_medicos()
    hospital_clinicas_itajuba.adicionar_hospital

    

if __name__ == "__main__":
    main()