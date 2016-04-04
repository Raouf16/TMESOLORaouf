import soccersimulator
from soccersimulator import BaseStrategy, Vector2D, SoccerAction, settings
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Player, SoccerTournament
from Strat import *
from tmesolo import *

team1 = SoccerTeam ("DZPOWER",[Player("Messi",joueur_fonceur)])


team2 = SoccerTeam ("DZPOWER",[Player("Raouf",joueur_passeur), Player("Yacine",joueur_passeur)])

team3 = SoccerTeam ("DZPOWER",[Player("Raouf",joueur_fonceur), Player("Yacine",joueur_fonceur), Player("Yacine",joueur_fonceur)])

team4 = SoccerTeam ("DZPOWER",[Player("Raouf",joueur_passeur), Player("Yacine",joueur_passeur), Player("Raouf JR",joueur_passeur), Player("Yacine JR",joueur_passeur)])



