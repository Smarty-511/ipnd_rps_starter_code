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
        x=input("Choose your move! ")
        if x.strip().lower()=='rock':
            return 'rock'
        elif x.strip().lower()=='paper':
            return 'paper'
        elif x.strip().lower()=='scissors':
            return 'scissors'
        else:
            return 'please provide a valid input'
        # while x not in moves:
        #     if x != 'z':
        #         x = input('Please enter a valid throw: rock, paper, scissors, or z.\n')

        # return x

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

def beats(self, one, two):
    if one == two:
        return f"It's a Tie!, score: {self.score1, self.score2}"
    elif ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock')):
        self.score1 +=1
        return f"Human wins!, score: {self.score1, self.score2}"
    else: 
        self.score2 +=1
        return f"Computer wins!, score: {self.score1, self.score2}"

    

class Game:
# score1 = human, score2 = computer
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0
        self.index = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Human: {move1}  Computer: {move2}")
        print(f"Result: {beats(self, move1,move2)}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
