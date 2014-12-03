#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 # -*-coding: 850 -*-
 
import random 
import os 
import time
import sys
import copy

s = "a"
#Contadores de Turnos
TurnoP1 = 0
TurnoP2 = 0
#Tableros Globales para los Players
TableroPlayer2 = []
TableroPlayer1 = []

def MusicaInicio():
	try:
		import pygame
		pygame.init()
		pygame.display.set_mode((1,1))
		pygame.mixer.music.load("Inicio.mp3")
		pygame.mixer.music.play()
	except ImportError:
		"No se Encontro Libreria"

#-------------------------------------------------------------------------------------------------------------
#------------------------------- Borra Pantallas -------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
def borra_pantallas():
	os.system(['clear', 'cls'][os.name == 'nt'])

class Juego(object):
	s = "a"

	#Para Impresión de Tableros
	def Imprimir_Tablero(self,s,tablero):
		player = "Jugador"
		if s == "u":
			print " "
		print "El " + player + " y Su Tablero: \n"
		borra_pantallas()
		print """
	\t\t___ ____ ___  _    ____ ____ ____ 
	\t\t |  |__| |__] |    |___ |__/ |  | 
	\t\t |  |  | |__] |___ |___ |  \ |__| 
	                                  
										
	"""
		print " "
		print " "
		#Imprime los Números Horizontales del Tablero
		print " ",
		for i in range(10):
			print "  " + str(i+1) + "  ",
		print "\n"
		for i in range(10):
			#Imprime los Números Verticales del Tablero
			if i != 9: 
				print str(i+1) + "  ",
			else:
				print str(i+1) + " ",
			#Impresión de Separadores
			for j in range(10):
				if tablero[i][j] == -1:
					print ' ',	
				elif s == "u":
					print tablero[i][j],
				elif s == "c":
					if tablero[i][j] == "*" or tablero[i][j] == "$":
						print tablero[i][j],
					else:
						print " ",
				if j != 9:
					print " | ",
			print
			if i != 9:
				print "   ----------------------------------------------------------"
			else: 
				print 

	def Player_Pone_Barcos(self,tablero,barcos):
		for barco in barcos.keys():
			#Validación de Posiciones
			valid = False
			while(not valid):
				print " "
				Playing.Imprimir_Tablero("u",tablero)
				print " "
				print "Se Colocará un/una: " + barco
				print " "
				x,y = Playing.Coordenadas()
				ori = Playing.v_o_h()
				valid = Playing.Validacion(tablero,barcos[barco],x,y,ori)
				borra_pantallas()
				if not valid:
					print "No Puedes Poner un Barco Allí..\nBusque Otra Posición para el Barco."
					raw_input("Pusha Enter Para Continuar")
			#Lugar del Barco
			tablero = Playing.Lugar_Barcos(tablero,barcos[barco],barco[0],ori,x,y)
			Playing.Imprimir_Tablero("u",tablero)
		raw_input("Colocando Barcos....... Pusha Enter para CONTINUAR.")
		print " "
		borra_pantallas()
		print " "
		print """

	\t\t _     _ _____  _____________    ______ _______    ______     _ _____________ ______      ______ _____   ///
	\t\t |_____||     ||_____/|_____|    |     \|______      |  |     ||  ____|_____||_____/     |  ____|     | /// 
	\t\t |     ||_____||    \_|     |    |_____/|______    __|  |_____||_____||     ||    \_.    |_____||_____|...  
	                                                                                                           
		"""
		time.sleep(3)
		return tablero

	def PC_Pone_Barcos(self,tablero,barcos):
		for barco in barcos.keys():
		#Generador de Random Barcos
			valid = False
			while(not valid):
				x = random.randint(1,10)-1
				y = random.randint(1,10)-1
				o = random.randint(0,1)
				if o == 0: 
					ori = "v"
				else:
					ori = "h"
				valid = Playing.Validacion(tablero,barcos[barco],x,y,ori)
			#Lugares
			print " "
			print "La PC Ha Colocado Un: " + barco
			print " "
			tablero = Playing.Lugar_Barcos(tablero,barcos[barco],barco[0],ori,x,y)
		return tablero

	def Lugar_Barcos(self,tablero,barco,s,ori,x,y):
		#Orientación de los Barcos
		if ori == "v":
			for i in range(barco):
				tablero[x+i][y] = s
		elif ori == "h":
			for i in range(barco):
				tablero[x][y+i] = s
		return tablero

	def Validacion(self,tablero,barco,x,y,ori):
	#Validacion the barco can be placed at given coordinates
		if ori.lower() == "v" and x+barco > 10:
			return False
		elif ori.lower() == "h" and y+barco > 10:
			return False
		else:
			if ori == "v":
				for i in range(barco):
					if tablero[x+i][y] != -1:
						return False
			elif ori == "h":
				for i in range(barco):
					if tablero[x][y+i] != -1:
						return False
		return True

	def v_o_h(self):
		#Orientación de los Barcos según Vertical u Horizontal
		while(True):
			print " "
			Entrada_Datos = raw_input("¿En Posición Vertical u Horizotal? (v,h): ")
			if Entrada_Datos == "v" or Entrada_Datos == "h":
				return Entrada_Datos
			else:
				print " "
				print "Respuesta Inválida, Intentelo Nuevamente. (v,h): "
				print " "

	def Coordenadas(self):
		while (True):
			Entrada_Datos = raw_input("Introduce las Coordenadas para tus Barcos(Si ya ingresaste tus Barcos; Ingresa Coordenadas para atacar) (fila,columna): ")
			try:
				coor = Entrada_Datos.split(",")
				if len(coor) != 2:
					raise Exception("Coordenadas Inválidas, Revisa Muy Bien Capitán.");
				coor[0] = int(coor[0])-1
				coor[1] = int(coor[1])-1
				if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
					raise Exception("Coordenadas Inválidas! Use Solamente Valores del 1 al 10.")
				return coor
			except ValueError:
				print "Capitán! Me parece que está Borracho, solo puede con valores Numéricos... Tomese un Descanso mejor."
			except Exception as e:
				print e

	def Mover(self,tablero,x,y):
		if tablero[x][y] == -1:
			return "Fallido"
		elif tablero[x][y] == '*' or tablero[x][y] == '$':
			return "Hazlo De Nuevo"
		else:
			return "¡Yuju Le hemos dado a uno!"

	def Mover_Usuario(self,tablero):
		while(True):
			x,y = Playing.Coordenadas()
			res = Playing.Mover(tablero,x,y)
			if res == "¡Yuju Le hemos dado a uno!":
				print " "
				print "Le Pegamos a uno! Bien Hecho " + str(x+1) + "," + str(y+1)
				Playing.PosicionesMios(tablero,x,y)
				tablero[x][y] = '$'
				if Playing.Ganador(tablero):
					return "Ganar"
			elif res == "Fallido":
				print " "
				print "Ooou., Con estas Coordenadas " + str(x+1) + "," + str(y+1) + " Hemos Fallado. Parece que Tendremos que comprar Anteojos "
				time.sleep(3)
				tablero[x][y] = "*"
			elif res == "Hazlo De Nuevo":
				print " "
				print "Ya Disparamos en Esa Coordenada! . Hazlo De Nuevo"	

			if res != "Hazlo De Nuevo":
				return tablero

	def Mover_PC(self,tablero):
		while(True):
			x = random.randint(1,10)-1
			y = random.randint(1,10)-1
			res = Playing.Mover(tablero,x,y)
			if res == "!Siii!!! Te dí con todo!":
				print " "
				print "Siii.. Te dí! " + str(x+1) + "," + str(y+1)
				time.sleep(3)
				Playing.PosicionesMios(tablero,x,y)
				tablero[x][y] = '$'
				if Playing.Ganador(tablero):
					return "Ganar"
			elif res == "Fallido":
				print " "
				print "Jajajaj con Esta Coordenada, " + str(x+1) + "," + str(y+1) + " Has Fallado!."
				tablero[x][y] = "*"
			if res != "Hazlo De Nuevo":
				return tablero
		
	def PosicionesMios(self,tablero,x,y):
		if tablero[x][y] == "A":
			barco = "Titanic"
		elif tablero[x][y] == "B":
			barco = "Yates"
		elif tablero[x][y] == "S":
			barco = "Buques" 
		elif tablero[x][y] == "D":
			barco = "Lanchas"

			
	def Ganador(self,tablero):
		for i in range(10):
			for j in range(10):
				if tablero[i][j] != -1 and tablero[i][j] != '*' and tablero[i][j] != '$':
					return False
		return True

	def main(self):
	#Tipos de Barcos
		barcos = {"Titanic":5,
				 "Yates":4,
				 "Buques":3,
				 "Lanchas":3}
		tablero = []
		for i in range(10):
			tablero_fila = []
			for j in range(10):
				tablero_fila.append(-1)
			tablero.append(tablero_fila)
		#Tableros de Usuario y PC
		tablero_usuario = copy.deepcopy(tablero)
		tablero_pc = copy.deepcopy(tablero)
		#Agregar elementos a Tableros
		tablero_usuario.append(copy.deepcopy(barcos))
		tablero_pc.append(copy.deepcopy(barcos))
		#Colocación de Barcos
		tablero_usuario = Playing.Player_Pone_Barcos(tablero_usuario,barcos)
		tablero_pc = Playing.PC_Pone_Barcos(tablero_pc,barcos)
		#Loop para Tableros
		while(1):
			Playing.Imprimir_Tablero("c",tablero_pc)
			tablero_pc = Playing.Mover_Usuario(tablero_pc)
			if tablero_pc == "Ganar":
				print " "
				print "Hemos Ganado la Batalla! :)"
				quit()
			time.sleep(1)
			Playing.Imprimir_Tablero("c",tablero_pc)
			raw_input("Nuestro Turno ha Terminado, Es Turno de la PC. Pusha Enter para CONTINUAR.")
			print " "
			borra_pantallas()
			print """
	____  ______  _____   ___ ____   _   ____   ___ ____ 
	 | |  ||__/|\ ||  |   |  \|___   |   |__|   |__]|   .
	 | |__||  \| \||__|   |__/|___   |___|  |   |   |___.
	                                                     
			La PC está Calculando en donde Tirar. Cuidado te Dá en uno xD                                                            
				"""
			time.sleep(2)
			#Movimiento de la PC
			tablero_usuario = Playing.Mover_PC(tablero_usuario)
			#Checar si la PC gana
			if tablero_usuario == "Ganar":
				print " "
				print "Bien Hecho... Al Parecer tu vas a comandar la Marina de los Estados Unidos para la 3ra Guerra Mundial"
				print " "
				print "Regrasando al Menú Principal..."
				time.sleep(3)
				Menu()
				quit()
			Playing.Imprimir_Tablero("u",tablero_usuario)
			raw_input("Estas son Nuestras Posiciones!. Pusha Enter para CONTINUAR.")

	 
	#-----------------------------------------------------------------------------------------------------------------------------------
	#------------------------------------------------------------- PLAYER 1 ------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------


	#Para Impresión de Tableros
	def PrintableroP1(self,s,TableroPlayer1):
		player = "Player 1"
		if s == "u":
			print " "                           
		print """
	__________ _   ____________   ___ _   _____   _________   _  __  _____ 
	 | |__||__]|   |___|__/|  |   |__]|   |__| \_/ |___|__/   |  ||\ ||  |.
	 | |  ||__]|___|___|  \|__|   |   |___|  |  |  |___|  \   |__|| \||__|.

	"""
		print " "
		print "Este es el Tablero del Player 1: \n"
		print " "
		#Imprime los Números Horizontales del TableroPlayer1
		print " ",
		for i in range(10):
			print "  " + str(i+1) + "  ",
		print "\n"
		for i in range(10):
			#Imprime los Números Verticales del TableroPlayer1
			if i != 9: 
				print str(i+1) + "  ",
			else:
				print str(i+1) + " ",
			#Impresión de Separadores
			for j in range(10):
				if TableroPlayer1[i][j] == -1:
					print ' ',  
				elif s == "u":
					print TableroPlayer1[i][j],
				elif s == "c":
					if TableroPlayer1[i][j] == "*" or TableroPlayer1[i][j] == "$":
						print TableroPlayer1[i][j],
					else:
						print " ",
				if j != 9:
					print " | ",
			print
			#print a horizontal line
			if i != 9:
				print "   ----------------------------------------------------------"
			else: 
				print 

	def Player_Pone_BarcosPlayer1(self,TableroPlayer1,BarcosPlayer1):
		for barco in BarcosPlayer1.keys():
			#Validación de Posiciones
			valid = False
			while(not valid):
				print " "
				Playing.PrintableroP1("u",TableroPlayer1)
				print " "
				print "Se Colocará un/una: " + barco
				print " "
				x,y = Playing.CoordenadasPlayer1()
				ori = Playing.v_o_h()
				valid = Playing.ValidacionPlayer1(TableroPlayer1,BarcosPlayer1[barco],x,y,ori)
				borra_pantallas()
				if not valid:
					print "No Puedes Poner un Barco Allí..\nBusque Otra Posición para el Barco."
					raw_input("Pusha Enter Para Continuar")
			#Lugar del Barco
			Playing.TableroPlayer1 = Playing.Lugar_BarcosPlayer1(TableroPlayer1,BarcosPlayer1[barco],barco[0],ori,x,y)
			Playing.PrintableroP1("u",TableroPlayer1)
		raw_input("Colocando Barcos Player1....... Pusha Enter para CONTINUAR.")
		Playing.JcjPlayer2(TableroPlayer1,TableroPlayer2)
		print " "
		borra_pantallas()
		borra_pantallas()
		borra_pantallas()
		borra_pantallas()

		print " "
		print """

	\t\t _     _ _____  _____________    ______ _______    ______     _ _____________ ______      ______ _____   ///
	\t\t |_____||     ||_____/|_____|    |     \|______      |  |     ||  ____|_____||_____/     |  ____|     | /// 
	\t\t |     ||_____||    \_|     |    |_____/|______    __|  |_____||_____||     ||    \_.    |_____||_____|...  

		"""
		time.sleep(3)
		return Playing.TableroPlayer1

	def Lugar_BarcosPlayer1(self,TableroPlayer1,barco,s,ori,x,y):
		#Orientación de los BarcosPlayer1
		if ori == "v":
			for i in range(barco):
				TableroPlayer1[x+i][y] = s
		elif ori == "h":
			for i in range(barco):
				TableroPlayer1[x][y+i] = s
		return TableroPlayer1

	def ValidacionPlayer1(self,TableroPlayer1,barco,x,y,ori):
	#ValidacionPlayer1 the barco can be placed at given coordinates
		if ori.lower() == "v" and x+barco > 10:
			return False
		elif ori.lower() == "h" and y+barco > 10:
			return False
		else:
			if ori == "v":
				for i in range(barco):
					if TableroPlayer1[x+i][y] != -1:
						return False
			elif ori == "h":
				for i in range(barco):
					if TableroPlayer1[x][y+i] != -1:
						return False
		return True

	def v_o_h(self):
		#Orientación de los BarcosPlayer1 según Vertical u Horizontal
		while(True):
			print " "
			Entrada_Datos = raw_input("¿En Posición Vertical u Horizotal? (v,h): ")
			if Entrada_Datos == "v" or Entrada_Datos == "h":
				return Entrada_Datos
			else:
				print " "
				print "Respuesta Inválida, Intentelo Nuevamente. (v,h): "
				print " "

	def CoordenadasPlayer1(self):
		while (True):
			Entrada_Datos = raw_input("Player 1 (Si ya ingresaste tus Barcos; Ingresa Coordenadas para atacar al Player 2) (fila,columna): ")
			try:
				coor = Entrada_Datos.split(",")
				if len(coor) != 2:
					raise Exception("Coordenadas Player1 Inválidas, Revisa Muy Bien Capitán.");
				coor[0] = int(coor[0])-1
				coor[1] = int(coor[1])-1
				if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
					raise Exception("Coordenadas Player1 Inválidas! Use Solamente Valores del 1 al 10.")
				return coor
			except ValueError:
				print "Capitán! Me parece que está Borracho, solo puede con valores Numéricos... Tomese un Descanso mejor."
			except Exception as e:
				print e

	def MoverP1(self,TableroPlayer1,x,y):
		if TableroPlayer1[x][y] == -1:
			return "Fallido"
		elif TableroPlayer1[x][y] == '*' or TableroPlayer1[x][y] == '$':
			return "Hazlo De Nuevo"
		else:
			return "¡Yuju Le hemos dado a uno!"

	def MoverPlayer1(self,TableroPlayer1):
		while(True):
			x,y = Playing.CoordenadasPlayer1()
			res = Playing.MoverP1(TableroPlayer1,x,y)
			if res == "¡Yuju Le hemos dado a uno!":
				print " "
				print "Le Pegamos a uno! Bien Hecho " + str(x+1) + "," + str(y+1)
				Playing.PosicionesPlayer1(TableroPlayer1,x,y)
				TableroPlayer1[x][y] = '$'
				if Playing.GanadorPlayer1(TableroPlayer1):
					return "Ganar"
			elif res == "Fallido":
				print " "
				print "Ooou., " + str(x+1) + "," + str(y+1) + "Hemos Fallado. Parece que Tendremos que comprar Anteojos"
				time.sleep(3)
				TableroPlayer1[x][y] = "*"
			elif res == "Hazlo De Nuevo":
				print " "
				print "Ya Disparamos en Esa Coordenada! . Hazlo De Nuevo"   

			if res != "Hazlo De Nuevo":
				return TableroPlayer1

	def PosicionesPlayer1(self,TableroPlayer1,x,y):
		if TableroPlayer1[x][y] == "A":
			barco = "Titanic"
		elif TableroPlayer1[x][y] == "B":
			barco = "Yates"
		elif TableroPlayer1[x][y] == "S":
			barco = "Buques" 
		elif TableroPlayer1[x][y] == "D":
			barco = "Lanchas"

	def GanadorPlayer1(self,TableroPlayer1):
		for i in range(10):
			for j in range(10):
				if TableroPlayer1[i][j] != -1 and TableroPlayer1[i][j] != '*' and TableroPlayer1[i][j] != '$':
					return False
		return True

	def JcJPlayer1(self,TableroPlayer2):
		#Tipos de BarcosPlayer1
		BarcosPlayer1 = {"Titanic":5,
				 "Yates":4,
				 "Buques":3,
				 "Lanchas":3}
		TableroPlayer1 = []
		for i in range(10):
			tablero_fila = []
			for j in range(10):
				tablero_fila.append(-1)
			TableroPlayer1.append(tablero_fila)
		#Tableros de Usuario y PC
		MostTablePlayer1 = copy.deepcopy(TableroPlayer1)
		#Agregar elementos a Tableros
		MostTablePlayer1.append(copy.deepcopy(BarcosPlayer1))
		#Colocación de BarcosPlayer1
		MostTablePlayer1 = Playing.Player_Pone_BarcosPlayer1(MostTablePlayer1,BarcosPlayer1)
		#Loop para Tableros
		while(1):
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			#PrintableroP1("u",MostTablePlayer1)
			#PrintableroP2("c",TableroPlayer2)
			TableroPlayer2 = Playing.MoverPlayer1(TableroPlayer2)
			if TableroPlayer2 == "Ganar":
				print " "
				print "Hemos Ganado la Batalla! :)"
				quit()
			time.sleep(1)
			#PrintableroP2("c",MostTablePlayer2)
			raw_input("Nuestro Turno ha Terminado, Es Turno del Player 2. Pusha Enter para CONTINUAR.")
			print " "
			borra_pantallas()
			print """
	__________ _   ____________   ___ _   _____   _________   ___ ________ 
	 | |__||__]|   |___|__/|  |   |__]|   |__| \_/ |___|__/   |  \|  |[__ .
	 | |  ||__]|___|___|  \|__|   |   |___|  |  |  |___|  \   |__/|__|___].
																			 
				"""
			time.sleep(1)
			#Movimiento de la PC
			#MostTablePlayer1 = MoverPlayer2(MostTablePlayer1)
			#Checar si la PC gana
			if MostTablePlayer1 == "Ganar":
				print " "
				print "Bien Hecho... Al Parecer tu vas a comandar la Marina de los Estados Unidos para la 3ra Guerra Mundial"
				print "Player 1: Mandaste a vender chicles a la Flota del Player 2."
				print " "
				print "Regrasando al Menú Principal..."
				time.sleep(3)
				Menu()
				quit()
			raw_input("Estas son Nuestras Posiciones!. Pusha Enter para CONTINUAR.")

	#-----------------------------------------------------------------------------------------------------------------------------------
	#------------------------------------------------------------- PLAYER 2 ------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------

	#Para Impresión de Tableros
	def PrintableroP2(self,s,TableroPlayer2):
		player = "Player2"
		if s == "u":
			print " "
		print """
	__________ _   ____________   ___ _   _____   _________   ___ ________ 
	 | |__||__]|   |___|__/|  |   |__]|   |__| \_/ |___|__/   |  \|  |[__ .
	 | |  ||__]|___|___|  \|__|   |   |___|  |  |  |___|  \   |__/|__|___].
	                                                                       
	"""
		print " "
		print "Este es el Tablero del Player 2: \n"
		print " "
		#Imprime los Números Horizontales del TableroPlayer2
		print " ",
		for i in range(10):
			print "  " + str(i+1) + "  ",
		print "\n"
		for i in range(10):
			#Imprime los Números Verticales del TableroPlayer2
			if i != 9: 
				print str(i+1) + "  ",
			else:
				print str(i+1) + " ",
			#Impresión de Separadores
			for j in range(10):
				if TableroPlayer2[i][j] == -1:
					print ' ',  
				elif s == "u":
					print TableroPlayer2[i][j],
				elif s == "c":
					if TableroPlayer2[i][j] == "*" or TableroPlayer2[i][j] == "$":
						print TableroPlayer2[i][j],
					else:
						print " ",
				if j != 9:
					print " | ",
			print
			#print a horizontal line
			if i != 9:
				print "   ----------------------------------------------------------"
			else: 
				print 

	def Player_Pone_BarcosPlayer2(self,TableroPlayer2,BarcosPlayer2):
		for barco in BarcosPlayer2.keys():
			#Validación de Posiciones
			valid = False
			while(not valid):
				print " "
				Playing.PrintableroP2("u",TableroPlayer2)
				print " "
				print "Se Colocará un/una: " + barco
				print " "
				x,y = Playing.CoordenadasPlayer2()
				ori = Playing.v_o_h()
				valid = Playing.ValidacionPlayer2(TableroPlayer2,BarcosPlayer2[barco],x,y,ori)
				borra_pantallas()
				if not valid:
					print "No Puedes Poner un Barco Allí..\nBusque Otra Posición para el Barco."
					raw_input("Pusha Enter Para Continuar")
			#Lugar del Barco
			Playing.TableroPlayer2 = Playing.Lugar_BarcosPlayer2(TableroPlayer2,BarcosPlayer2[barco],barco[0],ori,x,y)
			Playing.PrintableroP2("u",TableroPlayer2)
		raw_input("Colocando Barcos Player2....... Pusha Enter para CONTINUAR.")
		print " "
		borra_pantallas()
		borra_pantallas()
		borra_pantallas()
		borra_pantallas()
		print " "
		print """

	\t\t _     _ _____  _____________    ______ _______    ______     _ _____________ ______      ______ _____   ///
	\t\t |_____||     ||_____/|_____|    |     \|______      |  |     ||  ____|_____||_____/     |  ____|     | /// 
	\t\t |     ||_____||    \_|     |    |_____/|______    __|  |_____||_____||     ||    \_.    |_____||_____|... 

		"""
		time.sleep(1)
		return TableroPlayer2

	def Lugar_BarcosPlayer2(self,TableroPlayer2,barco,s,ori,x,y):
		#Orientación de los BarcosPlayer2
		if ori == "v":
			for i in range(barco):
				TableroPlayer2[x+i][y] = s
		elif ori == "h":
			for i in range(barco):
				TableroPlayer2[x][y+i] = s
		return TableroPlayer2

	def ValidacionPlayer2(self,TableroPlayer2,barco,x,y,ori):
		#ValidacionPlayer2 the barco can be placed at given coordinates
		if ori.lower() == "v" and x+barco > 10:
			return False
		elif ori.lower() == "h" and y+barco > 10:
			return False
		else:
			if ori == "v":
				for i in range(barco):
					if TableroPlayer2[x+i][y] != -1:
						return False
			elif ori == "h":
				for i in range(barco):
					if TableroPlayer2[x][y+i] != -1:
						return False
		return True

	def CoordenadasPlayer2(self):
		while (True):
			Entrada_Datos = raw_input("Player 2 (Si ya ingresaste tus Barcos; Ingresa Coordenadas para atacar al Player 1) (fila,columna): ")
			try:
				coor = Entrada_Datos.split(",")
				if len(coor) != 2:
					raise Exception("CoordenadasPlayer2 Inválidas, Revisa Muy Bien Capitán.");
				coor[0] = int(coor[0])-1
				coor[1] = int(coor[1])-1
				if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
					raise Exception("CoordenadasPlayer2 Inválidas! Use Solamente Valores del 1 al 10.")
				return coor
			except ValueError:
				print "Capitán! Me parece que está Borracho, solo puede con valores Numéricos... Tomese un Descanso mejor."
			except Exception as e:
				print e

	def MoverP2(self,TableroPlayer2,x,y):
		if TableroPlayer2[x][y] == -1:
			return "Fallido"
		elif TableroPlayer2[x][y] == '*' or TableroPlayer2[x][y] == '$':
			return "Hazlo De Nuevo"
		else:
			return "¡Yuju Le hemos dado a uno!"

	def MoverPlayer2(self,TableroPlayer2):
		while(True):
			x,y = Playing.CoordenadasPlayer2()
			res = Playing.MoverP2(TableroPlayer2,x,y)
			if res == "¡Yuju Le hemos dado a uno!":
				print " "
				print "Le Pegamos a uno! Bien Hecho " + str(x+1) + "," + str(y+1)
				Playing.PosicionesPlayer2(TableroPlayer2,x,y)
				TableroPlayer2[x][y] = '$'
				if Playing.GanadorPlayer2(TableroPlayer2):
					return "Ganar"
			elif res == "Fallido":
				print " "
				print "Ooou., " + str(x+1) + "," + str(y+1) + "Hemos Fallado. Parece que Tendremos que comprar Anteojos"
				time.sleep(3)
				TableroPlayer2[x][y] = "*"
			elif res == "Hazlo De Nuevo":
				print " "
				print "Ya Disparamos en Esa Coordenada! . Hazlo De Nuevo"   

			if res != "Hazlo De Nuevo":
				return TableroPlayer2

	def PosicionesPlayer2(self,TableroPlayer2,x,y):
		if TableroPlayer2[x][y] == "A":
			barco = "Titanic"
		elif TableroPlayer2[x][y] == "B":
			barco = "Yates"
		elif TableroPlayer2[x][y] == "S":
			barco = "Buques" 
		elif TableroPlayer2[x][y] == "D":
			barco = "Lanchas"

	def GanadorPlayer2(self,TableroPlayer2):
		for i in range(10):
			for j in range(10):
				if TableroPlayer2[i][j] != -1 and TableroPlayer2[i][j] != '*' and TableroPlayer2[i][j] != '$':
					return False
		return True

	def JcjPlayer2(self,TableroPlayer1,TableroPlayer2):
	#Tipos de BarcosPlayer2
		BarcosPlayer2 = {"Titanic":5,
				 "Yates":4,
				 "Buques":3,
				 "Lanchas":3}
		TableroPlayer2=[]
		for i in range(10):
			tablero_fila = []
			for j in range(10):
				tablero_fila.append(-1)
			TableroPlayer2.append(tablero_fila)
		#Tableros de Usuario y PC
		MostTablePlayer2 = copy.deepcopy(TableroPlayer2)
		#Agregar elementos a Tableros
		MostTablePlayer2.append(copy.deepcopy(BarcosPlayer2))
		#Colocación de BarcosPlayer2
		MostTablePlayer2 = Playing.Player_Pone_BarcosPlayer2(MostTablePlayer2,BarcosPlayer2)
		#Loop para Tableros
		while(1):
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			Playing.PrintableroP2("u",MostTablePlayer2)
			Playing.PrintableroP1("c",TableroPlayer1)
			TableroPlayerMostrar = Playing.MoverPlayer2(TableroPlayer1)
			if TableroPlayerMostrar == "Ganar":
				print " "
				print "Hemos Ganado la Batalla! :)"
				quit()
			time.sleep(1)
			borra_pantallas()
			borra_pantallas()
			Playing.PrintableroP2("u",MostTablePlayer2)
			Playing.PrintableroP1("c",TableroPlayer1)
			raw_input("Nuestro Turno ha Terminado, Es Turno del Player 1. Pusha Enter para CONTINUAR.")
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			print """
	____  ______  _____   ___ _____      ___ _   _____   _________   _  __  _____ 
	 | |  ||__/|\ ||  |   |  \|___|      |__]|   |__| \_/ |___|__/   |  ||\ ||  |.
	 | |__||  \| \||__|   |__/|___|___   |   |___|  |  |  |___|  \   |__|| \||__|.
	                                                                                                               
				"""
			time.sleep(1)
			#Muestra mi tablero como Player 1 (Falta mostrar las po)
			Playing.PrintableroP1("u",TableroPlayer1)
			#Muestra el tablero del contendiente Player 2
			Playing.PrintableroP2("c",MostTablePlayer2)
			#PrintableroP2("u",TableroPlayer2)
			MostTablePlayer2 = Playing.MoverPlayer1(MostTablePlayer2)
			#Checar si la PC gana
			if MostTablePlayer2 == "Ganar":
				print " "
				print "Bien Hecho... Al Parecer tu vas a comandar la Marina de los Estados Unidos para la 3ra Guerra Mundial"
				print "Player 2: Mandaste a vender chicles a la Flota del Player 1."
				print " "
				print "Regrasando al Menú Principal..."
				time.sleep(3)
				Menu()
				quit()
			time.sleep(1)
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			borra_pantallas()
			time.sleep(1)
			Playing.PrintableroP1("u",TableroPlayer1)
			Playing.PrintableroP2("c",MostTablePlayer2)
			raw_input("Nuestro Turno ha Terminado, Es Turno del Player 2. Pusha Enter para CONTINUAR.")

	#-----------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------- MENU --------------------------------------------------------------
	#-----------------------------------------------------------------------------------------------------------------------------------

	def Cargando(self):
		MusicaInicio()
		borra_pantallas()
		print "                ──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌                   ──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌ "
		print "\t\t───▄▄██▌█ Cargando. BATALLA 			   ───▄▄██▌█ Metralladoras,	"
		print "\t\t▄▄▄▌▐██▌█ 		NAVAL...                   ▄▄▄▌▐██▌█ 		Municiones "
		print "\t\t███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌	           ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌	"
		print "\t\t▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀(@)▀                 ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀(@)▀   Transportando Cargamento al Barco........"
		print " "
		time.sleep(2)
		borra_pantallas()
		print "El Cargamento fué Transportando sin ningún problema al Barco..."
		time.sleep(1)
		print " "
		Playing.Menu()
	#-------------------------------------------------------------------------------
	#--------------------------------- Menú Principal ------------------------------
	#-------------------------------------------------------------------------------
	def Menu(self):
		borra_pantallas()
		print " "
		print " "
		print " "
		for x in range(0,5):
			print " "
			print " "
			print " "
			print " "
			print " "
			print " "
			print " "
			print " "
			print """
	\t\t\t\t888888b.   d8b                                              d8b      888          
	\t\t\t\t888  "88b  Y8P                                              Y8P      888          
	\t\t\t\t888  .88P                                                            888          
	\t\t\t\t8888888K.  888  .d88b.  88888b.  888  888  .d88b.  88888b.  888  .d88888  .d88b.  
	\t\t\t\t888  "Y88b 888 d8P  Y8b 888 "88b 888  888 d8P  Y8b 888 "88b 888 d88" 888 d88""88b 
	\t\t\t\t888    888 888 88888888 888  888 Y88  88P 88888888 888  888 888 888  888 888  888 
	\t\t\t\t888   d88P 888 Y8b.     888  888  Y8bd8P  Y8b.     888  888 888 Y88b 888 Y88..88P 
	\t\t\t\t8888888P"  888  "Y8888  888  888   Y88P    "Y8888  888  888 888  "Y88888  "Y88P"  
																					"""
			print " "
			print """
	\t\t\t\t\t   __        ___    __   _____ _____  _     ____  __   _     _   ___  
	\t\t\t\t\t  / /\      | |_)  / /\   | |   | |  | |   | |_  ( (` | |_| | | | |_) 
	\t\t\t\t\t /_/--\     |_|_) /_/--\  |_|   |_|  |_|__ |_|__ _)_) |_| | |_| |_|  """
			time.sleep(0.5)
			borra_pantallas()
			time.sleep(0.5)
		while True:
			try:
				print " "
				print " "
				print " "
				print " "
				print """
	\t\t\t\t888888b.   d8b                                              d8b      888          
	\t\t\t\t888  "88b  Y8P                                              Y8P      888          
	\t\t\t\t888  .88P                                                            888          
	\t\t\t\t8888888K.  888  .d88b.  88888b.  888  888  .d88b.  88888b.  888  .d88888  .d88b.  
	\t\t\t\t888  "Y88b 888 d8P  Y8b 888 "88b 888  888 d8P  Y8b 888 "88b 888 d88" 888 d88""88b 
	\t\t\t\t888    888 888 88888888 888  888 Y88  88P 88888888 888  888 888 888  888 888  888 
	\t\t\t\t888   d88P 888 Y8b.     888  888  Y8bd8P  Y8b.     888  888 888 Y88b 888 Y88..88P 
	\t\t\t\t8888888P"  888  "Y8888  888  888   Y88P    "Y8888  888  888 888  "Y88888  "Y88P"  
																							"""
				print " "
				print """
	\t\t\t\t\t   __        ___    __   _____ _____  _     ____  __   _     _   ___  
	\t\t\t\t\t  / /\      | |_)  / /\   | |   | |  | |   | |_  ( (` | |_| | | | |_) 
	\t\t\t\t\t /_/--\     |_|_) /_/--\  |_|   |_|  |_|__ |_|__ _)_) |_| | |_| |_|  """
				
				print " "
				print "\t***************************************************************************************************************** "
				print "\t* Pon a prueba tus habilidades en este juego. Enbarcate y supera toda clase de retos que encuentres en el mismo.*"
				print "\t*                                                                                                               *"
				print "\t* Elige una opción de juego. (Sólo puedes ingresar números)                                                     *"
				print "\t*****************************************************************************************************************"
				print " "
				tablero=[]
				tablero2=[]
				tablero_pc=[]
				tableroo_culto=[]
				print "1. Instrucciones Generales"
				print "2. Entrar y Jugar"
				print "3. Créditos"
				print " "
				print "4. Salir"
				print " "
		#-----------------------------------------------------------------------------------------------------------------------------------
		#--------------------------------------------------- OPCIONES MENÚ PRINCIPAL DEL JUEGO ---------------------------------------------
		#-----------------------------------------------------------------------------------------------------------------------------------        
				opmenu = input("Ingrese Número de Opción: ")
				if opmenu == 1:
					borra_pantallas()
					print " "
					print "Cargando Instrucciones Generales..."
					time.sleep(1)
					Playing.instrucciones()
				if opmenu == 2:
					borra_pantallas()
					print " "
					print "Cargando Juego..."
					time.sleep(4)
					borra_pantallas()
					s = True
					while s==True:
						try:
							print """
				\t\t           ___  ___  ___      ___  __    __           __  ___   ___   
				\t\t  /\/\    /___\/   \/___\    /   \/__\   \ \  /\ /\  /__\/ _ \ /___\_ 
				\t\t /    \  //  // /\ //  //   / /\ /_\      \ \/ / \ \/_\ / /_\///  /(_)
				\t\t/ /\/\ \/ \_// /_// \_//   / /_///__   /\_/ /\ \_/ //__/ /_\\/ \_// _ 
				\t\t\/    \/\___/___,'\___/   /___,'\__/   \___/  \___/\__/\____/\___/ (_)

							"""
							print ""
							print "\t1. Un Jugador"
							print "\t2. Dos Jugadores"
							print "\t3. Regresar al Menú Principal "
							print " "
							p = input("\t¿Que Opción elige?: ")
							if p==1:
								borra_pantallas()
								print " "
								print "Cargando Juego........................"
								time.sleep(2)
								Playing.main()
							elif p==2:
								borra_pantallas()
								Playing.JcJPlayer1(TableroPlayer2)
							elif p==3:
								Playing.Menu()
							else:
								borra_pantallas()
								print "Opción No Válida. Vuelva a Intentarlo"
						except (SyntaxError,TypeError,NameError,ValueError):
							borra_pantallas()
							print " "
							print "Eso no es válido Intentalo Nuevamente"
							print " "	
					break
				if opmenu == 3:
					borra_pantallas()
					print " "
					print "Cargando Créditos..."
					time.sleep(1)
					Playing.Creditos()
				if opmenu == 4:
					borra_pantallas()
					print " "
					print "Saliendo del Juego..."
					print """
		▒▒▒▒▒▒▓   
		▒▒▒▒▒▒▒▓
		▒▒▒▒▒▒▒▓▓▓
		▒▓▓▓▓▓▓░░░▓
		▒▓░░░░▓░░░░▓
		▓░░░░░░▓░▓░▓
		▓░░░░░░▓░░░▓
		▓░░▓░░░▓▓▓▓
		▒▓░░░░▓▒▒▒▒▓    Visitame en mi Bello y Sensual Facebook: www.Facebook.com/Bettogc
		▒▒▓▓▓▓▒▒▒▒▒▓
		▒▒▒▒▒▒▒▒▓▓▓▓    Y en mi Famoso y Codisiado Twitter: 
		▒▒▒▒▒▓▓▓▒▒▒▒▓
		▒▒▒▒▓▒▒▒▒▒▒▒▒▓
		▒▒▒▓▒▒▒▒▒▒▒▒▒▓
		▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓
		▒▓▒▓▒▒▒▒▒▒▒▒▒▓
		▒▓▒▓▓▓▓▓▓▓▓▓▓
		▒▓▒▒▒▒▒▒▒▓
		▒▒▓▒▒▒▒ """

					time.sleep(4)
					borra_pantallas()
					sys.exit()
				else:
					borra_pantallas()
					print " "
					print "Eso no es válido"
					print " "
			except (SyntaxError,TypeError,NameError,ValueError):
				borra_pantallas()
				print " "
				print "Eso no es válido"
				print " "
	#-------------------------------------------------------------------------------
	#----------------------------- Instrucciones Generales---------------------------
	#-------------------------------------------------------------------------------
	def instrucciones(self):
		borra_pantallas()
		ins = True
		while ins==True:
			try:
				print """                                                                                                                                           
				  
			\t\t _____ __   _ _______ _______  ______ _     _ _______ _______ _____  _____  __   _ _______ _______
			\t\t   |   | \  | |______    |    |_____/ |     | |       |         |   |     | | \  | |______ |______
			\t\t __|__ |  \_| ______|    |    |    \_ |_____| |_____  |_____  __|__ |_____| |  \_| |______ ______|
																											  


																											   """
				print " "
				print "BATALLA NAVAL o bien conocido en inglés como BATTLE SHIPS, se compone de dos tableros por jugador, dividido cada uno en cuadrículas. Los tableros típicos son cuadrados de 10 por 10 casillas, y cada posición se identifica con números para las columnas y las filas (de 1 a 10). En uno de los tableros el jugador coloca sus barcos y registra los tiros del oponente. En el otro, se registran los tiros propios. "
				print " "
				print "Antes de comenzar, cada jugador posiciona los barcos de forma secreta o invisible al oponente, generalmente con el tablero en posición vertical como pizarra. Cada uno ocupa, según su modelo, una cierta cantidad de posiciones, ya sea horizontal o verticalmente. De esta forma, no se permiten lugares solapados, ya que cada uno ocupa posiciones únicas. Ambos participantes poseen y deben ubicar igual número de naves. "
				print " "
				print "Una vez todas las naves han sido posicionadas, se inicia una serie de rondas. En cada ronda, cada jugador en su turno indica una posición del tablero de su oponente. Si esa posición es ocupada por una parte de un barco, el oponente indica averiado (toque o tocado) y el atacante marca con rojo esa posición, con un pin. Cuando todas las posiciones de un mismo barco han sido dañadas debe indicarse hundido dando a conocer tal circunstancia que indicará al atacante la importancia de la nave destruida. Ahora bien, si la posición indicada, efectivamente, no posee un barco alojado, se indica con agua, y será marcada con un pin blanco."
				print " "
				print "Quien destruya primero todas las naves será el vencedor y podrá tomar el tesoro de la Isla Errante."
				print " "
				print "1. Menú"
				print " "
				preg=input("Ingrese la Opción a la que desea acceder: ")
				print " "
				if preg ==1:
					print " "
					print "Regresando al Menú Principal..."
					print " "
					time.sleep(1)
					borra_pantallas()
					Playing.Menu()
				else:
					borra_pantallas()
					print "Respuesta Inválida Intentalo Nuevamente"
			except (SyntaxError,TypeError,NameError,ValueError):
				borra_pantallas()
				print " "
				print "¿A?, Eso no es válido Intentalo Nuevamente "
				print " "

	#-------------------------------------------------------------------------------
	#------------------------------ Creditos del Juego -----------------------------
	#-------------------------------------------------------------------------------
	def Creditos(self):
		print " "
		ins = True
		while ins==True:
			try:
				print "\t\t\t\t\t\t========================================================"
				print "\t\t\t\t\t\t=                                                      ="
				print "\t\t\t\t\t\t=\t\t     Batalla Naval                                ="								  
				print "\t\t\t\t\t\t=                                                      =    *"
				print "\t\t\t\t\t\t=\t\tVersión 1.1 Star 2014                             ="
				print "\t\t\t\t\t\t=                                                      =    *"
				print "\t\t\t\t\t\t=\t\t   By: Erick (Betto)                              ="
				print "\t\t\t\t\t\t=                                                      ="
				print "\t\t\t\t\t\t========================================================"
				print "1. Regresar Al Menú Principal"
				print " "
				preg=input("Ingrese la Opción a la que desea acceder: ")
				if preg ==1:
					print "Regresando al Menú Principal..."
					print " "
					time.sleep(1)
					borra_pantallas()
					Playing.Menu()
				else:
					borra_pantallas()
					print "Respuesta Inválida"
			except (SyntaxError,TypeError,NameError,ValueError):
				borra_pantallas()
				print " "
				print "Eso no es válido Intentalo Nuevamente"
				print " "
Playing = Juego()
#Playing.Cargando()
Playing.Cargando()