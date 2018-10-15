#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""

import random 

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass




class RandomPlayer(Player):  
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):  
    def move(self):
        x=input("Choose your move!\n")
        while x not in moves:
            if x != 'z':
                x = input('Please choose a valid move: rock, paper, scissors\n')


        return x.strip().lower()

    def learn(self, my_move, their_move):
        pass

# This player will learn human's previous move and play it for the next round
class ReflectPlayer(Player):

    def __init__(self):
        self.comp = random.choice(moves)
        self.enemy = ''

    def move(self):
        move1 = ''
        move2 = ''
        return ReflectPlayer.learn(self, move2, move1)

    def learn(self, my_move, their_move):
        self.enemy = self.comp
        self.comp = their_move
        return self.enemy
        
# This player will cycle through the provided moves
class CyclePlayer(Player):

    def __init__(self):
        self.index = 0

    def move(self):
        move1 = ''
        move2 = ''
        return CyclePlayer.learn(self, move2, move1)

    def learn(self, my_move, their_move):
        if self.index <2:
            self.index +=1
        else:
            self.index = 0
        return moves[self.index]

# returns 1 in case of human wins and 0 otherwise
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
# score1 = human, score2 = computer
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0


    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Human: {move1}  Computer: {move2}")
        if move1 == move2:
            print (f"It's a Tie!\nHuman Score:{self.score1}     Computer Score: {self.score2}")
        elif beats(move1,move2) ==1:
            self.score1 +=1
            print (f"Human wins!\nHuman Score:{self.score1}     Computer Score: {self.score2}")
        else: 
            self.score2 +=1
            print (f"Computer wins!\nHuman Score:{self.score1}      Computer Score: {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    print('Game Rules:\nscissor cuts paper,\npaper covers rock,\nrock crushes scissors')
    print('Choose one: "rock" --  "paper" -- "scissors"')
    print('to quit, press z')
    x = input('Choose Computer Player!\nEnter "random", "reflect", "repeat", or "cycle"\n')
    while x not in ['random', 'reflect', 'cycle', 'repeat']:
        if x != "z":
            x = input("Please enter a valid input\n")
        else: 
            print("Thank you for playing!")
            break
    if x == "random":
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif x == "cycle":
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
    elif x == "repeat":
        game = Game(HumanPlayer(), Player())
        game.play_game()
    elif x == "reflect":
        game = Game(HumanPlayer(), ReflectPlayer())             
        game.play_game()
