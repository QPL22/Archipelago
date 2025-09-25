from BaseClasses import Location
from enum import IntFlag
import typing
from typing import Dict, List


class MHWLocation(Location):
    game = "Monster Hunter World"

    def __init__(self, player: int, name: str = '', code: int = None, parent=None):
        super().__init__(player, name, code, parent)
        self.event = code is None
        self.show_in_spoiler = code is not None




class LocType(IntFlag):
    Normal = 0
    Low_Rank = 1
    High_Rank = 2
    Master_Rank = 4
    Event_Quest = 8
    Normal_Life = 16
    Rare_Life = 32
    Legendary_Life = 64
    Tool = 128


class LocationData(typing.NamedTuple):
    code: int
    loc_type: LocType
    zone: int
    required_quest: List[str] = None


LOCATION_ID_OFFSET = 14000000000
ENDEMIC_ID_OFFSET = LOCATION_ID_OFFSET + 10000

# Multi Cursor with alt click
quest_database: Dict[str, LocationData] = {
    # Level 1 Quests
    "Jagras of the Ancient Forest": LocationData(LOCATION_ID_OFFSET + 101, LocType.Low_Rank, 0),
    "Learning to Clutch": LocationData(LOCATION_ID_OFFSET + 241, LocType.Low_Rank, 0),
    "Butting Heads With Nature": LocationData(LOCATION_ID_OFFSET + 151, LocType.Low_Rank, 0, ["A Kestodon Kerfuffle"]),
    "A Thicket of Thugs": LocationData(LOCATION_ID_OFFSET + 152, LocType.Low_Rank, 0, ["Jagras of the Ancient Forest"]),
    "Fungal Flexin' in the Ancient Forest": LocationData(LOCATION_ID_OFFSET + 153, LocType.Low_Rank, 0, ["Jagras of the Ancient Forest"]),
    # Level 2 Assigned Quests
    "A Kestodon Kerfuffle": LocationData(LOCATION_ID_OFFSET + 102, LocType.Low_Rank, 0, ["Jagras of the Ancient Forest"]),
    "The Great Jagras Hunt": LocationData(LOCATION_ID_OFFSET + 103, LocType.Low_Rank, 0, ["A Kestodon Kerfuffle"]),
    "Bird-Brained Bandit": LocationData(LOCATION_ID_OFFSET + 201, LocType.Low_Rank, 2, ["The Great Jagras Hunt"]), # Progress 2
    # Level 2 Optional Quests
    "The Great Glutton": LocationData(LOCATION_ID_OFFSET + 251, LocType.Low_Rank, 2, ["The Great Jagras Hunt"]),
    "Camp Crasher": LocationData(LOCATION_ID_OFFSET + 252, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "The Pain from Gains": LocationData(LOCATION_ID_OFFSET + 262, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "Exterminator of the Waste": LocationData(LOCATION_ID_OFFSET + 263, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "Snatch the Snatcher": LocationData(LOCATION_ID_OFFSET + 261, LocType.Low_Rank, 2, ["The Great Glutton"]),
    # Level 3 Assigned Quests
    "Urgent: Pukei-Pukei Hunt": LocationData(LOCATION_ID_OFFSET + 205, LocType.Low_Rank, 2, ["Bird-Brained Bandit"]),
    "The Best Kind of Quest": LocationData(LOCATION_ID_OFFSET + 301, LocType.Low_Rank, 2, ["Urgent: Pukei-Pukei Hunt"]),  # Wildspire
    "Sinister Shadows in the Swamp": LocationData(LOCATION_ID_OFFSET + 302, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "Flying Sparks: Tobi-Kadachi": LocationData(LOCATION_ID_OFFSET + 305, LocType.Low_Rank, 2, ["Sinister Shadows in the Swamp"]),
    # Level 3 Optional Quests
    "Scatternut Shortage": LocationData(LOCATION_ID_OFFSET + 351, LocType.Low_Rank, 2, ["Urgent: Pukei-Pukei Hunt"]),
    "Flying Sparks: Tobi-Kadachi(Optional)": LocationData(LOCATION_ID_OFFSET + 352, LocType.Low_Rank, 2, ["Flying Sparks: Tobi-Kadachi"]),
    "Mired in the Spire": LocationData(LOCATION_ID_OFFSET + 361, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "The Piscine Problem": LocationData(LOCATION_ID_OFFSET + 362, LocType.Low_Rank, 2, ["Sinister Shadows in the Swamp"]),
    "Prickly Predicament": LocationData(LOCATION_ID_OFFSET + 363, LocType.Low_Rank, 2, ["Flying Sparks: Tobi-Kadachi"]),
    "Gettin' Yolked in the Waste": LocationData(LOCATION_ID_OFFSET + 364, LocType.Low_Rank, 2, ["Flying Sparks: Tobi-Kadachi"]),
    "The Current Situation": LocationData(LOCATION_ID_OFFSET + 353, LocType.Low_Rank, 2, ["Urgent: Pukei-Pukei Hunt"]),
    "Landing the Landslide Wyvern": LocationData(LOCATION_ID_OFFSET + 365, LocType.Low_Rank, 2, ["Snatch the Snatcher"]),
    # Level 4 Assigned Quests
    "The Encroaching Anjanath": LocationData(LOCATION_ID_OFFSET + 306, LocType.Low_Rank, 4, ["Flying Sparks: Tobi-Kadachi"]), # Progress 4
    "One for the History Books": LocationData(LOCATION_ID_OFFSET + 401, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Ballooning Problems": LocationData(LOCATION_ID_OFFSET + 405, LocType.Low_Rank, 4, ["One for the History Books"]),  # Coral Highlands
    "Radobaan Roadblock": LocationData(LOCATION_ID_OFFSET + 407, LocType.Low_Rank, 4, ["Ballooning Problems"]),  # Rotton Vale
    # Level 4 Optional Quests
    "One Helluva Sinus Infection": LocationData(LOCATION_ID_OFFSET + 451, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Gettin' Yolked in the Forest": LocationData(LOCATION_ID_OFFSET + 452, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Royal Relocation": LocationData(LOCATION_ID_OFFSET + 461, LocType.Low_Rank, 4, ["One for the History Books"]),
    "It's a Crying Shamos": LocationData(LOCATION_ID_OFFSET + 471, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "A Tzitzi for Science": LocationData(LOCATION_ID_OFFSET + 472, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "Sorry You're Not Invited": LocationData(LOCATION_ID_OFFSET + 473, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "What a Bunch of Abalone": LocationData(LOCATION_ID_OFFSET + 474, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "White Monster for a White Coat":
        LocationData(LOCATION_ID_OFFSET + 475, LocType.Low_Rank, 4, ["Ballooning Problems", "Landing the Landslide Wyvern"]),
    "Persistent Pests": LocationData(LOCATION_ID_OFFSET + 481, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "A Rotten Thing To Do": LocationData(LOCATION_ID_OFFSET + 482, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "A Bone to Pick": LocationData(LOCATION_ID_OFFSET + 483, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "On Nightmare's Wings": LocationData(LOCATION_ID_OFFSET + 484, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    # Level 5 Assigned Quests
    "Legiana: Embodiment of Elegance": LocationData(LOCATION_ID_OFFSET + 408, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "Into the Bowels of the Vale": LocationData(LOCATION_ID_OFFSET + 501, LocType.Low_Rank, 4, ["Legiana: Embodiment of Elegance"]),
    "A Fiery Throne Atop the Forest": LocationData(LOCATION_ID_OFFSET + 502, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    "Horned Tyrant Below the Sands": LocationData(LOCATION_ID_OFFSET + 503, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    # Level 5 Optional Quests
    "When Desire Becomes an Obsession": LocationData(LOCATION_ID_OFFSET + 551, LocType.Low_Rank, 4, ["A Fiery Throne Atop the Forest"]),
    "Redefining the 'Power Couple'": LocationData(LOCATION_ID_OFFSET + 552, LocType.Low_Rank, 4, ["A Fiery Throne Atop the Forest"]),
    "Twin Spires Upon the Sands": LocationData(LOCATION_ID_OFFSET + 561, LocType.Low_Rank, 4, ["Horned Tyrant Below the Sands"]),
    "A Humid Headache": LocationData(LOCATION_ID_OFFSET + 571, LocType.Low_Rank, 4, ["Legiana: Embodiment of Elegance"]),
    "Gone in a Flash": LocationData(LOCATION_ID_OFFSET + 572, LocType.Low_Rank, 4, ["Man's Best Friend"]),
    "Scratching the Itch": LocationData(LOCATION_ID_OFFSET + 581, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    "Man's Best Friend":
        LocationData(LOCATION_ID_OFFSET + 582, LocType.Low_Rank, 4, ["Into the Bowels of the Vale", "White Monster For A White Coat"]),
    "The Meat of the Matter": LocationData(LOCATION_ID_OFFSET + 583, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    # Level 6 Assigned Quests
    "A Colossal Task":
        LocationData(LOCATION_ID_OFFSET + 504, LocType.Low_Rank, 4, ["Horned Tyrant Below the Sands", "A Fiery Throne Atop The Forest"]), # Low Rank Goal
    "Invader In The Waste": LocationData(LOCATION_ID_OFFSET + 601, LocType.High_Rank, 5, ["A Colossal Task"]),  # Progress 5
    "Tickled Pink": LocationData(LOCATION_ID_OFFSET + 605, LocType.High_Rank, 5, ["Invader In The Waste"]),
    # Level 6 Optional Quests
    "Left Quite The Impression": LocationData(LOCATION_ID_OFFSET + 641, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Hard To Swallow": LocationData(LOCATION_ID_OFFSET + 651, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Googly-Eyed Green Monster": LocationData(LOCATION_ID_OFFSET + 652, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "A Hair-Raising Experience": LocationData(LOCATION_ID_OFFSET + 653, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "It Can't See You If You Don't Move": LocationData(LOCATION_ID_OFFSET + 654, LocType.High_Rank, 5, ["Tickled Pink"]),
    "The Sleeping Sylvan Queen": LocationData(LOCATION_ID_OFFSET + 655, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Stuck In Their Ways": LocationData(LOCATION_ID_OFFSET + 656, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Keep Your Hands To Yourself!": LocationData(LOCATION_ID_OFFSET + 661, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "A Crown Of Mud And Anger": LocationData(LOCATION_ID_OFFSET + 662, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Pukei-Pukei Ambush": LocationData(LOCATION_ID_OFFSET + 663, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Up To Your Waist In The Waste": LocationData(LOCATION_ID_OFFSET + 665, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Brown Desert, Green Queen": LocationData(LOCATION_ID_OFFSET + 666, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Tresspassing Troublemaker": LocationData(LOCATION_ID_OFFSET + 667, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Say Cheese!": LocationData(LOCATION_ID_OFFSET + 671, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Loop the Paolumu": LocationData(LOCATION_ID_OFFSET + 672, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Tingling Taste": LocationData(LOCATION_ID_OFFSET + 681, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Stuck in a Rut": LocationData(LOCATION_ID_OFFSET + 682, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Chef Quest! Pumped to Deliver": LocationData(LOCATION_ID_OFFSET + 683, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Chef Quest! A Rotten Request":
        LocationData(LOCATION_ID_OFFSET + 684, LocType.High_Rank, 5, ["Tickled Pink", "Chef Quest! Pumped to Deliver"]),
    "Chef Quest! Gajalaka Lockdown": LocationData(LOCATION_ID_OFFSET + 694, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "Dodogama Drama": LocationData(LOCATION_ID_OFFSET + 693, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "A Scalding Scoop": LocationData(LOCATION_ID_OFFSET + 692, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "A Meow for Help": LocationData(LOCATION_ID_OFFSET + 691, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    # Level 7 Assigned Quests
    "Old World Monster In The New World": LocationData(LOCATION_ID_OFFSET + 607, LocType.High_Rank, 6, ["Tickled Pink"]), # Progress 6, Elder Recess
    # Level 7 Optional Quests
    "A Cherry Wind Upon the Reefs": LocationData(LOCATION_ID_OFFSET + 771, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Pretty In Pink": LocationData(LOCATION_ID_OFFSET + 761, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "A Fiery Convergence": LocationData(LOCATION_ID_OFFSET + 795, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Ruler of the Azure Skies": LocationData(LOCATION_ID_OFFSET + 793, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Ore-eating Occupier": LocationData(LOCATION_ID_OFFSET + 792, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Lavasioth, Master of Magma": LocationData(LOCATION_ID_OFFSET + 791, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Legiana: Highlands Royalty": LocationData(LOCATION_ID_OFFSET + 772, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Well, That Diablos!": LocationData(LOCATION_ID_OFFSET + 762, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Rathalos in Blue": LocationData(LOCATION_ID_OFFSET + 752, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "The Red and Blue Crew": LocationData(LOCATION_ID_OFFSET + 753, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Two-horned Hostility": LocationData(LOCATION_ID_OFFSET + 763, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Talons of Ire and Ice": LocationData(LOCATION_ID_OFFSET + 774, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Odogaron Unleashed": LocationData(LOCATION_ID_OFFSET + 781, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "RRRRRumble in the Waste!": LocationData(LOCATION_ID_OFFSET + 764, LocType.High_Rank, 6, ["A Sore Site"]),
    "A Sore Site": LocationData(LOCATION_ID_OFFSET + 773, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Bazelgeuse in the Field of Fire": LocationData(LOCATION_ID_OFFSET + 794, LocType.High_Rank, 6, ["Man's Best Friend"]),
    # Level 8 Assigned Quests
    "A Wound and a Thirst": LocationData(LOCATION_ID_OFFSET + 701, LocType.High_Rank, 7, ["Old World Monster In The New World"]), # Progress 7
    "Kushala Daora, Dragon of Steel": LocationData(LOCATION_ID_OFFSET + 801, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Teostra the Infernal": LocationData(LOCATION_ID_OFFSET + 802, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Hellish Fiend Vaal Hazak": LocationData(LOCATION_ID_OFFSET + 803, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    # Level 8 Optional Quests
    "The Eater of Elders": LocationData(LOCATION_ID_OFFSET + 891, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Lightning Strikes Twice": LocationData(LOCATION_ID_OFFSET + 871, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Master of the Gale": LocationData(LOCATION_ID_OFFSET + 892, LocType.High_Rank, 7, ["Kushala Daora, Dragon of Steel"]),
    "Stirring from the Grave": LocationData(LOCATION_ID_OFFSET + 881, LocType.High_Rank, 7, ["Hellish Fiend Vaal Hazak"]),
    "The Winds of Wrath Bite Deep": LocationData(LOCATION_ID_OFFSET + 895, LocType.High_Rank, 7, ["Teostra the Infernal"]),
    "A Portent of Disaster": LocationData(LOCATION_ID_OFFSET + 851, LocType.High_Rank, 7, ["Kushala Daora, Dragon of Steel"]),
    "Hellfire's Stronghold": LocationData(LOCATION_ID_OFFSET + 893, LocType.High_Rank, 7, ["Teostra the Infernal"]),
    "A Blaze in the Sand": LocationData(LOCATION_ID_OFFSET + 861, LocType.High_Rank, 7, ["Teostra the Infernal"]),
    # High Rank Win Condition
    "Land of Convergence": LocationData(LOCATION_ID_OFFSET + 804, LocType.High_Rank, 7,
                                        ["Teostra the Infernal", "Kushala Daora, Dragon of Steel", "Teostra the Infernal"]), # High Rank Goal
    # Master Rank Start
    # MR 1 Assigned Quests
    "Baptism by Ice": LocationData(LOCATION_ID_OFFSET + 1101, LocType.Master_Rank, 8, ["Land of Convergence"]), # Progress 8
    "Banbaro Blockade": LocationData(LOCATION_ID_OFFSET + 1102, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    # MR 1 Optional Quests
    "Deep Snow Diver": LocationData(LOCATION_ID_OFFSET + 1121, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "Ice Catch!": LocationData(LOCATION_ID_OFFSET + 1123, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Taking Charge": LocationData(LOCATION_ID_OFFSET + 1122, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "Call of the Wild": LocationData(LOCATION_ID_OFFSET + 1124, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "The Great Jagras Returns!": LocationData(LOCATION_ID_OFFSET + 1151, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Literary Thief": LocationData(LOCATION_ID_OFFSET + 1154, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "New World Problems": LocationData(LOCATION_ID_OFFSET + 1152, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Beating Around the Bush": LocationData(LOCATION_ID_OFFSET + 1153, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Trapping the Tree Trasher": LocationData(LOCATION_ID_OFFSET + 1155, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Wildspire Treasure Hunt": LocationData(LOCATION_ID_OFFSET + 1161, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Taster's Tour": LocationData(LOCATION_ID_OFFSET + 1164, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Dragged Through the Mud": LocationData(LOCATION_ID_OFFSET + 1162, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Jyura in My Way": LocationData(LOCATION_ID_OFFSET + 1163, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "All the Wrong Signals": LocationData(LOCATION_ID_OFFSET + 1171, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Grinding My Girros": LocationData(LOCATION_ID_OFFSET + 1181, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Can't Bring Yourself To It": LocationData(LOCATION_ID_OFFSET + 1191, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "This Here's Big Horn Country!": LocationData(LOCATION_ID_OFFSET + 1192, LocType.Master_Rank, 8, ["Ready to Strike", "Ice Catch!"]),
    # MR 2 Assigned Quests
    "Ready to Strike": LocationData(LOCATION_ID_OFFSET + 1201, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "No Time for Naps": LocationData(LOCATION_ID_OFFSET + 1202, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Play Both Ends": LocationData(LOCATION_ID_OFFSET + 1203, LocType.Master_Rank, 8, ["Ready to Strike"]),
    # MR 2 Optional Quests
    "Analysis Creates Paralysis": LocationData(LOCATION_ID_OFFSET + 1221, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Poison and Paralysis Pinch": LocationData(LOCATION_ID_OFFSET + 1222, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Boaboa Constrictor": LocationData(LOCATION_ID_OFFSET + 1223, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "By Our Powers Combined": LocationData(LOCATION_ID_OFFSET + 1224, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "You Scratch Our Backs...": LocationData(LOCATION_ID_OFFSET + 1225, LocType.Master_Rank, 8, ["By Our Powers Combined"]),
    "Anjanath Antics": LocationData(LOCATION_ID_OFFSET + 1251, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Fool's Mate": LocationData(LOCATION_ID_OFFSET + 1252, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Nighty Night Nightshade": LocationData(LOCATION_ID_OFFSET + 1253, LocType.Master_Rank, 8, ["No Time for Naps", "Trapping the Tree Trasher"]),
    "Stick Your Nose Somewhere Else": LocationData(LOCATION_ID_OFFSET + 1263, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "A Queen At Heart": LocationData(LOCATION_ID_OFFSET + 1261, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "A Face Nightmares are Made Of": LocationData(LOCATION_ID_OFFSET + 1262, LocType.Master_Rank, 8, ["No Time for Naps"]),
    "Feisty Girl Talk": LocationData(LOCATION_ID_OFFSET + 1264, LocType.Master_Rank, 8, ["Pink Power Grab", "A Queen At Heart"]),
    "The Plight of Paolumu": LocationData(LOCATION_ID_OFFSET + 1271, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Pink Power Grab": LocationData(LOCATION_ID_OFFSET + 1272, LocType.Master_Rank, 8, ["Feisty Girl Talk"]),
    "Protip: Stay Hydrated": LocationData(LOCATION_ID_OFFSET + 1273, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "No Laughing Matter": LocationData(LOCATION_ID_OFFSET + 1281, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Bugger Off Bugs!": LocationData(LOCATION_ID_OFFSET + 1282, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Looking For That Glimmer": LocationData(LOCATION_ID_OFFSET + 1291, LocType.Master_Rank, 8, ["Ready to Strike", "Greetings from the Tundra"]),
    "Put That Red Cup Away": LocationData(LOCATION_ID_OFFSET + 1274, LocType.Master_Rank, 8, ["Feisty Girl Talk", "Poison and Paralysis Pinch"]), #Also need Waterproof Mantle
    # MR 3 Assigned Quests
    "Blizzard Blitz": LocationData(LOCATION_ID_OFFSET + 1301, LocType.Master_Rank, 10, ["No Time for Naps", "Play Both Ends"]), # Progress 10
    "Ever-present Shadow": LocationData(LOCATION_ID_OFFSET + 1302, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "The Scorching Blade": LocationData(LOCATION_ID_OFFSET + 1303, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Absolute Power": LocationData(LOCATION_ID_OFFSET + 1304, LocType.Master_Rank, 10, ["Ever-present Shadow", "The Scorching Blade"]),
    "A Smashing Cross Counter": LocationData(LOCATION_ID_OFFSET + 1305, LocType.Master_Rank, 10, ["Ever-present Shadow", "The Scorching Blade"]),
    "A Tale of Ice and Fire": LocationData(LOCATION_ID_OFFSET + 1306, LocType.Master_Rank, 10, ["A Smashing Cross Counter", "Absolute Power"]),
    # MR 3 Optional Quests
    "Remember That One Time?": LocationData(LOCATION_ID_OFFSET + 1321, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "The Purr-fect Room: Stone": LocationData(LOCATION_ID_OFFSET + 1322, LocType.Master_Rank, 10, ["Absolute Power"]),
    "Swoop to a New Low": LocationData(LOCATION_ID_OFFSET + 1351, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Nargacoulda, Should, Would": LocationData(LOCATION_ID_OFFSET + 1352, LocType.Master_Rank, 10, ["Ever-present Shadow"]),
    "The Secret to a Good Slice": LocationData(LOCATION_ID_OFFSET + 1353, LocType.Master_Rank, 10, ["The Scorching Blade"]),
    "Red and Black Aces": LocationData(LOCATION_ID_OFFSET + 1354, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Simmer and Slice": LocationData(LOCATION_ID_OFFSET + 1363, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),  # MR 11
    "Legiana Left Behind": LocationData(LOCATION_ID_OFFSET + 1371, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "The Black Wind": LocationData(LOCATION_ID_OFFSET + 1372, LocType.Master_Rank, 10, ["Ever-present Shadow"]),
    "Don't be a Jerk with the Jerky": LocationData(LOCATION_ID_OFFSET + 1381, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "A Roar that Shook the Vale": LocationData(LOCATION_ID_OFFSET + 1382, LocType.Master_Rank, 10, ["Absolute Power"]),
    "Runnin', Rollin', and Weepin'": LocationData(LOCATION_ID_OFFSET + 1383, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),  # MR 11 and Challenger
    "Everyone's a Critic": LocationData(LOCATION_ID_OFFSET + 1392, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Begone Uragaan": LocationData(LOCATION_ID_OFFSET + 1393, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Blast Warning In Effect!": LocationData(LOCATION_ID_OFFSET + 1391, LocType.Master_Rank, 10, ["A Smashing Cross Counter"]),
    "Secret of the Ooze": LocationData(LOCATION_ID_OFFSET + 1394, LocType.Master_Rank, 10, ["Ready to Strike", "A Smashing Cross Counter"]),  # Complete all deliveries
    "Festival of Explosions!": LocationData(LOCATION_ID_OFFSET + 1395, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),  # MR 11 & Fireproof mantle
    "Proud White Knight":
        LocationData(LOCATION_ID_OFFSET + 1323, LocType.Master_Rank, 10, ["Red and Black Aces", "Runnin', Rollin', and Weepin'", "Festival of Explosions!"]),  # MR 12 & Evasion Mantle as well
    "A Nasty Flesh Wound":
        LocationData(LOCATION_ID_OFFSET + 1373, LocType.Master_Rank, 10, ["Red and Black Aces", "Runnin', Rollin', and Weepin'", "Festival of Explosions!"]),  # MR 12 & Bandit Mantle as well
    # MR 4 Assigned Quests
    "When the Mist Taketh You": LocationData(LOCATION_ID_OFFSET + 1401, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),
    "The Thunderous Troublemaker": LocationData(LOCATION_ID_OFFSET + 1405, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "The Disintegrating Blade": LocationData(LOCATION_ID_OFFSET + 1402, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "Bad Friends, Great Enemies": LocationData(LOCATION_ID_OFFSET + 1403, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "The Defense of Seliana":
        LocationData(LOCATION_ID_OFFSET + 1404, LocType.Master_Rank, 10, ["The Disintegrating Blade", "Bad Friends, Great Enemies"]),
    # MR 4 Optional Quests
    "Noblefrost Hunter": LocationData(LOCATION_ID_OFFSET + 1421, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Tundra Troublemaker": LocationData(LOCATION_ID_OFFSET + 1422, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "Duet of Rime": LocationData(LOCATION_ID_OFFSET + 1423, LocType.Master_Rank, 10, ["The Defense of Seliana"]),  # MR 16 and Iceproof
    "Treasure in the Snow": LocationData(LOCATION_ID_OFFSET + 1424, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "These Azure Eyes See All": LocationData(LOCATION_ID_OFFSET + 1451, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Misfortune in the Forest": LocationData(LOCATION_ID_OFFSET + 1452, LocType.Master_Rank, 10, ["Bad Friends, Great Enemies"]),
    "In the Heat of the Moment": LocationData(LOCATION_ID_OFFSET + 1461, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "A Shadowy Offender": LocationData(LOCATION_ID_OFFSET + 1471, LocType.Master_Rank, 10, ["Bad Friends, Great Enemies"]),
    "This Corroded Blade": LocationData(LOCATION_ID_OFFSET + 1481, LocType.Master_Rank, 10, ["The Disintegrating Blade"]),
    "The Purr-fect Room: Light Iron":
        LocationData(LOCATION_ID_OFFSET + 1482, LocType.Master_Rank, 10, ["The Disintegrating Blade", "The Purr-fect Room: Stone"]),
    "The Purr-fect Room: Dark Iron": LocationData(LOCATION_ID_OFFSET + 1483, LocType.Master_Rank, 10, ["The Purr-fect Room: Light Iron"]),
    "Blue Rathalos Blues": LocationData(LOCATION_ID_OFFSET + 1491, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Trap the Thunder Jaw": LocationData(LOCATION_ID_OFFSET + 1492, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),  # Thunder mantle
    "Piercing Black": LocationData(LOCATION_ID_OFFSET + 1462, LocType.Master_Rank, 10, ["Duet of Rime", "Trap the Thunder Jaw"]),  # Also MR 17 and Rocksteady
    # "Treasure in the Steam": LocationData(LOCATION_ID_OFFSET + 1424, LocType.Master_Rank, ["Available from event start time?"]),
    # MR 5 Assigned Quests
    "The Iceborne Wyvern": LocationData(LOCATION_ID_OFFSET + 1501, LocType.Master_Rank, 11, ["The Defense of Seliana"]), # Progress 11
    "The Second Coming": LocationData(LOCATION_ID_OFFSET + 1502, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Under the Veil of Death": LocationData(LOCATION_ID_OFFSET + 1503, LocType.Master_Rank, 11, ["The Second Coming"]),
    "A Light from the Abyss": LocationData(LOCATION_ID_OFFSET + 1504, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    # MR 5 Optional Quests
    "Clashing Swords Upon The Rime": LocationData(LOCATION_ID_OFFSET + 1521, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Mark of the Sun": LocationData(LOCATION_ID_OFFSET + 1592, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Royal Audience on the Sand": LocationData(LOCATION_ID_OFFSET + 1561, LocType.Master_Rank, 11, ["Mark of the Sun"]),
    "Wings of the Wind": LocationData(LOCATION_ID_OFFSET + 1591, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "The Harbringer of Clear Skies": LocationData(LOCATION_ID_OFFSET + 1551, LocType.Master_Rank, 11, ["Wings of the Wind"]),
    "It's the Afterlife for Me": LocationData(LOCATION_ID_OFFSET + 1581, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    "Memories of the Sea God": LocationData(LOCATION_ID_OFFSET + 1572, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "Seething with Anger": LocationData(LOCATION_ID_OFFSET + 1593, LocType.Master_Rank, 11, ["The Second Coming"]),
    "The Tyrant's Banquet": LocationData(LOCATION_ID_OFFSET + 1562, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Lightning Crashes": LocationData(LOCATION_ID_OFFSET + 1571, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "The Purr-fect Room: Silver":
        LocationData(LOCATION_ID_OFFSET + 1594, LocType.Master_Rank, 11, ["The Iceborne Wyvern", "The Purr-fect Room: Light Iron"]),  # Actually only Light Iron
    "Here Comes the Deathmaker": LocationData(LOCATION_ID_OFFSET + 1552, LocType.Master_Rank, 11, ["Absolute Power", "Under the Veil of Death"]),  # Actually only Absolute
    # MR 6 Assigned Quests
    "To the Guided, A Paean": LocationData(LOCATION_ID_OFFSET + 1601, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "Paean of Guidance": LocationData(LOCATION_ID_OFFSET + 1602, LocType.Master_Rank, 11, ["To the Guided, A Paean"]),  # Master Rank Goal
}

arenaquest_database: Dict[str, LocationData] = {
    # Level 3
    "Special Arena: Pukei-Pukei": LocationData(LOCATION_ID_OFFSET + 331, LocType.Low_Rank, 2, ["One For The History Books"]),
    "Special Arena: Barroth": LocationData(LOCATION_ID_OFFSET + 332, LocType.Low_Rank, 2, ["Sinister Shadows In The Swamp"]),
    "Special Arena: Tobi-Kadachi": LocationData(LOCATION_ID_OFFSET + 333, LocType.Low_Rank, 2, ["The Encroaching Anjanath"]),
    # Level 4
    "Special Arena: Anjanath": LocationData(LOCATION_ID_OFFSET + 431, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Special Arena: Paolumu": LocationData(LOCATION_ID_OFFSET + 433, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "Special Arena: Radobaan": LocationData(LOCATION_ID_OFFSET + 434, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    # Level 5
    "Special Arena: Legiana": LocationData(LOCATION_ID_OFFSET + 531, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Special Arena: Odogaron":
        LocationData(LOCATION_ID_OFFSET + 532, LocType.Low_Rank, 4, ["Horned Tyrant Below The Sands", "A Fiery Throne Atop The Forest"]),
    "Special Arena: Rathalos":
        LocationData(LOCATION_ID_OFFSET + 533, LocType.Low_Rank, 4, ["Horned Tyrant Below The Sands", "A Fiery Throne Atop The Forest"]),
    "Special Arena: Diablos":
        LocationData(LOCATION_ID_OFFSET + 534, LocType.Low_Rank, 4, ["Horned Tyrant Below The Sands", "A Fiery Throne Atop The Forest"]),
    # Level 6
    "Special Arena: HR Pukei-Pukei": LocationData(LOCATION_ID_OFFSET + 631, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Special Arena: HR Barroth": LocationData(LOCATION_ID_OFFSET + 632, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Special Arena: HR Anjanath": LocationData(LOCATION_ID_OFFSET + 634, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Rathian": LocationData(LOCATION_ID_OFFSET + 635, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Tobi-Kadachi": LocationData(LOCATION_ID_OFFSET + 633, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Paolumu": LocationData(LOCATION_ID_OFFSET + 636, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Radobaan": LocationData(LOCATION_ID_OFFSET + 637, LocType.High_Rank, 5, ["Tickled Pink"]),
    # Level 7
    "Special Arena: HR Pink Rathian": LocationData(LOCATION_ID_OFFSET + 731, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Special Arena: HR Legiana": LocationData(LOCATION_ID_OFFSET + 732, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Odogaron": LocationData(LOCATION_ID_OFFSET + 733, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Azure Rathalos": LocationData(LOCATION_ID_OFFSET + 736, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Diablos": LocationData(LOCATION_ID_OFFSET + 737, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Black Diablos": LocationData(LOCATION_ID_OFFSET + 738, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Uragaan": LocationData(LOCATION_ID_OFFSET + 734, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Rathalos": LocationData(LOCATION_ID_OFFSET + 735, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    # MR 1
    "Special Arena: MR Pukei-Pukei": LocationData(LOCATION_ID_OFFSET + 1131, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Special Arena: MR Barroth": LocationData(LOCATION_ID_OFFSET + 1132, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Special Arena: MR Tobi-Kadachi": LocationData(LOCATION_ID_OFFSET + 1133, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Special Arena: MR Banbaro": LocationData(LOCATION_ID_OFFSET + 1134, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    # MR 2
    "Special Arena: MR Anjanath": LocationData(LOCATION_ID_OFFSET + 1231, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Radobaan": LocationData(LOCATION_ID_OFFSET + 1232, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Coral Pukei-Pukei": LocationData(LOCATION_ID_OFFSET + 1233, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Special Arena: MR Viper Tobi-Kadachi": LocationData(LOCATION_ID_OFFSET + 1234, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Rathian": LocationData(LOCATION_ID_OFFSET + 1235, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Pink Rathian": LocationData(LOCATION_ID_OFFSET + 1236, LocType.Master_Rank, 8, ["Pink Power Grab"]),
    "Special Arena: MR Paolumu": LocationData(LOCATION_ID_OFFSET + 1237, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Nightshade Paolumu": LocationData(LOCATION_ID_OFFSET + 1238, LocType.Master_Rank, 8, ["No Time for Naps"]),
    # MR 3
    "Special Arena: MR Legiana": LocationData(LOCATION_ID_OFFSET + 1331, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Odogaron": LocationData(LOCATION_ID_OFFSET + 1332, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Uragaan": LocationData(LOCATION_ID_OFFSET + 1333, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Rathalos": LocationData(LOCATION_ID_OFFSET + 1334, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Diablos": LocationData(LOCATION_ID_OFFSET + 1335, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Barioth": LocationData(LOCATION_ID_OFFSET + 1336, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Nargacuga": LocationData(LOCATION_ID_OFFSET + 1337, LocType.Master_Rank, 10, ["Ever-present Shadow"]),
    "Special Arena: MR Glavenus": LocationData(LOCATION_ID_OFFSET + 1338, LocType.Master_Rank, 10, ["The Scorching Blade"]),
    "Special Arena: MR Brachydios": LocationData(LOCATION_ID_OFFSET + 1339, LocType.Master_Rank, 10, ["A Smashing Cross Counter"]),
    "Special Arena: MR Tigrex": LocationData(LOCATION_ID_OFFSET + 1340, LocType.Master_Rank, 10, ["Absolute Power"]),
    # MR 4
    "Special Arena: MR Azure Rathalos": LocationData(LOCATION_ID_OFFSET + 1431, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Special Arena: MR Black Diablos": LocationData(LOCATION_ID_OFFSET + 1432, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Special Arena: MR Fulgur Anjanath": LocationData(LOCATION_ID_OFFSET + 1435, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "Special Arena: MR Acidic Glavenus": LocationData(LOCATION_ID_OFFSET + 1433, LocType.Master_Rank, 10, ["The Disintegrating Blade"]),
    "Special Arena: MR Ebony Odogaron": LocationData(LOCATION_ID_OFFSET + 1434, LocType.Master_Rank, 10, ["Bad Friends, Great Enemies"]),
}

specialquest_database: Dict[str, LocationData] = {
    "The Food Chain Dominator": LocationData(LOCATION_ID_OFFSET + 50701, LocType.High_Rank, 7, ["Old World Monster In The New World"]),
    "The Blazing Sun": LocationData(LOCATION_ID_OFFSET + 50801, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Pandora's Arena": LocationData(LOCATION_ID_OFFSET + 50802, LocType.Master_Rank, 8, ["The Blazing Sun"]),
    "No Remorse, No Surrender": LocationData(LOCATION_ID_OFFSET + 50803, LocType.Master_Rank, 8, ["Pandora's Arena"]),
    "A Visitor from Another World": LocationData(LOCATION_ID_OFFSET + 50601, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Legendary Beast": LocationData(LOCATION_ID_OFFSET + 50905, LocType.Master_Rank, 8, ["A Visitor from Another World"]),
    "He Taketh It With His Eyes": LocationData(LOCATION_ID_OFFSET + 50906, LocType.Master_Rank, 8, ["The Legendary Beast"]),
    "Contract: Trouble in the Ancient Forest": LocationData(LOCATION_ID_OFFSET + 50910, LocType.Master_Rank, 8, ["Land of Convergence"]),
    # Tools
    "Temporal Mantle": LocationData(LOCATION_ID_OFFSET + 1, LocType.Low_Rank.Tool, 8, ["No Remorse, No Surrender"]), # Requires Special
    # "Temporal Mantle+": LocationData(LOCATION_ID_OFFSET + 21, LocType.Master_Rank, 11, ["Divine Surge"]), Post game content
    "Dragonproof Mantle": LocationData(LOCATION_ID_OFFSET + 10, LocType.High_Rank.Tool, 7, ["The Food Chain Dominator"]),  # Requires Special Quests
    "Dragonproof Mantle+": LocationData(LOCATION_ID_OFFSET + 30, LocType.Master_Rank.Tool, 11, ["Royal Audience on the Sand", "The Harbringer of Clear Skies"]),  # Requires craft of teostra and daora
}

eventquest_database: Dict[str, LocationData] = {
    # Level 2
    "Up at the Crack of Dawn": LocationData(LOCATION_ID_OFFSET + 61101, LocType.Low_Rank, 2, ["A Kestodon Kerfuffle"]),
    "Chew the Fat": LocationData(LOCATION_ID_OFFSET + 66101, LocType.Low_Rank, 2, ["The Great Jagras Hunt"]),
    # Level 3
    "USJ: Gold Star Treatment": LocationData(LOCATION_ID_OFFSET + 67106, LocType.Low_Rank, 2, ["Sinister Shadows In The Swamp"]),
    "Where Sun Meets Moon": LocationData(LOCATION_ID_OFFSET + 61103, LocType.Low_Rank, 2, ["Sinister Shadows In The Swamp"]),
    # Level 4
    "Greeting the Gluttons": LocationData(LOCATION_ID_OFFSET + 66106, LocType.Low_Rank, 4, ["One For The History Books"]),
    "Ya-Ku With That?": LocationData(LOCATION_ID_OFFSET + 66102, LocType.Low_Rank, 4, ["One For The History Books"]),
    "Timberland Troublemakers": LocationData(LOCATION_ID_OFFSET + 61104, LocType.Low_Rank, 4, ["One For The History Books"]),
    # Level 5
    "Fleshed Cleaved to Bone": LocationData(LOCATION_ID_OFFSET + 66103, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Every Hunter's Dream": LocationData(LOCATION_ID_OFFSET + 61105, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "The Poison Posse": LocationData(LOCATION_ID_OFFSET + 66105, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Kirin the Myth": LocationData(LOCATION_ID_OFFSET + 66104, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Wicked Wildspire Warfare": LocationData(LOCATION_ID_OFFSET + 64101, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    # Level 6
    "Triple Threat Throwdown": LocationData(LOCATION_ID_OFFSET + 65605, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "Wiggle Me This": LocationData(LOCATION_ID_OFFSET + 65604, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Egg Lovers United": LocationData(LOCATION_ID_OFFSET + 65603, LocType.High_Rank, 5, ["A Colossal Task"]),
    "A Flash in the Pan": LocationData(LOCATION_ID_OFFSET + 65602, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Scrapping with the Shamos": LocationData(LOCATION_ID_OFFSET + 65601, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Gaze Upon the Dawn": LocationData(LOCATION_ID_OFFSET + 62608, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Mosswinin' and Dinin'": LocationData(LOCATION_ID_OFFSET + 61605, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Midnight Mayhem": LocationData(LOCATION_ID_OFFSET + 61601, LocType.High_Rank, 5, ["A Colossal Task"]),
    # Level 7
    "USJ Blazing Azure Stars!": LocationData(LOCATION_ID_OFFSET + 67604, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "A Rush of Blood": LocationData(LOCATION_ID_OFFSET + 67103, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Coral Waltz": LocationData(LOCATION_ID_OFFSET + 66603, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Wildspire Bolero": LocationData(LOCATION_ID_OFFSET + 66602, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Kings Know No Fear": LocationData(LOCATION_ID_OFFSET + 61604, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "A Royal Pain": LocationData(LOCATION_ID_OFFSET + 61603, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "This Is How Revolts Start": LocationData(LOCATION_ID_OFFSET + 66606, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Rock N' Roll Recess": LocationData(LOCATION_ID_OFFSET + 66605, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Rollin' With The Uragaan": LocationData(LOCATION_ID_OFFSET + 64601, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Effluvial Opera": LocationData(LOCATION_ID_OFFSET + 66604, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Deep Green Blues": LocationData(LOCATION_ID_OFFSET + 66601, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    # Level 8
    "Code: Red": LocationData(LOCATION_ID_OFFSET + 67605, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    # Level 9
    "Keeper of the Otherworld": LocationData(LOCATION_ID_OFFSET + 62609, LocType.Master_Rank, 8, ["Land of Convergence"]),
    # The following require high amount of HR, may disable or subcategorize
    "A Simple Task": LocationData(LOCATION_ID_OFFSET + 65606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Nose for an Eye": LocationData(LOCATION_ID_OFFSET + 66608, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "No Tomorrow for Usurpers": LocationData(LOCATION_ID_OFFSET + 66609, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Heralds of Destruction City": LocationData(LOCATION_ID_OFFSET + 62506, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "When Blue Dust Surpasses Red Lust": LocationData(LOCATION_ID_OFFSET + 62511, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Snow & Cherry Blossoms": LocationData(LOCATION_ID_OFFSET + 66607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Deathly Quiet Curtain": LocationData(LOCATION_ID_OFFSET + 62502, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Whisper of White Mane": LocationData(LOCATION_ID_OFFSET + 62503, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Relish the Moment": LocationData(LOCATION_ID_OFFSET + 62515, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Greatest Jagras": LocationData(LOCATION_ID_OFFSET + 61606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Name's Lavasioth": LocationData(LOCATION_ID_OFFSET + 61607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Scorn of the Sun": LocationData(LOCATION_ID_OFFSET + 62504, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Eye of the Storm": LocationData(LOCATION_ID_OFFSET + 62505, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Undying Alpenglow": LocationData(LOCATION_ID_OFFSET + 62606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Like a Moth to the Flame": LocationData(LOCATION_ID_OFFSET + 62607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Thronetaker": LocationData(LOCATION_ID_OFFSET + 66610, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Tracking the Delivery": LocationData(LOCATION_ID_OFFSET + 65607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Visitor from Eorzea (LOCATION_ID_OFFSET + Extreme)": LocationData(LOCATION_ID_OFFSET + 67606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Contract: Woodland Spirit": LocationData(LOCATION_ID_OFFSET + 67610, LocType.Master_Rank, 8, ["Land of Convergence"]),
    # MR 1
    "Fetching Light Pearls": LocationData(LOCATION_ID_OFFSET + 66853, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "A Fish to Whet Your Appetite": LocationData(LOCATION_ID_OFFSET + 61816, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Skyward Snipers": LocationData(LOCATION_ID_OFFSET + 61815, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Flora Frostbite": LocationData(LOCATION_ID_OFFSET + 61811, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "Duffel Duty": LocationData(LOCATION_ID_OFFSET + 61805, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "A Bunch of Sticks in the Mud": LocationData(LOCATION_ID_OFFSET + 66803, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Desert Desserts": LocationData(LOCATION_ID_OFFSET + 66804, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Trophy Fishin'": LocationData(LOCATION_ID_OFFSET + 66801, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Pearl Snatchers": LocationData(LOCATION_ID_OFFSET + 61801, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "The Lord of the Underworld Beckons": LocationData(LOCATION_ID_OFFSET + 66802, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    # MR 2
    "Paolumu Lullabies": LocationData(LOCATION_ID_OFFSET + 61809, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Kadachi Twins": LocationData(LOCATION_ID_OFFSET + 66862, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Camoflawed": LocationData(LOCATION_ID_OFFSET + 66854, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Every Hunter's Dream II": LocationData(LOCATION_ID_OFFSET + 61802, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Ballon Fight": LocationData(LOCATION_ID_OFFSET + 64801, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Colorful Carnival": LocationData(LOCATION_ID_OFFSET + 66806, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "A New Troublemaker in Town": LocationData(LOCATION_ID_OFFSET + 66805, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Hunter-Blunder": LocationData(LOCATION_ID_OFFSET + 66807, LocType.Master_Rank, 8, ["Ready to Strike"]),
    # MR 3
    "Seeing is Believing": LocationData(LOCATION_ID_OFFSET + 66855, LocType.Master_Rank, 10, ["Absolute Power"]),
    "When the Swift Meets the Roar": LocationData(LOCATION_ID_OFFSET + 66834, LocType.Master_Rank, 10, ["Absolute Power"]),
    "50 Shades of White": LocationData(LOCATION_ID_OFFSET + 61813, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Every Hunter's Dream III": LocationData(LOCATION_ID_OFFSET + 61803, LocType.Master_Rank, 10, ["Absolute Power"]),
    "Fired-Up Bruisers": LocationData(LOCATION_ID_OFFSET + 66811, LocType.Master_Rank, 10, ["Absolute Power"]),
    "A Curious Experiment": LocationData(LOCATION_ID_OFFSET + 66809, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Soaked and Shivering": LocationData(LOCATION_ID_OFFSET + 66810, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "A Sky & Sea of Fire": LocationData(LOCATION_ID_OFFSET + 66808, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    # MR 4
    "Beef is Never a Mi-steak": LocationData(LOCATION_ID_OFFSET + 61812, LocType.Master_Rank, 10, ["The Defense of Seliana"]),
    "Servants of the Vale": LocationData(LOCATION_ID_OFFSET + 66814, LocType.Master_Rank, 10, ["The Defense of Seliana"]),
    "The Desert Dash": LocationData(LOCATION_ID_OFFSET + 66812, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "In the Depths of the Forest": LocationData(LOCATION_ID_OFFSET + 66813, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    # MR 5
    "Scores of Ores": LocationData(LOCATION_ID_OFFSET + 61806, LocType.Master_Rank, 11, ["The Defense of Seliana"]),
    "A Chilling Entrance": LocationData(LOCATION_ID_OFFSET + 61807, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    "RE: Return of the Bioweapon": LocationData(LOCATION_ID_OFFSET + 67801, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    "A Reason Behind The Hunger": LocationData(LOCATION_ID_OFFSET + 66817, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "The Winter Blues": LocationData(LOCATION_ID_OFFSET + 66816, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "We Three Kings": LocationData(LOCATION_ID_OFFSET + 66815, LocType.Master_Rank, 11, ["The Second Coming"]),
    "Talk About a Party Foul...": LocationData(LOCATION_ID_OFFSET + 66859, LocType.Master_Rank, 11, ["The Second Coming"]),
    "Old Dog, New Trick": LocationData(LOCATION_ID_OFFSET + 66867, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
}

grindy_database: Dict[str, LocationData] = {
    "A Light Upon the River's Gloom": LocationData(LOCATION_ID_OFFSET + 991, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Showdown: the Muck and the Maul": LocationData(LOCATION_ID_OFFSET + 996, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "New World Sky, New World Flower": LocationData(LOCATION_ID_OFFSET + 997, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Summons from Below": LocationData(LOCATION_ID_OFFSET + 998, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The White Winds of the New World": LocationData(LOCATION_ID_OFFSET + 992, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Sapphire Star's Guidance": LocationData(LOCATION_ID_OFFSET + 995, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Beyond the Blasting Scales": LocationData(LOCATION_ID_OFFSET + 961, LocType.Master_Rank, 8, ["Land of Convergence"]),  # Also 805?
    "Thunderous Rumble in the Highlands": LocationData(LOCATION_ID_OFFSET + 971, LocType.Master_Rank, 8, ["Land of Convergence"]), # Also 806?
    # Tools
    "Rocksteady Mantle": LocationData(LOCATION_ID_OFFSET + 3, LocType.Master_Rank.Tool, 8, ["A Summons from Below"]), # Requires Grindy
    "Rocksteady Mantle+": LocationData(LOCATION_ID_OFFSET + 23, LocType.Master_Rank.Tool, 10, ["Piercing Black"]),
    "Evasion Mantle": LocationData(LOCATION_ID_OFFSET + 13, LocType.Master_Rank.Tool, 8, ["New World Sky, New World Flower"]),  # Requires Grindy
    "Evasion Mantle+": LocationData(LOCATION_ID_OFFSET + 33, LocType.Master_Rank.Tool, 10, ["Proud White Knight"]),
    "Impact Mantle": LocationData(LOCATION_ID_OFFSET + 14, LocType.Master_Rank.Tool, 8, ["Showdown: the Muck and the Maul"]),  # Requires Grindy
    "Immunity Mantle+": LocationData(LOCATION_ID_OFFSET + 36, LocType.Master_Rank, 11, ["It's the Afterlife for Me"]),
}

endemiclife_database: Dict[str, LocationData] = {
    # Wildspire 2
    # Coral and Rotten 4
    # Elder 6
    # Iceborne 8
    # Terrestial Life
    "Shepard Hare": LocationData(ENDEMIC_ID_OFFSET + 8, LocType.Normal_Life, 0),
    "Pilot Hare": LocationData(ENDEMIC_ID_OFFSET + 9, LocType.Rare_Life, 0),
    "Forest Gecko": LocationData(ENDEMIC_ID_OFFSET + 40, LocType.Normal_Life, 0),
    "Wildspire Gecko": LocationData(ENDEMIC_ID_OFFSET + 41, LocType.Normal_Life, 2),
    "Gloom Gecko": LocationData(ENDEMIC_ID_OFFSET + 42, LocType.Normal_Life, 4),
    "Moonlight Gecko": LocationData(ENDEMIC_ID_OFFSET + 43, LocType.Rare_Life, 4),
    "Vaporonid": LocationData(ENDEMIC_ID_OFFSET + 48, LocType.Normal_Life, 0),
    "Scavantula": LocationData(ENDEMIC_ID_OFFSET + 49, LocType.Normal_Life, 4),
    "Revolture": LocationData(ENDEMIC_ID_OFFSET + 56, LocType.Normal_Life, 0),
    "Blissbill": LocationData(ENDEMIC_ID_OFFSET + 57, LocType.Normal_Life, 0),
    "Dung Beetle": LocationData(ENDEMIC_ID_OFFSET + 80, LocType.Normal_Life, 2),
    "Bomb Beetle": LocationData(ENDEMIC_ID_OFFSET + 81, LocType.Normal_Life, 6),
    "Paratoad": LocationData(ENDEMIC_ID_OFFSET + 144, LocType.Normal_Life, 0),
    "Sleeptoad": LocationData(ENDEMIC_ID_OFFSET + 145, LocType.Normal_Life, 4),
    "Nitrotoad": LocationData(ENDEMIC_ID_OFFSET + 147, LocType.Normal_Life, 6),
    "Wiggler": LocationData(ENDEMIC_ID_OFFSET + 152, LocType.Normal_Life, 4),
    "Wiggler Queen": LocationData(ENDEMIC_ID_OFFSET + 153, LocType.Rare_Life, 4),
    "Carrier Ant": LocationData(ENDEMIC_ID_OFFSET + 176, LocType.Normal_Life, 0),
    "Emperor Hopper": LocationData(ENDEMIC_ID_OFFSET + 192, LocType.Normal_Life, 0),
    "Tyrant Hopper": LocationData(ENDEMIC_ID_OFFSET + 193, LocType.Normal_Life, 4),
    "Iron Helmcrab": LocationData(ENDEMIC_ID_OFFSET + 248, LocType.Normal_Life, 2),
    "Soldier Helmcrab": LocationData(ENDEMIC_ID_OFFSET + 249, LocType.Normal_Life, 4),
    "Emerald Helmcrab": LocationData(ENDEMIC_ID_OFFSET + 250, LocType.Rare_Life, 2),
    # Need to implement Kulve Taroth
    # "Gold Helmcrab": LocationData(ENDEMIC_ID_OFFSET + 251, LocType.Normal_Life.Event_Quest, 8),
    # "Shiny Gold Helmcrab": LocationData(ENDEMIC_ID_OFFSET + 252, LocType.Rare_Life.Event_Quest, 8),
    # "Copper Calappa": LocationData(ENDEMIC_ID_OFFSET + 328, LocType.Normal_Life.Event_Quest, 8),
    # "Gold Calappa": LocationData(ENDEMIC_ID_OFFSET + 329, LocType.Rare_Life.Event_Quest, 8),
    # "Tsuchinoko": LocationData(ENDEMIC_ID_OFFSET + 58, LocType.Normal_Life.Event_Quest, 8),
    "Stonebill": LocationData(ENDEMIC_ID_OFFSET + 58, LocType.Normal_Life, 8),
    "Rime Beetle": LocationData(ENDEMIC_ID_OFFSET + 82, LocType.Normal_Life, 8),
    "Pearlspring Macaque": LocationData(ENDEMIC_ID_OFFSET + 400, LocType.Normal_Life, 8),
    "Goldspring Macaque": LocationData(ENDEMIC_ID_OFFSET + 401, LocType.Legendary_Life, 8),
    "Crowned Prawn": LocationData(ENDEMIC_ID_OFFSET + 408, LocType.Normal_Life, 8),
    "Duffel Penguin": LocationData(ENDEMIC_ID_OFFSET + 424, LocType.Normal_Life, 8),
    "Arrowhead Gecko": LocationData(ENDEMIC_ID_OFFSET + 432, LocType.Legendary_Life, 8),
    # Aquatic Life
    "Climbing Joyperch": LocationData(ENDEMIC_ID_OFFSET + 32, LocType.Normal_Life, 0),
    "Pink Parexus": LocationData(ENDEMIC_ID_OFFSET + 88, LocType.Normal_Life, 0),
    "Burst Arowana": LocationData(ENDEMIC_ID_OFFSET + 96, LocType.Normal_Life, 0),
    "Bomb Arowana": LocationData(ENDEMIC_ID_OFFSET + 97, LocType.Normal_Life, 0),
    "Andangler": LocationData(ENDEMIC_ID_OFFSET + 112, LocType.Normal_Life, 4),
    "Hopguppy": LocationData(ENDEMIC_ID_OFFSET + 128, LocType.Normal_Life, 0),
    "Petricanths": LocationData(ENDEMIC_ID_OFFSET + 136, LocType.Legendary_Life, 4),
    "Whetfish": LocationData(ENDEMIC_ID_OFFSET + 264, LocType.Normal_Life, 0),
    "Gastronome Tuna": LocationData(ENDEMIC_ID_OFFSET + 272, LocType.Normal_Life, 0),
    "King Marlin": LocationData(ENDEMIC_ID_OFFSET + 280, LocType.Legendary_Life, 0),
    "Goldenfish": LocationData(ENDEMIC_ID_OFFSET + 296, LocType.Normal_Life, 2),
    "Platinumfish": LocationData(ENDEMIC_ID_OFFSET + 297, LocType.Normal_Life, 6),
    "Goldenfry": LocationData(ENDEMIC_ID_OFFSET + 304, LocType.Normal_Life, 0),
    "Sushifish": LocationData(ENDEMIC_ID_OFFSET + 312, LocType.Normal_Life, 0),
    "Gunpowderfish": LocationData(ENDEMIC_ID_OFFSET + 320, LocType.Normal_Life, 4),
    "Sealord's Crestfish": LocationData(ENDEMIC_ID_OFFSET + 448, LocType.Legendary_Life, 8),
    "Glass Parexus": LocationData(ENDEMIC_ID_OFFSET + 456, LocType.Normal_Life, 8),
    # Airborne Life
    "Cobalt Flutterfly": LocationData(ENDEMIC_ID_OFFSET + 24, LocType.Normal_Life, 0),
    "Phantom Flutterfly": LocationData(ENDEMIC_ID_OFFSET + 25, LocType.Rare_Life, 0),
    "Omenfly": LocationData(ENDEMIC_ID_OFFSET + 64, LocType.Normal_Life, 0),
    "Augurfly": LocationData(ENDEMIC_ID_OFFSET + 65, LocType.Rare_Life, 0),
    "Scalebat": LocationData(ENDEMIC_ID_OFFSET + 72, LocType.Normal_Life, 0),
    # Kulve Taroth
    # "Gold Scalebat": LocationData(ENDEMIC_ID_OFFSET + 73, LocType.Normal_Life.Event_Quest, 8),
    "Elegant Coralbird": LocationData(ENDEMIC_ID_OFFSET + 104, LocType.Normal_Life, 4),
    "Dapper Coralbird": LocationData(ENDEMIC_ID_OFFSET + 105, LocType.Rare_Life, 4),
    "Vigorwasp": LocationData(ENDEMIC_ID_OFFSET + 160, LocType.Normal_Life, 0),
    "Giant Vigorwasp": LocationData(ENDEMIC_ID_OFFSET + 161, LocType.Normal_Life, 0),
    "Flying Meduso": LocationData(ENDEMIC_ID_OFFSET + 168, LocType.Normal_Life, 4),
    "Flashfly": LocationData(ENDEMIC_ID_OFFSET + 200, LocType.Normal_Life, 0),
    "Grandfather Mantagrell": LocationData(ENDEMIC_ID_OFFSET + 240, LocType.Normal_Life, 4),
    "Moon Slug": LocationData(ENDEMIC_ID_OFFSET + 52, LocType.Normal_Life, 8),
    # Treetop Life
    "Woodland Pteryx": LocationData(ENDEMIC_ID_OFFSET + 16, LocType.Normal_Life, 0),
    "Forest Pteryx": LocationData(ENDEMIC_ID_OFFSET + 17, LocType.Rare_Life, 0),
    "Hercudrome": LocationData(ENDEMIC_ID_OFFSET + 184, LocType.Normal_Life, 0),
    "Gold Hercudrome": LocationData(ENDEMIC_ID_OFFSET + 185, LocType.Rare_Life, 0),
    "Prism Hercudrome": LocationData(ENDEMIC_ID_OFFSET + 186, LocType.Rare_Life, 0),
    "Blue Diva": LocationData(ENDEMIC_ID_OFFSET + 440, LocType.Legendary_Life, 8),
    # Unclassified Life
    "Downy Crake": LocationData(ENDEMIC_ID_OFFSET + 120, LocType.Legendary_Life, 0),
    "Bristly Crake": LocationData(ENDEMIC_ID_OFFSET + 121, LocType.Legendary_Life, 4),
    "Cactuar": LocationData(ENDEMIC_ID_OFFSET + 344, LocType.Rare_Life, 2),
    "Cactuar Cutting": LocationData(ENDEMIC_ID_OFFSET + 345, LocType.Rare_Life, 2),
    "Flowering Cactuar Cutting": LocationData(ENDEMIC_ID_OFFSET + 346, LocType.Legendary_Life, 2),
    # Nekker
    "Wintermoon Nettle": LocationData(ENDEMIC_ID_OFFSET + 464, LocType.Legendary_Life, 8),
    # The Molys are in Guiding lands
}

specializedtools_database: Dict[str, LocationData] = {
    "Ghillie Mantle": LocationData(LOCATION_ID_OFFSET + 0, LocType.Low_Rank, 2, ["Sinister Shadows in the Swamps"]),
    "Health Booster": LocationData(LOCATION_ID_OFFSET + 2, LocType.Low_Rank, 4, ["One for the History Books"]),
    "Challenger Mantle": LocationData(LOCATION_ID_OFFSET + 4, LocType.High_Rank, 6, ["The Red and Blue Crew"]),
    "Vitality Mantle": LocationData(LOCATION_ID_OFFSET + 5, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    "Fireproof Mantle": LocationData(LOCATION_ID_OFFSET + 6, LocType.High_Rank, 6, ["A Fiery Convergence"]),
    "Waterproof Mantle": LocationData(LOCATION_ID_OFFSET + 7, LocType.High_Rank, 5, ["Up to Your Waist in the Waste"]),
    "Iceproof Mantle": LocationData(LOCATION_ID_OFFSET + 8, LocType.High_Rank, 5, ["Loop the Paolumu"]),
    "Thunderproof Mantle": LocationData(LOCATION_ID_OFFSET + 9, LocType.Low_Rank, 4, ["Gone in a Flash"]),
    "Cleanser Booster": LocationData(LOCATION_ID_OFFSET + 11, LocType.Low_Rank, 4, ["On Nightmare's Wings"]),
    "Glider Mantle": LocationData(LOCATION_ID_OFFSET + 12, LocType.Low_Rank, 4),
    "Apothecary Mantle": LocationData(LOCATION_ID_OFFSET + 15, LocType.High_Rank, 7, ["A Portent of Disaster"]),
    "Immunity Mantle": LocationData(LOCATION_ID_OFFSET + 16, LocType.High_Rank, 7, ["A Blaze on the Sand"]),
    "Affinity Booster": LocationData(LOCATION_ID_OFFSET + 17, LocType.High_Rank, 6, ["RRRRRumble in the Waste!"]),
    "Bandit Mantle": LocationData(LOCATION_ID_OFFSET + 18, LocType.High_Rank, 4, ["Redefining the Power Couple"]),
    # Upgrades
    "Ghillie Mantle+": LocationData(LOCATION_ID_OFFSET + 20, LocType.Master_Rank, 8, ["Ice Catch"]),
    "Health Booster+": LocationData(LOCATION_ID_OFFSET + 22, LocType.Master_Rank, 8, ["Feisty Girl Talk"]),
    "Challenger Mantle+": LocationData(LOCATION_ID_OFFSET + 24, LocType.Master_Rank, 10, ["Runnin', Rollin', and Weepin'"]),
    "Vitality Mantle+": LocationData(LOCATION_ID_OFFSET + 25, LocType.Master_Rank, 8, ["This Here's Big Horn Country"]),
    "Fireproof Mantle+": LocationData(LOCATION_ID_OFFSET + 26, LocType.Master_Rank, 10, ["Festival of Explosions!"]),
    "Waterproof Mantle+": LocationData(LOCATION_ID_OFFSET + 27, LocType.Master_Rank, 8, ["Put That Red Cup Away"]),
    "Iceproof Mantle+": LocationData(LOCATION_ID_OFFSET + 28, LocType.Master_Rank, 10, ["Duet of Rime"]),
    "Thunderproof Mantle+": LocationData(LOCATION_ID_OFFSET + 29, LocType.Master_Rank, 10, ["Trap the Thunder Jaw"]),
    "Cleanser Booster+": LocationData(LOCATION_ID_OFFSET + 31, LocType.Master_Rank, 8, ["Poison and Paralysis Pinch"]),
    "Glider Mantle+": LocationData(LOCATION_ID_OFFSET + 32, LocType.Master_Rank, 10, ["Red and Black Aces"]),
    # "Impact Mantle+": LocationData(LOCATION_ID_OFFSET + 34, LocType.Master_Rank, 11, ["Hymn of Moon and Sun"]), Post game content
    "Apothecary Mantle+": LocationData(LOCATION_ID_OFFSET + 35, LocType.Master_Rank, 11, ["The Tyrant's Banquet"]),
    # "Affinity Booster+": LocationData(LOCATION_ID_OFFSET + 37, LocType.Master_Rank, 2, ["The Storm Brings the Unexpected"]), Post game content
    "Bandit Mantle+": LocationData(LOCATION_ID_OFFSET + 38, LocType.Master_Rank, 10, ["A Nasty Flesh Wound"]),
}

masterlocations_database: typing.Dict[str, LocationData] = {
    **quest_database,
    **arenaquest_database,
    **specialquest_database,
    **eventquest_database,
    **endemiclife_database,
    **grindy_database,
    **specializedtools_database,
}


da_list = []
for key, location_data in masterlocations_database.items():
    if location_data.code in da_list:
        print(f"name = {key}, id = {location_data.code}")
    else:
        da_list.append(location_data.code)



