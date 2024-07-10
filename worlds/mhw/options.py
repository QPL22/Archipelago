from Options import PerGameCommonOptions, Choice, Toggle, DefaultOnToggle, DeathLink, StartInventoryPool
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


class OverpoweredWeaponsAndArmor(DefaultOnToggle):
    """Adds the next rank of progressive weapons and armor to the pool.
    Note: This does not have an effect if selecting Master Rank."""
    display_name = "Overrank Weapons & Armor"


@dataclass
class MonsterHunterWorldOptions(PerGameCommonOptions):
    ending_rank: EndingRank
    arena_quests: ArenaQuests
    event_quests: EventQuests
    special_quests: SpecialQuests
    overpowered: OverpoweredWeaponsAndArmor
