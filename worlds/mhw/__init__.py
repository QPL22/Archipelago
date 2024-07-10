import settings
import typing
from .options import MonsterHunterWorldOptions  # the options we defined earlier
from .items import masteritems_database, MHWItem  # data used below to add items to the World
from .locations import masterlocations_database, quest_database, arenaquest_database, eventquest_database, specialquest_database, LocType, MHWLocation  # same as above
from worlds.AutoWorld import World, WebWorld
from typing import Dict
from BaseClasses import Region, Location, Entrance, Item, ItemClassification, Tutorial


# Finish when almost done with dev
class MHWWeb(WebWorld):
    theme = "stone"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Monster Hunter World randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["QPL22"]
    )]


class MHWWorld(World):
    """Insert description of the world/game here."""
    game = "Monster Hunter World"  # name of the game/world
    options_dataclass = MonsterHunterWorldOptions  # options the player can set
    options: MonsterHunterWorldOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler
    base_id = 14000000000
    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: data.code for name, data in masteritems_database.items()}
    location_name_to_id = {name: data.code for name, data in masterlocations_database.items()}

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        set_region: Dict[int, Region] = {
            0: Region("Zone 0", self.player, self.multiworld),
            2: Region("Zone 2", self.player, self.multiworld),
            4: Region("Zone 4", self.player, self.multiworld),
        }

        menu_region.connect(set_region[0], "Jagras of the Ancient Forest")
        set_region[0].connect(set_region[2], "Bird-Brained Bandit", lambda state: state.has("Progressive Weapon", self.player, 2)
                       and state.has("Progressive Armor", self.player, 2))
        set_region[2].connect(set_region[4], "The Encroaching Anjanath", lambda state: state.has("Progressive Weapon", self.player, 4)
                        and state.has("Progressive Armor", self.player, 4))
        if self.options.ending_rank >= 1:
            set_region[5] = Region("Zone 5", self.player, self.multiworld)
            set_region[6] = Region("Zone 6", self.player, self.multiworld)
            set_region[7] = Region("Zone 7", self.player, self.multiworld)

            set_region[4].connect(set_region[5], "A Colossal Task", lambda state: state.has("Progressive Weapon", self.player, 5)
                        and state.has("Progressive Armor", self.player, 5))
            set_region[5].connect(set_region[6], "Tickled Pink", lambda state: state.has("Progressive Weapon", self.player, 6)
                        and state.has("Progressive Armor", self.player, 6))
            set_region[6].connect(set_region[7], "Old World Monster In The New World", lambda state: state.has("Progressive Weapon", self.player, 7)
                        and state.has("Progressive Armor", self.player, 7))
        if self.options.ending_rank == 2:
            set_region[8] = Region("Zone 8", self.player, self.multiworld)
            set_region[10] = Region("Zone 10", self.player, self.multiworld)
            set_region[11] = Region("Zone 11", self.player, self.multiworld)

            set_region[7].connect(set_region[8], "Land of Convergence", lambda state: state.has("Progressive Weapon", self.player, 8)
                        and state.has("Progressive Armor", self.player, 8))
            set_region[8].connect(set_region[10], "Blizzard Blitz", lambda state: state.has("Progressive Weapon", self.player, 10)
                        and state.has("Progressive Armor", self.player, 10))
            set_region[10].connect(set_region[11], "The Iceborne Wyvern", lambda state: state.has("Progressive Weapon", self.player, 11)
                        and state.has("Progressive Armor", self.player, 11))

        for loc_name, loc_data in quest_database.items():
            if loc_data.zone in set_region:
                loc_region = set_region[loc_data.zone]
                loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                loc_region.locations.append(loc)

        if self.options.arena_quests.value == 1:
            for loc_name, loc_data in arenaquest_database.items():
                if loc_data.zone in set_region:
                    loc_region = set_region[loc_data.zone]
                    loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                    loc_region.locations.append(loc)

        if self.options.event_quests.value == 1:
            for loc_name, loc_data in eventquest_database.items():
                if loc_data.zone in set_region:
                    loc_region = set_region[loc_data.zone]
                    loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                    loc_region.locations.append(loc)

        if self.options.special_quests.value == 1:
            for loc_name, loc_data in specialquest_database.items():
                if loc_data.zone in set_region:
                    loc_region = set_region[loc_data.zone]
                    loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                    loc_region.locations.append(loc)

        menu_region.connect(set_region[0])
        self.multiworld.regions += [
            menu_region,
            *set_region.values()
        ]

    def create_items(self) -> None:
        item_count = 0
        total_required_locations = len(self.multiworld.get_unfilled_locations(self.player))
        progressive_gear_amount = 0
        if (self.options.ending_rank.value == 2) or (self.options.overpowered.value == 0):
            progressive_gear_amount = (4 * (self.options.ending_rank.value + 1)+1)
        else:
            progressive_gear_amount = (4 * (self.options.ending_rank.value + 2)+1)

        for key, element in masteritems_database.items():
            if element.classification.progression:
                for _ in range(progressive_gear_amount):
                    item = self.create_item(key)
                    self.multiworld.itempool.append(item)
                    item_count += 1

        for x in range(total_required_locations-item_count):
            item = self.create_item(self.get_filler_item_name())
            self.multiworld.itempool.append(item)

    def get_filler_item_name(self) -> str:
        return "1,000 Zenny"

    def create_item(self, name: str) -> "Item":
        data = masteritems_database[name]
        return MHWItem(name, data.classification, data.code, self.player)

    def set_rules(self) -> None:
        if self.options.ending_rank.value == 0:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("A Colossal Task", self.player)
        elif self.options.ending_rank.value == 1:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Land of Convergence", self.player)
        else:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Paean of Guidance", self.player)
    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
    #     "weapons": {"sword", "lance"},
    # }
