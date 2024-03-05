import time
import os
import domino



isValid = True

while (isValid):

    print("\n============== ¿Cuantos jugadores van a jugar? [2-4] ==================== \n")

    try:

        amountPlayer = int(input("Cantidad de jugadores: "))

        # OPCION 0 para cerrar el juego

        if (amountPlayer == 0):
            isValid = False
            print("Juego cancelado")
            break

         # ELEGIR CANTIDAD DE JUGADORES
         
        if (amountPlayer > 4 or amountPlayer < 2):
            
            print("La cantidad de jugadores no es valida  \n");

            time.sleep(2);

            os.system("cls");

            continue
        
        Ia_duracion = int(input("Tiempo Maximo de la IA (Seg): "));
         
        # ELEGIR CUALES JUGADORES SERAN IA
        
        Player_Tipes = input("Selecione quienes sean la computadora (1,2):  ");
        
        players = [ int(player) for player in Player_Tipes.split(',')];
   
        if len(players) == 4 and len(players) > amountPlayer:
            
            print("Todos los jugadores no pueden ser la maquina   \n");
            
            time.sleep(2);
            
            os.system("cls")
            
            continue;
        
        juego =  domino.Domino(amountPlayer, Ia_duracion, players)
                
        # Manejar Turnos del juego
        juegoActivo = True
        
        while juegoActivo:
            
            os.system("cls");
             
            print(f"\nTurno del jugador {juego.jugadorActual + 1}");
                
            # Juega la IA
            
            if juego.jugadorActual + 1 in juego.jugadoresMaquina:
                
                print("La Maquina esta pensado ............")
                            
                juego.siguienteMovimiento(Ia_duracion);
                 
                print(juego.estadoActual())  
            
                continue;
            
            print(juego.estadoActual())       
            
            pasarTurno = int(input('Para pasar turno (selecciona por número): ingrese 1 '));
                
            if pasarTurno == 1:
                    juego.siguienteTurno();
                    continue;   
            
            indiceFicha = int(input('Selecciona la ficha que vas a jugar (selecciona por número): ')) - 1

            lado = int(input('Para jugar el lado izquierdo de la ficha, selecciona 0 y 1 para la derecha: '))

            if juego.jugarFicha(indiceFicha, lado):
                    
                juego.siguienteTurno()
                    
            else:
                print("Esta jugada no es válida, utiliza otro lado o intenta con otra ficha")
                time.sleep(1)   

    except ValueError as error:
        print("El número que ha introdicido no es válido\n")
        time.sleep(1)
        os.system("cls")

