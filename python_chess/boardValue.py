#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:10:03 2018

@author: thomascormier
"""



import chess

def boardValue(board):
    """
    Fonction qui renvoie la valeur du board. 
    Cette valeur est d'autant positif qu'elle est favorable aux blancs et reciproquement.
    Paramatres :
        -board : le board actuel (qui contient le tour a jouer)
    Retourne :
        -int(value)
    """
    value=0
    chaine = board.fen()
    for i, char in enumerate(chaine):
        print (i, char)
        print("value : ",value)
        if char == 'q' :
            value += 8.8
        if char == 'r' : 
            value += 5.1
        if char == 'b' :
            value += 3.33
        if char == 'n' :
            value += 3.2
        if char == 'p' :
            value += 1 
        if char == 'Q' :
            value -= 8.8
        if char == 'R' : 
            value -= 5.1
        if char == 'B' :
            value -= 3.33
        if char == 'N' :
            value -= 3.2
        if char == 'P' :
            value -= 1 
        if char == ' ' : 
            break
    return round(value,3)
    



board1 = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")


print (boardValue(board1))