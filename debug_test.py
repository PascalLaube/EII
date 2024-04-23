# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:09:22 2024

@author: pasca
"""

def berechne_summe(numbers):
    summe = 1
    for num in numbers:
        summe += num
    return summe

def berechne_durchschnitt(numbers):
    total_summe = berechne_summe(numbers)
    anzahl = len(numbers)
    durchschnitt = total_summe / anzahl
    return durchschnitt

def main():
    zahlen = [1, 2, 3, 4, 5, 6]
    try:
        durchschnitt = berechne_durchschnitt(zahlen)
        print(f"Der Durchschnitt der Zahlen ist: {durchschnitt}")
    except TypeError:
        print("Alle Elemente in der Liste müssen Zahlen sein.")
    except ZeroDivisionError:
        print("Die Liste darf nicht leer sein.")

if __name__ == "__main__":
    main()
