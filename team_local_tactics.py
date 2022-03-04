#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:41:15 2022

@author: edyta
"""

from rich import print
from rich.prompt import Prompt
from rich.table import Table
from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team


def print_available_champs(champions: dict[Champion]) -> None:

    # Create a table containing available champions
    available_champs = Table(title='Available champions')

    # Add the columns Name, probability of rock, probability of paper and
    # probability of scissors
    available_champs.add_column("Name", style="cyan", no_wrap=True)
    available_champs.add_column("prob(:raised_fist-emoji:)", justify="center")
    available_champs.add_column("prob(:raised_hand-emoji:)", justify="center")
    available_champs.add_column("prob(:victory_hand-emoji:)", justify="center")

    # Populate the table
    for champion in champions.values():
        available_champs.add_row(*champion.str_tuple)
    print(available_champs)



def print_match_summary(match: Match):

    EMOJI = {
        Shape.ROCK: ':raised_fist-emoji:',
        Shape.PAPER: ':raised_hand-emoji:',
        Shape.SCISSORS: ':victory_hand-emoji:'
    }

    # For each round print a table with the results
    for index, round in enumerate(match.rounds):

        # Create a table containing the results of the round
        round_summary = Table(title=f'Round {index+1}')

        # Add columns for each team
        round_summary.add_column("Red",
                                 style="red",
                                 no_wrap=True)
        round_summary.add_column("Blue",
                                 style="blue",
                                 no_wrap=True)

        # Populate the table
        for key in round:
            red, blue = key.split(', ')
            round_summary.add_row(f'{red} {EMOJI[round[key].red]}',
                                  f'{blue} {EMOJI[round[key].blue]}')
        print(round_summary)
        print('\n')

    # Print the score
    red_score, blue_score = match.score
    print(f'Red: {red_score}\n'
          f'Blue: {blue_score}')

    # Print the winner
    if red_score > blue_score:
        a = ('\n[red]Red victory! :grin:')
    elif red_score < blue_score:
        a = ('\n[blue]Blue victory! :grin:')
    else:
        a = ('\nDraw :expressionless:')
    return [a, red_score, blue_score]




def input_champion(name,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected
    while True:
        match name:
            case name if name not in champions:
                print(f'The champion {name} is not available. Try again.')
            case name if name in player1:
                print(f'{name} is already in your team. Try again.')
            case name if name in player2:
                print(f'{name} is in the enemy team. Try again.')
            case _:
                player1.append(name)
                break


def game(a, b, c, d):
    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')
    
    champions = load_some_champs()
    print_available_champs(champions)
    print('\n')
    
    player1 = [a,b]
    player2 = [c,d]
    
 #   for name in [a, b, c, d]:
    #    input_champion( name, champions, player1, player2)
   #     input_champion( name, champions, player2, player1)

    print('\n')

   # Match
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    match.play()

    return (match)

def clientSiteGame(num):
    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = load_some_champs()
    print_available_champs(champions)
    print('\n')
    
    players = []
    for n in range(2):
        print("Player ", num,  " Fighter ", n+1)
        players.append((input(" Name "))) # take input
    return players