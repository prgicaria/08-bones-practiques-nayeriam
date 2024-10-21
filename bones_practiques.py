#!/usr/bin/env python3

"""
Programa de divisió senzilla
-----------------------------
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

Aquest programa permet a l'usuari introduir dos nombres enters
(dividend i divisor)
i calcular el quocient sencer i el residu.

"""
__author__ = "Nayeri Anglada Monterrubio"
__email__ = "nanglada@instituticaria.cat"
__date__ = "2024/10/14"

# !/usr/bin/env python3

# Programa per calcular el quocient sencer
#  i residu de dos nombres enters

# Entrada de dades: demana al usuari el dividend i divisor
dividend = int(input("Introdueix el dividend (nombre enter): "))
divisor = int(input("Introdueix el divisor (nombre enter): "))

# Comprova que el divisor no sigui zero
if divisor != 0:
    # Càlculs del quocient sencer i residu
    divisio_real = dividend/divisor
    quocient_sencer = dividend // divisor
    residu = dividend % divisor

    # Mostra dels resultats
    print("\n--- Resultats de la divisió ---")
    print(f"Divisió: {dividend}/{divisor}")
    print(f"Quocient: {quocient_sencer}")
    print(f"Residu: {residu}")
else:
    print("\nError: El divisor no pot ser zero.")
