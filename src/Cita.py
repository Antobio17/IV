from datetime import datetime

class Cita:
    def __init__(self,telefono,dia,turno,tipo_de_cita):
        self.telefono=telefono
        self.dia=dia
        self.turno=turno
        self.tipo_de_cita=tipo_de_cita #Esta tiene que ser un diccionario

    def MuestraCita(self):
        print("Telefono usuario:",self.telefono,"\nDia:",self.dia
        ,"\nTurno:",self.turno,)
        print("\nTipo de cita:",self.tipo_de_cita['name'])
        print("\nTiempo trabajo incial:",self.tipo_de_cita['time']['work1'])
        print("\nTiempo trabajo pausa:",self.tipo_de_cita['time']['pause'])
        print("\nTiempo trabajo final:",self.tipo_de_cita['time']['work2'])

    def IntroduceCita(self):
        self.telefono = input("Telefono del usuario: ")
        self.dia = input("Fecha: ")
        self.turno = input("Turno: ")
        self.tipo_de_cita['name'] = input("Tipo de cita: ")
        self.tipo_de_cita['time']['work1'] = input("Tiempo que se tarda al principio: ")
        self.tipo_de_cita['time']['pause'] = input("Tiempo de pausa: ")
        self.tipo_de_cita['time']['work2'] = input("Tiempo para finalizar: ")
        
