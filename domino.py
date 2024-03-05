import time;
import random
import copy
import numpy as np
import os
'''
Chelkyn
'''
class FichaDomino:
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self):
        return f'[{self.izquierda}|{self.derecha}]'


class Domino():

    def __init__(self, amountPlayer, IA_duraction, jugadoresMaquina):

        self.PrimeraJugada = False
     
        self.amountPlayer = amountPlayer
        self.jugadores = [[] for _ in range(amountPlayer)]
        self.fichas = self.crearCombinaciones();
        self.fichasEnJuego = [];
        self.repartirFichas()
        self.jugadorActual = 0
        
        self.IA_duraction = IA_duraction
        self.jugadoresMaquina = jugadoresMaquina;
    
    # MODULO FICHA
    
    def crearCombinaciones(self):

        fichas = []

        for izquierda in range(7):

            for derecha in range(izquierda, 7):
                fichas.append(FichaDomino(izquierda, derecha))

        random.shuffle(fichas)

        return fichas
    
    def repartirFichas(self):

        amountPlayer = len(self.jugadores)

        fichasPorJugador = 7

        for _ in range(fichasPorJugador):
            for jugador in self.jugadores:
                jugador.append(self.fichas.pop())
                
 
    def imprimirFichas(self):

        for i, jugador in enumerate(self.jugadores, start=1):
            print(f"Jugador {i}:{', '.join(map(str, jugador))}");


    # Modulo Juego
    
    def jugadaValida(self, indiceFicha, lado):
        
        if 0 <= indiceFicha < len(self.jugadores[self.jugadorActual]):
            ficha = self.jugadores[self.jugadorActual][indiceFicha]
            return ficha.izquierda == lado or ficha.derecha == lado
        return False

    def jugarFicha(self, indiceFicha, lado):
        
        if not self.PrimeraJugada:
            
           ficha = self.jugadores[self.jugadorActual].pop(indiceFicha);
           self.PrimeraJugada = True; 
           return  ficha;
        #
        
        if self.jugadaValida(indiceFicha, lado):
            ficha = self.jugadores[self.jugadorActual].pop(indiceFicha)
            return ficha
        return None
    

    def siguienteTurno(self):
         self.jugadorActual = (self.jugadorActual + 1) % self.amountPlayer
          
        
    def estadoActual(self):
        estado = f"Jugador actual: {self.jugadorActual + 1}\n"
        estado += "Fichas en juego:\n"
        for i, jugador in enumerate(self.jugadores, start=1):
            estado += f"Jugador {i}: {'|'.join(map(str, jugador))}\n"
        return estado
    
    def evaluarEstado(self, jugador):
        
        # Sumar puntos
        suma = sum(f.izquierda + f.derecha for f in self.jugadores[jugador])
        return suma
        
   
    # Logica de finalizar juego
    
    def is_terminando(self):
        
        for jugador in self.jugadores:
                if len(jugador) == 0:
                    return True, jugador
                
                
        return False, _;
    
    
    # ALGORITMO MINIMAX
    
    def min_max(self, jugador, profundidad, alpha, beta):
        
            if time.time() - self.time_start >= self.max_time:
                raise StopIteration("Out of time!")
        
            if profundidad == 0 or not self.jugadores[jugador]:
                return self.evaluarEstado(jugador), None

            mejor_valor = float('-inf') if jugador == self.jugadorActual else float('inf')
            mejor_jugada = None

            for i, _ in enumerate(self.jugadores[jugador]):
                for lado in [0, 1]:
                    if self.jugadaValida(i, lado):
                        ficha = self.jugadores[jugador].pop(i)
                        valor, _ = self.min_max((jugador + 1) % self.amountPlayer, profundidad - 1, alpha, beta)
                        self.jugadores[jugador].insert(i, ficha)
                        if jugador == self.jugadorActual:
                            if valor > mejor_valor:
                                mejor_valor = valor
                                mejor_jugada = (i, lado)
                            alpha = max(alpha, mejor_valor)
                        else:
                            if valor < mejor_valor:
                                mejor_valor = valor
                                mejor_jugada = (i, lado)
                            beta = min(beta, mejor_valor)

                        if beta <= alpha:
                            break

            return mejor_valor, mejor_jugada

    def siguienteMovimiento(self, max_time):
        
        self.time_start = time.time()
        
        self.max_time = max_time
        
        for depth in range(2, 10000):
             
            try:    
             _, mejor_jugada = self.min_max(self.jugadorActual, profundidad=depth, alpha=float('-inf'), beta=float('inf'))
            except StopIteration:
                break
            
        if mejor_jugada:
            print("La IA eligio" + str(mejor_jugada));
            time.sleep(3);
            i, lado = mejor_jugada
            self.jugarFicha(i, lado)
            self.siguienteTurno()

    def siguienteMovimiento2(self, max_time = 10):
        
        self.time_start = time.time()
        
        self.max_time = max_time
         
        for depth in range(2, 10000):
             
            try:
               _ , mejor_jugada, _ = self.min_max(self.jugadorActual, depth, -np.inf, np.inf)
            except StopIteration:
                break
 
        if mejor_jugada:
            i, lado = mejor_jugada
            self.jugarFicha(i, lado)
            self.siguienteTurno()
            


