#!/usr/bin/python
import sys
import subprocess

#Definicion de argumentos pasados por consola
if len(sys.argv) > 1:
    argumento = sys.argv[1]
else:
    argumento = False

#Comprobacion de argumentos
if (argumento == "pacman"):
    print("### ACTUZALIDANDO PACMAN")
    subprocess.call(['sudo','pacman', '-Syu'])
    print("### PROCESO DE ACTUZALIZACION DE PACMAN TERMINADO")
    subprocess.call(['sudo','killall','pacman'])

elif (argumento == "yaourt"):
    print("### ACTUZALIDANDO YAOURT")
    subprocess.call(['yaourt', '-Su', '--aur'])
    print("### PROCESO DE ACTUZALIZACION DE YAOURT TERMINADO")

elif (argumento == "clean"):
    print("### LIMPIANDO SISTEMA")
    subprocess.call(['sudo','pacman','-Sc'])
    subprocess.call(['sudo','pacman-optimize'])
    subprocess.call(['sudo','sync'])
    subprocess.call(['sudo','updatedb'])
    print("### PROCESO DE LIMPIANDO SISTEMA TERMINADO")
    subprocess.call(['sudo','killall','pacman'])
    
else:
    print("tiene que utilizar un argumento,(pacman, yaourt, clean)")
