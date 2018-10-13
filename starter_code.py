#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random 

class Player:
    def move(self):
        # return random.choice(moves)
        pass

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):  
    def move(self):
        return random.choice(moves)


def beats(one, two):
    player1 = 0
    player2 = 0
    if one == two:
        return f"It's a Tie!, score: {player1, player2}"
    elif ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock')):
        player1 +=1
        return f"Player One wins!, score: {player1, player2}"
    else: 
        player2 +=1
        return f"Player Two wins!, score: {player1, player2}"

    

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        print(f"Result: {beats(move1,move2)}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
