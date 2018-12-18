#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:39:37 2018

@author: thomascormier
"""

import chess
import chess.pgn

game = chess.pgn.Game()
game.headers["Event"] = "Example"
node = game.add_variation(chess.Move.from_uci("e2e4"))
node = node.add_variation(chess.Move.from_uci("e7e5"))
ode.comment = "Comment"

board.fen = ('8/8/8/8/5R2/2pk4/5K2/8 b - - 0 1')

print(board.fen)


"""
[Event "PolyTournoi"]
[Site "Annecy"]
[Date "2018.12.12"]
[Round "1"]
[White "Evan"]
[Black "Maxence"]
[Result "0-1"]

1. e4 e5 { Comment } *
"""