# -*- coding: utf-8 -*-
import os

link = input("Podaj ścieżkę dostępu do pliku: ")

file = open(link, "r").read()
line = file.split("\n")
table = []

for l in line:
    table.append(l)
    
length = len(table)

result = open("Wyniki.txt", "w")
writetable = []

for i in range(0,length):
    for j in range(0, length):
        if table[i] != table[j]:
            print(table[i], "\t", table[j])
            result.write(f"{table[i]}\t{table[j]}\n")
result.close()