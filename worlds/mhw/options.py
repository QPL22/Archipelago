from Options import PerGameCommonOptions, Choice, Toggle, DefaultOnToggle, DeathLink, StartInventoryPool, Range
from dataclasses import dataclass


class Iceborne(DefaultOnToggle):
    """Do have the Iceborne DLC installed?
    Note: Certain settings require the DLC to be installed. If you select off and a certain setting requires the DLC to
    be installed, there will be an error and the generation will continue with the setting disabled. If you leave this
    setting on and the game detects you do not have Iceborne installed you will not be able to join the game and will be
    required to generate the game again."""
    display_name = "Iceborne DLC Installed"


class EndingRank(Choice):
    """Choose which rank you must reach the end of in order to complete.
    Low Rank: Finish \"A Colossal Task\"
    High Rank: Finish \"Land of Convergence\"
    Master Rank: Finish \"Paean of Guidance\""""
    display_name = "Completed Rank"
    option_low_rank = 0
    option_high_rank = 1
    option_master_rank = 2
    default = 1


class ArenaQuests(Toggle):
    """Adds Special Arena Quests to the quest pool.
    Note: These are the quest that are unlocked when you capture a monster."""
    display_name = "Special Arena Quests"


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
    display_name = "Grindy Quests"


class SinglePlayer(DefaultOnToggle):
    """Sets all quests to only allow one player to join. Good to do if you aren't playing multiplayer with anyone else in your world."""
    display_name = "Set Quests to Singleplayer Only"


class QuestRando(DefaultOnToggle):
    """Randomizes what monster is required for quest completion.
    Required to be on for all other quest randomization settings."""
    display_name = "Randomized Quest"


class IceQuestRando(DefaultOnToggle):
    """Randomizes what monster is required for quest completion.
    Iceborne is required for this."""
    display_name = "Randomized Iceborne Quests"


class QuestIcon(Choice):
    """Changes the icon for the monster to make it more of a surpise.
    Same: Icon will always match the monster given.
    Question Mark: All monster icons will be the question mark icon.
    Totally Random: Totally random icons.
    Handler Error: The chance of an error is the same as the Handler Error."""
    display_name = "Monster Quest Icons"
    option_same = 0
    option_question_mark = 1
    option_totally_random = 2
    option_handler_error = 3
    default = 1


# Might not be required since sorted to with previous quests info
class MultiObjective(Toggle):
    """Randomize quests that require 2 different monster to hunt/slay."""
    display_name = "Randomize Multi-Objective Quests"


# Might not be required since sorted to with previous quests info
class MultiMonster(Toggle):
    """Randomize quests with 2-5 monsters."""
    display_name = "Randomize Multi-Objective Quests"


class SameMonster(Toggle):
    """Randomize quests where you have to hunt two of the same monster."""
    display_name = "Randomize Quests with 2 of Same Monster"


class NoSlay(Toggle):
    """Won't randomize quests with the objective to slay large monsters."""
    display_name = "Don't Randomize Slay Quests"


class NoCapture(Toggle):
    """Won't randomize quests with the objective to capture large monsters."""
    display_name = "Don't Randomize Capture Quests"


class AllowDupMon(Toggle):
    """Allows duplicate monsters to appear on a quest."""
    display_name = "Duplicate Monsters on Quest"


class RandMonSpawn(DefaultOnToggle):
    """Randomize the spawn location of monsters."""
    display_name = "Randomize Monster Spawn"


class IceMonsterOptions(Choice):
    """Sets what monsters can be randomized to Iceborne quests.
    All Iceborne Monsters: Only randomizes monsters that found in Iceborne quests.
    Only Iceborne Added: All monster icons will be the question mark icon.
    All Monsters: Include all the monsters from all the ranks. !!!Experimental!!! Recommend free armor and free weapons."""
    display_name = "Iceborne Monster Pool Options"
    option_all_iceborne_monsters = 0
    option_only_iceborne_added = 1
    option_all_monsters = 2
    default = 0


class HighInLowMon(Toggle):
    """Allows high rank monsters in low rank. Challenging. Recommend making weapons and armor free with this on."""
    display_name = "High Rank Monster in Low Rank"


class MasterInPool(Choice):
    """Allows master rank monsters to spawn in lower ranks. !!!Experiemental!!!
    Requires Iceborne. Recommend making weapons and armor free with this on.
    Off: Won't spawn master rank monsters in lower ranks.
    High Rank Only: Master rank monsters have a chance to appear in high rank quests.
    All Ranks: Master rank monsters have a chance to appear in all ranks."""
    display_name = "Monster Quest Icons"
    option_off = 0
    option_high_rank_only = 1
    option_all_ranks = 2
    default = 0


class IncLeshen(Toggle):
    """Allows the Leshen to be added to the monster pool. Challenging."""
    display_name = "Include Leshen"


class IncBehemoth(Toggle):
    """Allows the Behemoth to be added to the monster pool. Challenging. !!!Experiemental!!! May get stuck."""
    display_name = "Include Behemoth"


class IncShara(Toggle):
    """Requires Iceborne.
    Allows the Shara to be added to the monster pool. Challenging. !!!Experiemental!!! May get stuck."""
    display_name = "Include Shara Ishvalda"


class IncRajang(Toggle):
    """Requires Iceborne.
    Allows the Furious Rajang to be added to the monster pool. Challenging. !!!Experiemental!!! May get stuck."""
    display_name = "Include Furious Rajang"


class IncAlatreon(Toggle):
    """Requires Iceborne.
    Allows the Alatreon to be added to the monster pool. Challenging. !!!Experiemental!!! May get stuck."""
    display_name = "Include Alatreon"


class SecondMonChance(Range):
    """Sets the weight of having a quest with a second monster objective."""
    display_name = "Second Monster Objective Chance"
    range_start = 0
    range_end = 100
    default = 0


class ThirdMonChance(Range):
    """Sets the weight of having a quest with a second monster objective.
    Note: This is the chance of getting a third monster objective if there is a second monster obejective.
    This will be same for the following options."""
    display_name = "Third Monster Objective Chance"
    range_start = 0
    range_end = 100
    default = 0


class FourthMonChance(Range):
    """Sets the weight of having a quest with a second monster objective.
    Note: This is the chance of getting a third monster objective if there is a second monster obejective.
    This will be same for the following options."""
    display_name = "Fourth Monster Objective Chance"
    range_start = 0
    range_end = 100
    default = 0


class FifthMonChance(Range):
    """Sets the weight of having a quest with a second monster objective."""
    display_name = "Fifth Monster Objective Chance"
    range_start = 0
    range_end = 100
    default = 0


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
    default = 10


class UtilityLootBox(Range):
    """Sets the weight of receiving a Utility Loot Box"""
    display_name = "Utility Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


class BuffBoxWeight(Range):
    """Sets the weight of receiving a Buff Loot Box"""
    display_name = "Buff Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


class AmmoBoxWeight(Range):
    """Sets the weight of receiving an Ammo Loot Box"""
    display_name = "Ammo Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


class IngredientBoxWeight(Range):
    """Sets the weight of receiving an Ingredient Loot Box"""
    display_name = "Ingredient Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


class JunkBoxWeight(Range):
    """Sets the weight of receiving a Junk Loot Box"""
    display_name = "Junk Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


class MeldingBoxWeight(Range):
    """Sets the weight of receiving a Melding Loot Box"""
    display_name = "Melding Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


class ChanceBoxWeight(Range):
    """Sets the weight of receiving a Chance Loot Box"""
    display_name = "Chance Box Chance Weight"
    range_start = 0
    range_end = 100
    default = 10


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


class SeasonalArmor(Toggle):
    """Makes it so seasonal armor and weapons are added to the pool for free weapons and armors."""
    display_name = "Seasonal Armor and Weapons"

@dataclass
class MonsterHunterWorldOptions(PerGameCommonOptions):
    iceborne: Iceborne
    ending_rank: EndingRank
    specialarena_quests: ArenaQuests
    event_quests: EventQuests
    special_quests: SpecialQuests
    grindy_quests: GrindyQuests
    singleplayer: SinglePlayer
    quest_rando: QuestRando
    ice_quest_rando: IceQuestRando
    mon_icon: QuestIcon
    multiobjective: MultiObjective
    multimonster: MultiMonster
    same_monster: SameMonster
    noslay: NoSlay
    nocap: NoCapture
    dup_mon: AllowDupMon
    mon_spawn: RandMonSpawn
    ice_mon: IceMonsterOptions
    high_in_low_mon: HighInLowMon
    mastermon: MasterInPool
    leshen: IncLeshen
    behemoth: IncBehemoth
    shara: IncShara
    rajang: IncRajang
    alatreon: IncAlatreon
    overpowered_equip: OverpoweredWeaponsAndArmor
    freearmor: FreeArmor
    freeweapon: FreeWeapon
    seasonal: SeasonalArmor
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
    utilityweight: UtilityLootBox
    healingweight: HealingBoxWeight

