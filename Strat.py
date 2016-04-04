from  soccersimulator import settings
from soccersimulator import BaseStrategy, SoccerAction, KeyboardStrategy
from Strategies import *
from tmesolo import *
class Strat(BaseStrategy):
    def __init__(self,comportement,name):
        BaseStrategy.__init__(self,name)
        self.comportement = comportement
    def compute_strategy(self, state, id_team, id_player):
        s_miroir = state
        if id_team==1 :
            Mystate = PlayerStateDecorator(s_miroir,id_team , id_player)
            return self.comportement(Mystate)
        else :
            s_miroir = miroir_st(state)
            Mystate = PlayerStateDecorator(s_miroir,id_team , id_player)
            return miroir_sa(self.comportement(Mystate))


joueur_fonceur = Strat(joueur_fonceur, "A")
joueur_passeur = Strat(joueur_fonceur, "B")

