# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:41:12 2018

@author: duxiaoqin
Functions:
    (1) Minimax Algorithm for TicTacToe
"""

from graphics import *
from tictactoe import *
from tttdraw import *
from tttinput import *
import sys

def Minimax(node, depth):
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
            v, _, leafDepth = Minimax(child, depth+1)
            if bestValue == v and bestDepth > leafDepth:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
            if bestValue < v:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
        return bestValue, bestMove, bestDepth
    else:
        bestValue = sys.maxsize
        bestMove = ()
        bestDepth = sys.maxsize
        moves = node.getAllMoves()
        for move in moves:
            child = node.clone()
            child.play(*move)
            v, _, leafDepth = Minimax(child, depth+1)
            if bestValue == v and bestDepth > leafDepth:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
            if bestValue > v:
                bestValue = v
                bestMove = move
                bestDepth = leafDepth
        return bestValue, bestMove, bestDepth
    
def main():
    win = GraphWin('Minimax for TicTacToe', 600, 600, autoflush=False)
    ttt = TicTacToe()
    tttdraw = TTTDraw(win)
    tttinput = TTTInput(win)
    tttdraw.draw(ttt)

    while win.checkKey() != 'Escape':
        if ttt.getPlayer() == TicTacToe.WHITE:
            v, move, _ = Minimax(ttt, 0)
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