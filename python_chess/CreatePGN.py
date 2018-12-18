#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:39:37 2018

@author: thomascormier
"""

import chess
import chess.pgn

game = chess.pgn.Game()
game.headers["Event"] = "PolyTournoi"
game.headers["Site"] = "Polytech Annecy"
game.headers["Date"] = "18.12.2018"
game.headers["Round"] = "74"
game.headers["White"] = "Evan"
game.headers["Black"] = "Maxence"
game.headers["Result"] = "1/2-1/2"
node = game.add_variation(chess.Move.from_uci("e2e4"))
node = node.add_variation(chess.Move.from_uci("e7e5"))
node.comment = "Amazing move from Evan ! "

print(game)
