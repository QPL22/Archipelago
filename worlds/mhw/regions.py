from . import MHWWorld
from BaseClasses import Region
from .locations import MHWLocation


def create_regions(world: MHWWorld):
    list = [Region("Menu", world.player, world.multiworld),
            Region("Zone 0", world.player, world.multiworld),
            Region("Zone 2", world.player, world.multiworld),
            Region("Zone 4", world.player, world.multiworld),
            Region("Zone 5", world.player, world.multiworld),
            Region("Zone 6", world.player, world.multiworld),
            Region("Zone 7", world.player, world.multiworld),
            Region("Zone 8", world.player, world.multiworld),
            Region("Zone 10", world.player, world.multiworld),
            Region("Zone 11", world.player, world.multiworld),]
    world.multiworld.regions += list
