from Options import PerGameCommonOptions, Choice, Toggle, DefaultOnToggle, DeathLink, StartInventoryPool, Range
from dataclasses import dataclass


class EndingRank(Choice):
    """Choose which rank you must reach the end of in order to complete.
    Low Rank: Finish \"Invader In The Waste\"
    High Rank: Finish \"Land of Convergence\"
    Master Rank: Finish \"Paean of Guidance"""
    display_name = "Completed Rank"
    option_low_rank = 0
    option_high_rank = 1
    option_master_rank = 2
    default = 1


class ArenaQuests(Toggle):
    """Adds Arena Quests to the quest pool."""
    display_name = "Arena Quests"


class EventQuests(Toggle):
    """Adds Event Quests to the quest pool."""
    display_name = "Event Quests"


class SpecialQuests(Toggle):
    """Adds Special Quests to the quest pool.
    Note: This does not add any Low Rank and one High Rank quest."""
    display_name = "Special Quests"


class GrindyQuests(Toggle):
    """Adds some quests and some dependent locations to the pool.
    Note: These quests require a significant amount of effort to unlock."""
    display_name = "Special Quests"


class OverpoweredWeaponsAndArmor(DefaultOnToggle):
    """Adds the next rank of progressive weapons and armor to the pool.
    Note: This does not have an effect if selecting Master Rank."""
    display_name = "Overrank Weapons & Armor"


class SpecializedTools(DefaultOnToggle):
    """Adds specialized tools to the item pool and location pool.
    Note: Currently the tool slots are not taken into account and will be unlocked per usual."""
    display_name = "Specialized Tools"


class OverpoweredSpecializedTools(DefaultOnToggle):
    """Adds the upgraded form of specialized tools to the item pool.
    Note: This does not have an effect if selecting Master Rank."""
    display_name = "Overpowered Tools"


class EndemicLife(Toggle):
    """Adds catching basic endemic life to the location pool."""
    display_name = "Endemic Life"


class RareEndemicLife(Toggle):
    """Adds catching rare endemic life to the location pool.
    These are animals that will likely appear during the game but you may need to seek them out."""
    display_name = "Rare Endemic Life"


class LegendaryEndemicLife(Toggle):
    """Adds catching legendary endemic life to the location pool.
    You will need to seek these animals in their specific conditions."""
    display_name = "Legendary Endemic Life"


class HealingBoxWeight(Range):
    """Sets the weight of receiving a Healing Loot Box"""
    display_name = "Healing Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class TrapBoxWeight(Range):
    """Sets the weight of receiving a Trap Loot Box"""
    display_name = "Trap Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class BuffBoxWeight(Range):
    """Sets the weight of receiving a Buff Loot Box"""
    display_name = "Buff Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class AmmoBoxWeight(Range):
    """Sets the weight of receiving an Ammo Loot Box"""
    display_name = "Ammo Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class IngredientBoxWeight(Range):
    """Sets the weight of receiving an Ingredient Loot Box"""
    display_name = "Ingredient Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class JunkBoxWeight(Range):
    """Sets the weight of receiving a Junk Loot Box"""
    display_name = "Junk Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class MeldingBoxWeight(Range):
    """Sets the weight of receiving a Melding Loot Box"""
    display_name = "Melding Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class ChanceBoxWeight(Range):
    """Sets the weight of receiving a Chance Loot Box"""
    display_name = "Chance Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 50


class ZennyWeight(Range):
    """Sets the weight of receiving an amount of Zenny"""
    display_name = "Zenny Chance Weight"
    range_start = 1
    range_end = 200
    default = 150


class FreeArmor(DefaultOnToggle):
    """Makes Armors cost no materials"""
    display_name = "Free Armor Crafting"


class FreeWeapon(DefaultOnToggle):
    """Makes Weapons cost no materials"""
    display_name = "Free Weapon Crafting"


@dataclass
class MonsterHunterWorldOptions(PerGameCommonOptions):
    ending_rank: EndingRank
    arena_quests: ArenaQuests
    event_quests: EventQuests
    special_quests: SpecialQuests
    grindy_quests: GrindyQuests
    overpowered_equip: OverpoweredWeaponsAndArmor
    freearmor: FreeArmor
    freeweapon: FreeWeapon
    endemiclife: EndemicLife
    rareendemic: RareEndemicLife
    legendendemic: LegendaryEndemicLife
    specialized_tools: SpecializedTools
    overpowered_tools: OverpoweredSpecializedTools
    zennyweight: ZennyWeight
    chanceweight: ChanceBoxWeight
    meldingweight: MeldingBoxWeight
    junkweight: JunkBoxWeight
    ingredientweight: IngredientBoxWeight
    ammoweight: AmmoBoxWeight
    buffweight: BuffBoxWeight
    trapweight: TrapBoxWeight
    healingweight: HealingBoxWeight


