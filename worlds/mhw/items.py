from BaseClasses import Item, ItemClassification
from .options import MonsterHunterWorldOptions
from enum import IntFlag
import typing
from typing import Dict
# Joel wants me to add gifting


class MHWItem(Item):
    game = "Monster Hunter World"


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: ItemClassification
    count: int = None


item_database: Dict[str, ItemData] = {
    "Progressive Weapon": ItemData(1, ItemClassification.progression),
    "Progressive Armor": ItemData(2, ItemClassification.progression),
    "1,000 Zenny": ItemData(3, ItemClassification.filler, 0),
}


masteritems_database: typing.Dict[str, ItemData] = {
    **item_database,
}