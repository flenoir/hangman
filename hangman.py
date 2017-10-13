#!/usr/bin/env python3 
# coding: utf-8

from donnees import *
from functions import *

import random



# on verifie le tableau des noms à trouver
print(word_array)

# on commence le programme
print("Bonjour, bienvenu dans Hangman !")

# On demande le nom du joueur et on l'affiche
player = raw_input("quel est votre nom ? ")
print("ok {}, pret a jouer ? Vous avez 8 tentatives possible".format(player))

# on choisit un numéro au hasard dans la liste de mots à trouver, on renvoi ensuite le mot associé et on le découpe en list
sort_number = random.randint(0,len(word_array)-1)
sorted_word = word_array[sort_number]
splited_sorted_word = list(sorted_word)

# on crée le mot video de 8 lettres à afficher
temp_word = ["_","_","_","_","_","_","_","_",]

# On imprime nos mots pour faciliter le dev

# print(splited_sorted_word)
print(sorted_word)
print(temp_word)


turn = 0

# si la lettre existe dans le mot, on la remplace au bon endroit
def test_keystroke(keystroke,turn):
	for index, item in enumerate(splited_sorted_word):
		if keystroke == item:
			temp_word[index] = keystroke
			print(temp_word)
	turn +=1
	print(turn)
	return turn


if turn < 8:	
	keystroke = raw_input("tapez une lettre ")
	# on teste si la lettre tapée est dans le mot
	test_keystroke(keystroke, turn)

print(turn)
















