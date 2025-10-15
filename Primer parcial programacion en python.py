# Consigna
# Deberá desarrollar un programa en Python que simule una carrera simple de autos entre varios competidores. 
# El objetivo es aplicar los conceptos de Programación Orientada a Objetos, diseñando clases con atributos, 
# métodos y comportamiento coherente con el problema planteado.
# Clase Auto
# Cada auto debe tener los atributos:
# nombre (identificador del auto o del piloto).
# velocidad máxima (un número aleatorio o asignado manualmente).
# posición actual (inicialmente 0).
# Se recomienda definir un método avanzar() 
# que simule el movimiento del auto sumando a su posición una cantidad 
# aleatoria de metros por turno (por ejemplo, entre 10 y 100).
# Se debe implementar un método mostrar_estado() que imprima el nombre y la posición actual del auto.
# Clase Carrera
# La clase debe encargarse de coordinar la competencia entre varios autos.
# Debe incluir métodos para:
# Agregar autos a la carrera.
# Iniciar la carrera, ejecutando varios turnos en los que todos los autos avancen.
# Mostrar el progreso de cada participante en cada turno.
# Determinar el ganador, es decir, el auto que haya recorrido la mayor distancia al finalizar la cantidad de 
# turnos definida (por ejemplo, 5 turnos).
# En caso de empate, se deberá indicar explícitamente.
# Simulación de la carrera
# Crear al menos 3 autos con nombres distintos.
# Definir una carrera y agregar los autos creados.
# Ejecutar la simulación mostrando los avances en cada turno.
# Finalizada la carrera, mostrar el nombre del ganador y la distancia recorrida.

import random
from typing import List

class Auto:
    def __init__(self, nombre, velocidad_maxima):
        self.__nombre = nombre
        self.__velocidad_maxima = velocidad_maxima
        self.__posicion_actual = 0

    def set_posicion_actual(self, nueva_posicion):
        self.__posicion_actual += nueva_posicion
    
    def get_nombre(self):
        nombre = self.__nombre
        return nombre
    
    def get_velocidad_maxima(self):
        velocidad_maxima = self.__velocidad_maxima
        return velocidad_maxima
    
    def get_posicion_actual(self):
        posicion_actual = self.__posicion_actual
        return posicion_actual
    
    def avanzar_auto(self):
        self.set_posicion_actual(random.randint(5, self.get_velocidad_maxima()))
    
    def mostrar_estado(self):
        print(f"el auto {self.get_nombre()} esta en la posicion {self.get_posicion_actual()}")
    

class Carrera:
    def __init__(self, meta_carrera, cantidad_turnos):
        self.__lista_autos = []
        self.__meta_carrera = meta_carrera
        self.__cantidad_turnos = cantidad_turnos
    
    def set_lista_autos(self, auto):
        self.__lista_autos.append(auto)
    
    def get_lista_autos(self):
        lista_autos = self.__lista_autos
        return lista_autos
    
    def get_meta_carrera(self):
        meta_carrera = self.__meta_carrera
        return meta_carrera
    
    def get_cantidad_turnos(self):
        cantidad_turnos = self.__cantidad_turnos
        return cantidad_turnos

    def agregar_autos(self, auto : Auto):
        self.set_lista_autos(auto)
    
    def iniciar_carrera(self):
        turno_lista_autos : List[Auto] = self.get_lista_autos()
        random.shuffle(turno_lista_autos)
        ganador = []
        turnos_usados = 0

        while len(ganador) == 0 and turnos_usados < self.get_cantidad_turnos():
            print(f"\nTurno nro {turnos_usados+1}")
            for auto in turno_lista_autos:
                auto.avanzar_auto()
                if auto.get_posicion_actual() >= self.get_meta_carrera():
                    ganador.append(auto)
            self.mostrar_progresos_participantes(turno_lista_autos)
            turnos_usados += 1
        
        if ganador:
            self.mostrar_ganador(ganador[0])
        elif len(ganador) > 1:
            self.mostrar_empate(ganador)
        elif turnos_usados == self.get_cantidad_turnos():
            print("\nSe acabaron los turnos de los autos, no hubo ganador")

    
    def mostrar_progresos_participantes(self, lista_participantes: List[Auto]):
        for auto in lista_participantes:
            auto.mostrar_estado()

    def mostrar_ganador(self, auto_ganador : Auto):
        print(f"\nEl auto ganador es {auto_ganador.get_nombre()}")

    def mostrar_empate(self, autos_empatados : List[Auto]):
        print(f"\nEmpate, entre los autos:")
        for auto in autos_empatados:
            print(f"{auto.get_nombre()}")

def main():
    lista_autos_competidores = []
    meta = random.randint(50, 100)
    turnos = random.randint(6, 10)
    copa_piston = Carrera(meta, turnos)
    
    auto_1 = Auto("Rayo McQueen", random.randint(14,23))
    auto_2 = Auto("Chick Hicks", random.randint(5,15))
    auto_3 = Auto("Francesco Bernoulli", random.randint(12,18))
    auto_4 = Auto("Jackson Storm", random.randint(14,19))

    lista_autos_competidores.extend([auto_1, auto_2, auto_3, auto_4])

    for auto in lista_autos_competidores:
        copa_piston.agregar_autos(auto)
    
    print(f"Inicia carrera! \nLa meta son {meta} metros \nCon {turnos} turnos")
    copa_piston.iniciar_carrera()

if __name__ == "__main__":
    main()