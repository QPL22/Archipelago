import settings
import typing
from .options import MonsterHunterWorldOptions  # the options we defined earlier
from .items import masteritems_database, MHWItem, ITEM_ID_OFFSET, \
    specialized_database  # data used below to add items to the World
from .locations import masterlocations_database, quest_database, arenaquest_database, eventquest_database, \
    specialquest_database, endemiclife_database, LocType, MHWLocation, LOCATION_ID_OFFSET, \
    ENDEMIC_ID_OFFSET, grindy_database, specializedtools_database  # same as above
from worlds.AutoWorld import World, WebWorld
from typing import Dict, List
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
    required_client_version = (0, 1, 0)
    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {name: data.code for name, data in masteritems_database.items()}
    location_name_to_id = {name: data.code for name, data in masterlocations_database.items()}
    filleritem: List
    filler_weight: int

    def generate_early(self) -> None:
        self.filler_weight = (
                self.options.healingweight.value + self.options.trapweight.value + self.options.buffweight.value
                + self.options.ammoweight.value + self.options.ingredientweight.value + self.options.junkweight.value +
                self.options.meldingweight.value + self.options.chanceweight.value + self.options.zennyweight.value)
        self.filleritem = [("1,000 Zenny", self.options.zennyweight.value),
                           ("Healing Loot Box", self.options.healingweight.value),
                           ("Trap Loot Box", self.options.trapweight), ("Buff Loot Box", self.options.buffweight),
                           ("Ammo Loot Box", self.options.ammoweight.value),
                           ("Ingredient Loot Box", self.options.ingredientweight),
                           ("Junk Loot Box", self.options.junkweight.value),
                           ("Melding Loot Box", self.options.meldingweight.value),
                           ("Chance Loot Box", self.options.chanceweight.value)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        set_region: Dict[int, Region] = {
            0: Region("Zone 0", self.player, self.multiworld),
            2: Region("Zone 2", self.player, self.multiworld),
            4: Region("Zone 4", self.player, self.multiworld),
        }

        menu_region.connect(set_region[0], "Jagras of the Ancient Forest")
        set_region[0].connect(set_region[2], "Bird-Brained Bandit",
                              lambda state: state.has("Progressive Weapon", self.player, 2)
                                            and state.has("Progressive Armor", self.player, 2))
        set_region[2].connect(set_region[4], "The Encroaching Anjanath",
                              lambda state: state.has("Progressive Weapon", self.player, 4)
                                            and state.has("Progressive Armor", self.player, 4))
        if self.options.ending_rank >= 1:
            set_region[5] = Region("Zone 5", self.player, self.multiworld)
            set_region[6] = Region("Zone 6", self.player, self.multiworld)
            set_region[7] = Region("Zone 7", self.player, self.multiworld)

            set_region[4].connect(set_region[5], "A Colossal Task",
                                  lambda state: state.has("Progressive Weapon", self.player, 5)
                                                and state.has("Progressive Armor", self.player, 5))
            set_region[5].connect(set_region[6], "Tickled Pink",
                                  lambda state: state.has("Progressive Weapon", self.player, 6)
                                                and state.has("Progressive Armor", self.player, 6))
            set_region[6].connect(set_region[7], "Old World Monster In The New World",
                                  lambda state: state.has("Progressive Weapon", self.player, 7)
                                                and state.has("Progressive Armor", self.player, 7))
        if self.options.ending_rank == 2:
            set_region[8] = Region("Zone 8", self.player, self.multiworld)
            set_region[10] = Region("Zone 10", self.player, self.multiworld)
            set_region[11] = Region("Zone 11", self.player, self.multiworld)

            set_region[7].connect(set_region[8], "Land of Convergence",
                                  lambda state: state.has("Progressive Weapon", self.player, 8)
                                                and state.has("Progressive Armor", self.player, 8))
            set_region[8].connect(set_region[10], "Blizzard Blitz",
                                  lambda state: state.has("Progressive Weapon", self.player, 10)
                                                and state.has("Progressive Armor", self.player, 10))
            set_region[10].connect(set_region[11], "The Iceborne Wyvern",
                                   lambda state: state.has("Progressive Weapon", self.player, 11)
                                                 and state.has("Progressive Armor", self.player, 11))

        for loc_name, loc_data in quest_database.items():
            if loc_data.zone in set_region:
                loc_region = set_region[loc_data.zone]
                loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                loc_region.locations.append(loc)

        if self.options.specialarena_quests.value == 1:
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
                    if loc_data.loc_type.Tool and self.options.specialized_tools.value == 0:
                        continue
                    loc_region = set_region[loc_data.zone]
                    loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                    loc_region.locations.append(loc)

        if self.options.grindy_quests.value == 1:
            for loc_name, loc_data in grindy_database.items():
                if loc_data.zone in set_region:
                    if loc_data.loc_type.Tool and self.options.specialized_tools.value == 0:
                        continue
                    loc_region = set_region[loc_data.zone]
                    loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                    loc_region.locations.append(loc)

        if self.options.specialized_tools.value == 1:
            for loc_name, loc_data in specializedtools_database.items():
                if loc_data.zone in set_region:
                    loc_region = set_region[loc_data.zone]
                    loc = MHWLocation(self.player, loc_name, loc_data.code, loc_region)
                    loc_region.locations.append(loc)

        if self.options.endemiclife.value == 1 or self.options.rareendemic.value == 1 or self.options.legendendemic.value == 1:
            for loc_name, loc_data in endemiclife_database.items():
                if loc_data.zone in set_region and (
                        (self.options.endemiclife.value == 1 and LocType.Normal_Life in loc_data)
                        or (self.options.rareendemic.value == 1 and LocType.Rare_Life in loc_data)
                        or (self.options.legendendemic.value == 1 and LocType.Legendary_Life in loc_data)):
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
        if (self.options.ending_rank.value == 2) or (self.options.overpowered_equip.value == 0):
            progressive_gear_amount = (4 * (self.options.ending_rank.value + 1) + 1)
        else:
            progressive_gear_amount = (4 * (self.options.ending_rank.value + 2) + 1)

        if (self.options.ending_rank.value == 2 or self.options.overpowered_tools.value == 1) and self.options.specialized_tools.value == 1:
            tool_amount = 2
        elif self.options.specialized_tools.value == 1:
            tool_amount = 1
        else:
            tool_amount = 0

        for key, element in masteritems_database.items():
            if ItemClassification.progression in element.classification:
                for _ in range(progressive_gear_amount):
                    item = self.create_item(key)
                    self.multiworld.itempool.append(item)
                    item_count += 1

        if self.options.specialized_tools.value == 1:
            for key, element in specialized_database.items():
                for _ in range(tool_amount):
                    item = self.create_item(key)
                    self.multiworld.itempool.append(item)
                    item_count += 1

        for x in range(total_required_locations - item_count):
            item = self.create_item(self.get_filler_item_name())
            self.multiworld.itempool.append(item)

    def get_filler_item_name(self) -> str:
        temp = self.random.randint(1, self.filler_weight)
        for x in self.filleritem:
            temp -= x[1]
            if temp <= 0:
                return x[0]
        return "1,000 Zenny"

    def create_item(self, name: str) -> "Item":
        data = masteritems_database[name]
        return MHWItem(name, data.classification, data.code, self.player)

    def set_rules(self) -> None:
        if self.options.ending_rank.value == 0:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location(
                "A Colossal Task", self.player)
        elif self.options.ending_rank.value == 1:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location(
                "Land of Convergence", self.player)
        else:
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location(
                "Paean of Guidance", self.player)

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
    #     "weapons": {"sword", "lance"},
    # }

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        slot_data = {
            "location_id": LOCATION_ID_OFFSET,
            "item_id": ITEM_ID_OFFSET,
            "endemic_id": ENDEMIC_ID_OFFSET,
            "free_weapon": self.options.freeweapon.value,
            "free_armor": self.options.freearmor.value,
            "seasonal": self.options.seasonal.value,
            "wincon": self.options.ending_rank.value,
        }

        return slot_data
