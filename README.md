# SlidingPuzzle

## Description

The motivation behind this project was to learn how to implement the A* algorithm into a fun game that many people have played before
and have the computer find the shortest path to find the answer. This game can take a puzzle of numbers of any size n x m, and the A* 
algorithm will find the shortest path to rearrange them according to correct ordering. 
The puzzle may take a puzzle that looks like this:
        4 7 3    and reorder the numbers to look like this       0 1 2
        0 8 5               ------------>                        3 4 5
        1 6 2                                                    6 7 8


## Installation

This program runs with Python 3 and requires these packages to be installed first before running:

        pip install heapq
        pip install math
        pip install copy
        pip install sys
        pip install tkinter

## Usage

Run slidingpuzzle.py puzzlename.puz on terminal inside SlidingPuzzle directory:
------> Puzzle files that are in the directory are called easy.puz, impossible.puz, and square.puz
