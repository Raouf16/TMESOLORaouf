from soccersimulator import show
from soccersimulator import SoccerTeam,Player, SoccerMatch
from team import *
from tmesolo import *
match = SoccerMatch(team2,team1,init_state=PADState.create_initial_state(2,1))
show(match)
match = SoccerMatch(team4,team3,init_state=PADState.create_initial_state(4,3))
show(match)
