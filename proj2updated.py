#!/usr/bin/env python3
import random
import sys
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    round = 1

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        while True:
            if beats(move1, move2):
                self.p1.score = self.p1.score + 1
                print(" You Win")
            elif move1 == move2:
                print(" Tie")
            else:
                self.p2.score = self.p2.score + 1
                print("You Lose")
            print("Score Player 1 " + str(self.p1.score))
            print("Score Player 2 " + str(self.p2.score))
            break
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        while self.p1 and self.p2:
            print(f"Round {Game.round}")
            self.play_round()
            Game.round += 1
        print("Game over!")


class HumanPlayer(Player):
    def move(self):
        choose = input("rock, paper, scissors? >")
        while choose.lower() not in moves:
            choose = input("rock, paper, scissors? >").lower()
            if choose == "exit":
                sys.exit()
        return choose

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None
    def move(self):
        if self.my_move == 'rock':
            self.my_move = 'paper'
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
        else:
            self.my_move = 'rock'
        return self.my_move


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return Player.move(self)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


if __name__ == '__main__':
    game = Game(HumanPlayer(), Player()) 
    game = Game(HumanPlayer(), RandomPlayer()) 
    game = Game(HumanPlayer(), CyclePlayer()) 
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
