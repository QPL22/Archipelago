from BaseClasses import Item, ItemClassification
from .options import MonsterHunterWorldOptions
from enum import IntFlag
import typing
from typing import Dict
# Joel wants me to add gifting


class MHWItem(Item):
    game = "Monster Hunter World"


class ItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification
    count: int = None


ITEM_ID_OFFSET = 14100000000


item_database: Dict[str, ItemData] = {
    "Progressive Weapon": ItemData(ITEM_ID_OFFSET + 1, ItemClassification.progression),
    "Progressive Armor": ItemData(ITEM_ID_OFFSET + 2, ItemClassification.progression),
    "1,000 Zenny": ItemData(ITEM_ID_OFFSET + 3, ItemClassification.filler),
    "Healing Loot Box": ItemData(ITEM_ID_OFFSET + 4, ItemClassification.filler),
    "Trap Loot Box": ItemData(ITEM_ID_OFFSET + 5, ItemClassification.filler),
    "Buff Loot Box": ItemData(ITEM_ID_OFFSET + 6, ItemClassification.filler),
    "Ammo Loot Box": ItemData(ITEM_ID_OFFSET + 7, ItemClassification.filler),
    "Ingredient Loot Box": ItemData(ITEM_ID_OFFSET + 8, ItemClassification.filler),
    "Junk Loot Box": ItemData(ITEM_ID_OFFSET + 9, ItemClassification.filler),
    "Melding Loot Box": ItemData(ITEM_ID_OFFSET + 10, ItemClassification.filler),  # Disable
    "Chance Loot Box": ItemData(ITEM_ID_OFFSET + 11, ItemClassification.filler),
}

specialized_database: Dict[str, ItemData] = {
    "Ghillie Mantle": ItemData(ITEM_ID_OFFSET + 100, ItemClassification.useful),
    "Temporal Mantle": ItemData(ITEM_ID_OFFSET + 101, ItemClassification.useful),
    "Health Booster": ItemData(ITEM_ID_OFFSET + 102, ItemClassification.useful),
    "Rocksteady Mantle": ItemData(ITEM_ID_OFFSET + 103, ItemClassification.useful),
    "Challenger Mantle": ItemData(ITEM_ID_OFFSET + 104, ItemClassification.useful),
    "Vitality Mantle": ItemData(ITEM_ID_OFFSET + 105, ItemClassification.useful),
    "Fireproof Mantle": ItemData(ITEM_ID_OFFSET + 106, ItemClassification.useful),
    "Waterproof Mantle": ItemData(ITEM_ID_OFFSET + 107, ItemClassification.useful),
    "Iceproof Mantle": ItemData(ITEM_ID_OFFSET + 108, ItemClassification.useful),
    "Thunderproof Mantle": ItemData(ITEM_ID_OFFSET + 109, ItemClassification.useful),
    "Dragonproof Mantle": ItemData(ITEM_ID_OFFSET + 110, ItemClassification.useful),
    "Cleanser Booster": ItemData(ITEM_ID_OFFSET + 111, ItemClassification.useful),
    "Glider Mantle": ItemData(ITEM_ID_OFFSET + 112, ItemClassification.useful),
    "Evasion Mantle": ItemData(ITEM_ID_OFFSET + 113, ItemClassification.useful),
    "Impact Mantle": ItemData(ITEM_ID_OFFSET + 114, ItemClassification.useful),
    "Apothecary Mantle": ItemData(ITEM_ID_OFFSET + 115, ItemClassification.useful),
    "Immunity Mantle": ItemData(ITEM_ID_OFFSET + 116, ItemClassification.useful),
    "Affinity Booster": ItemData(ITEM_ID_OFFSET + 117, ItemClassification.useful),
    "Bandit Mantle": ItemData(ITEM_ID_OFFSET + 118, ItemClassification.useful),
    # Event Only "Assassin's Hood": ItemData(ITEM_ID_OFFSET + 119, ItemClassification.useful),
}

masteritems_database: typing.Dict[str, ItemData] = {
    **item_database,
    **specialized_database,
}



