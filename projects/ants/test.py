'''
from ants import *
hive, layout = Hive(AssaultPlan()), dry_layout
colony = AntColony(None, hive, ant_types(), layout, (1, 9))
#
# Testing bodyguard performs thrower's action
bodyguard = BodyguardAnt()
thrower = ThrowerAnt()
bee = Bee(2)
# Place thrower before bodyguard
colony.places["tunnel_0_0"].add_insect(thrower)
colony.places["tunnel_0_0"].add_insect(bodyguard)
colony.places["tunnel_0_3"].add_insect(bee)
bodyguard.action(colony)
'''
import ants, importlib
importlib.reload(ants)
hive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
colony = ants.AntColony(None, hive, ants.ant_types(),ants.dry_layout, dimensions)
ants.bees_win = lambda: None
# QueenAnt Placement
queen = ants.QueenAnt()
impostor = ants.QueenAnt()
front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
tunnel = [colony.places['tunnel_0_{0}'.format(i)] for i in range(9)]
tunnel[1].add_insect(back_ant)
tunnel[7].add_insect(front_ant)
tunnel[4].add_insect(impostor)
impostor.action(colony)
tunnel[4].add_insect(queen)
queen.action(colony)


