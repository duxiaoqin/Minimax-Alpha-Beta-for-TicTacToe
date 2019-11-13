# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:53:08 2018

@author: duxiaoqin
Functions:
    (1) Alpha-Beta Algorithm for TicTacToe
"""

from graphics import *
from tictactoe import *
from tttdraw import *
from tttinput import *
import sys
import time

def AlphaBeta(node, depth, alpha, beta):
    result = node.isGameOver()
    if result != None:
        return result, (), depth
    if node.getPlayer() == TicTacToe.BLACK:
        bestValue = -sys.maxsize
        bestMove = ()
        bestDepth = sys.maxsize
        moves = node.getAllMoves()
        for move in moves:
            child = node.clone()
            child.play(*move)
            v, _, leafDepth = AlphaBeta(child, depth+1, alpha, beta)
            if bestValue == v and bestDepth > leafDepth:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
            if bestValue < v:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break #beta pruning
        return bestValue, bestMove, bestDepth
    else:
        bestValue = sys.maxsize
        bestMove = ()
        bestDepth = sys.maxsize
        moves = node.getAllMoves()
        for move in moves:
            child = node.clone()
            child.play(*move)
            v, _, leafDepth = AlphaBeta(child, depth+1, alpha, beta)
            if bestValue == v and bestDepth > leafDepth:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
            if bestValue > v:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
            beta = min(beta, bestValue)
            if beta <= alpha:
                break #alpha pruning
        return bestValue, bestMove, bestDepth
    
def main():
    win = GraphWin('Minimax for TicTacToe', 600, 600, autoflush=False)
    ttt = TicTacToe()
    tttdraw = TTTDraw(win)
    tttinput = TTTInput(win)
    tttdraw.draw(ttt)

    while win.checkKey() != 'Escape':
        if ttt.getPlayer() == TicTacToe.WHITE:
            v, move, _ = AlphaBeta(ttt, 0, -sys.maxsize, sys.maxsize)
            if move != ():
                ttt.play(*move)
        tttinput.input(ttt)
        tttdraw.draw(ttt)
        if ttt.isGameOver() != None:
            time.sleep(1)
            ttt.reset()
            tttdraw.draw(ttt)
            #win.getMouse()
    win.close()
    
if __name__ == '__main__':
    main()