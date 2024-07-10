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


class LocationData(typing.NamedTuple):
    code: typing.Optional[int]
    loc_type: LocType
    zone: int
    required_quest: List[str] = None


# Multi Cursor with alt click
quest_database: Dict[str, LocationData] = {
    # Level 1 Quests
    "Jagras of the Ancient Forest": LocationData(101, LocType.Low_Rank, 0),
    "Learning to Clutch": LocationData(241, LocType.Low_Rank, 0),
    "Butting Heads With Nature": LocationData(151, LocType.Low_Rank, 0, ["A Kestodon Kerfuffle"]),
    "A Thicket of Thugs": LocationData(152, LocType.Low_Rank, 0, ["Jagras of the Ancient Forest"]),
    "Fungal Flexin' in the Ancient Forest": LocationData(153, LocType.Low_Rank, 0, ["Jagras of the Ancient Forest"]),
    # Level 2 Assigned Quests
    "A Kestodon Kerfuffle": LocationData(102, LocType.Low_Rank, 0, ["Jagras of the Ancient Forest"]),
    "The Great Jagras Hunt": LocationData(103, LocType.Low_Rank, 0, ["A Kestodon Kerfuffle"]),
    "Bird-Brained Bandit": LocationData(201, LocType.Low_Rank, 2, ["The Great Jagras Hunt"]), # Progress 2
    # Level 2 Optional Quests
    "The Great Glutton": LocationData(251, LocType.Low_Rank, 2, ["The Great Jagras Hunt"]),
    "Camp Crasher": LocationData(252, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "The Pain from Gains": LocationData(262, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "Exterminator of the Waste": LocationData(263, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "Snatch the Snatcher": LocationData(261, LocType.Low_Rank, 2, ["The Great Glutton"]),
    # Level 3 Assigned Quests
    "Urgent: Pukei-Pukei Hunt": LocationData(205, LocType.Low_Rank, 2, ["Bird-Brained Bandit"]),
    "The Best Kind of Quest": LocationData(301, LocType.Low_Rank, 2, ["Urgent: Pukei-Pukei Hunt"]),  # Wildspire
    "Sinister Shadows in the Swamp": LocationData(302, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "Flying Sparks: Tobi-Kadachi": LocationData(305, LocType.Low_Rank, 2, ["Sinister Shadows in the Swamp"]),
    # Level 3 Optional Quests
    "Scatternut Shortage": LocationData(351, LocType.Low_Rank, 2, ["Urgent: Pukei-Pukei Hunt"]),
    "Flying Sparks: Tobi-Kadachi(Optional)": LocationData(352, LocType.Low_Rank, 2, ["Flying Sparks: Tobi-Kadachi"]),
    "Mired in the Spire": LocationData(361, LocType.Low_Rank, 2, ["The Best Kind of Quest"]),
    "The Piscine Problem": LocationData(362, LocType.Low_Rank, 2, ["Sinister Shadows in the Swamp"]),
    "Prickly Predicament": LocationData(363, LocType.Low_Rank, 2, ["Flying Sparks: Tobi-Kadachi"]),
    "Gettin' Yolked in the Waste": LocationData(364, LocType.Low_Rank, 2, ["Flying Sparks: Tobi-Kadachi"]),
    "The Current Situation": LocationData(353, LocType.Low_Rank, 2, ["Urgent: Pukei-Pukei Hunt"]),
    # Level 4 Assigned Quests
    "The Encroaching Anjanath": LocationData(306, LocType.Low_Rank, 4, ["Flying Sparks: Tobi-Kadachi"]), # Progress 4
    "One for the History Books": LocationData(401, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Ballooning Problems": LocationData(405, LocType.Low_Rank, 4, ["One for the History Books"]),  # Coral Highlands
    "Radobaan Roadblock": LocationData(407, LocType.Low_Rank, 4, ["Ballooning Problems"]),  # Rotton Vale
    # Level 4 Optional Quests
    "One Helluva Sinus Infection": LocationData(451, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Gettin' Yolked in the Forest": LocationData(452, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Royal Relocation": LocationData(461, LocType.Low_Rank, 4, ["One for the History Books"]),
    "It's a Crying Shamos": LocationData(471, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "A Tzitzi for Science": LocationData(472, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "Sorry You're Not Invited": LocationData(473, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "What a Bunch of Abalone": LocationData(474, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "White Monster for a White Coat":
        LocationData(475, LocType.Low_Rank, 4, ["Ballooning Problems", "Landing the Landslide Wyvern"]),
    "Persistent Pests": LocationData(481, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "A Rotten Thing To Do": LocationData(482, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "A Bone to Pick": LocationData(483, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "On Nightmare's Wings": LocationData(484, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    # Level 5 Assigned Quests
    "Legiana: Embodiment of Elegance": LocationData(408, LocType.Low_Rank, 4, ["Radobaan Roadblock"]),
    "Into the Bowels of the Vale": LocationData(501, LocType.Low_Rank, 4, ["Legiana: Embodiment of Elegance"]),
    "A Fiery Throne Atop the Forest": LocationData(502, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    "Horned Tyrant Below the Sands": LocationData(503, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    # Level 5 Optional Quests
    "When Desire Becomes an Obsession": LocationData(551, LocType.Low_Rank, 4, ["A Fiery Throne Atop the Forest"]),
    "Redefining the 'Power Couple'": LocationData(552, LocType.Low_Rank, 4, ["A Fiery Throne Atop the Forest"]),
    "Twin Spires Upon the Sands": LocationData(561, LocType.Low_Rank, 4, ["Horned Tyrant Below the Sands"]),
    "A Humid Headache": LocationData(571, LocType.Low_Rank, 4, ["Legiana: Embodiment of Elegance"]),
    "Gone in a Flash": LocationData(572, LocType.Low_Rank, 4, ["Man's Best Friend"]),
    "Scratching the Itch": LocationData(581, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    "Man's Best Friend":
        LocationData(582, LocType.Low_Rank, 4, ["Into the Bowels of the Vale", "White Monster For A White Coat"]),
    "The Meat of the Matter": LocationData(583, LocType.Low_Rank, 4, ["Into the Bowels of the Vale"]),
    # Level 6 Assigned Quests
    "A Colossal Task":
        LocationData(504, LocType.Low_Rank, 4, ["Horned Tyrant Below the Sands", "A Fiery Throne Atop The Forest"]), # Low Rank Goal
    "Invader In The Waste": LocationData(601, LocType.High_Rank, 5, ["A Colossal Task"]),  # Progress 5
    "Tickled Pink": LocationData(605, LocType.High_Rank, 5, ["Invader In The Waste"]),
    # Level 6 Optional Quests
    "Left Quite The Impression": LocationData(641, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Hard To Swallow": LocationData(651, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Googly-Eyed Green Monster": LocationData(652, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "A Hair-Raising Experience": LocationData(653, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "It Can't See You If You Don't Move": LocationData(654, LocType.High_Rank, 5, ["Tickled Pink"]),
    "The Sleeping Sylvan Queen": LocationData(655, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Stuck In Their Ways": LocationData(656, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Keep Your Hands To Yourself!": LocationData(661, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "A Crown Of Mud And Anger": LocationData(662, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Pukei-Pukei Ambush": LocationData(663, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Up To Your Waist In The Waste": LocationData(665, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Brown Desert, Green Queen": LocationData(666, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Tresspassing Troublemaker": LocationData(667, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Say Cheese!": LocationData(671, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Loop the Paolumu": LocationData(672, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Tingling Taste": LocationData(681, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Stuck in a Rut": LocationData(682, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Chef Quest! Pumped to Deliver": LocationData(683, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Chef Quest! A Rotten Request":
        LocationData(684, LocType.High_Rank, 5, ["Tickled Pink", "Chef Quest! Pumped to Deliver"]),
    "Chef Quest! Gajalaka Lockdown": LocationData(694, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "Dodogama Drama": LocationData(693, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "A Scalding Scoop": LocationData(692, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "A Meow for Help": LocationData(691, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    # Level 7 Assigned Quests
    "Old World Monster In The New World": LocationData(607, LocType.High_Rank, 6, ["Tickled Pink"]), # Progress 6, Elder Recess
    # Level 7 Optional Quests
    "A Cherry Wind Upon the Reefs": LocationData(771, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Pretty In Pink": LocationData(761, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "A Fiery Convergence": LocationData(795, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Ruler of the Azure Skies": LocationData(793, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Ore-eating Occupier": LocationData(792, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Lavasioth, Master of Magma": LocationData(791, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Legiana: Highlands Royalty": LocationData(772, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Well, That Diablos!": LocationData(762, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Rathalos in Blue": LocationData(752, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "The Red and Blue Crew": LocationData(753, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Two-horned Hostility": LocationData(763, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Talons of Ire and Ice": LocationData(774, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Odogaron Unleashed": LocationData(781, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "RRRRRumble in the Waste!": LocationData(764, LocType.High_Rank, 6, ["A Sore Site"]),
    "A Sore Site": LocationData(773, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Bazelgeuse in the Field of Fire": LocationData(794, LocType.High_Rank, 6, ["Man's Best Friend"]),
    # Level 8 Assigned Quests
    "A Wound and a Thirst": LocationData(701, LocType.High_Rank, 7, ["Old World Monster In The New World"]), # Progress 7
    "Kushala Daora, Dragon of Steel": LocationData(802, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Teostra the Infernal": LocationData(801, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Hellish Fiend Vaal Hazak": LocationData(803, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    # Level 8 Optional Quests
    "The Eater of Elders": LocationData(891, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Lightning Strikes Twice": LocationData(871, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    "Master of the Gale": LocationData(892, LocType.High_Rank, 7, ["Kushala Daora, Dragon of Steel"]),
    "Stirring from the Grave": LocationData(881, LocType.High_Rank, 7, ["Hellish Fiend Vaal Hazak"]),
    "The Winds of Wrath Bite Deep": LocationData(895, LocType.High_Rank, 7, ["Teostra the Infernal"]),
    "A Portent of Disaster": LocationData(851, LocType.High_Rank, 7, ["Kushala Daora, Dragon of Steel"]),
    "Hellfire's Stronghold": LocationData(893, LocType.High_Rank, 7, ["Teostra the Infernal"]),
    "A Blaze in the Sand": LocationData(861, LocType.High_Rank, 7, ["Teostra the Infernal"]),
    # High Rank Win Condition
    "Land of Convergence": LocationData(804, LocType.High_Rank, 7,
                                        ["Teostra the Infernal", "Kushala Daora, Dragon of Steel", "Teostra the Infernal"]), # High Rank Goal
    # Master Rank Start
    # MR 1 Assigned Quests
    "Baptism by Ice": LocationData(1101, LocType.Master_Rank, 8, ["Land of Convergence"]), # Progress 8
    "Banbaro Blockade": LocationData(1102, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    # MR 1 Optional Quests
    "Deep Snow Diver": LocationData(1121, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "Ice Catch!": LocationData(1123, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Taking Charge": LocationData(1122, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "Call of the Wild": LocationData(1124, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "The Great Jagras Returns!": LocationData(1151, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Literary Thief": LocationData(1154, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "New World Problems": LocationData(1152, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Beating Around the Bush": LocationData(1153, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Trapping the Tree Trasher": LocationData(1155, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Wildspire Treasure Hunt": LocationData(1161, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Taster's Tour": LocationData(1164, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Dragged Through the Mud": LocationData(1162, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Jyura in My Way": LocationData(1163, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "All the Wrong Signals": LocationData(1171, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Grinding My Girros": LocationData(1181, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Can't Bring Yourself To It": LocationData(1191, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "This Here's Big Horn Country!": LocationData(1192, LocType.Master_Rank, 8, ["Ready to Strike", "Ice Catch!"]),
    # MR 2 Assigned Quests
    "Ready to Strike": LocationData(1201, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "No Time for Naps": LocationData(1202, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Play Both Ends": LocationData(1203, LocType.Master_Rank, 8, ["Ready to Strike"]),
    # MR 2 Optional Quests
    "Analysis Creates Paralysis": LocationData(1221, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Poison and Paralysis Pinch": LocationData(1222, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Boaboa Constrictor": LocationData(1223, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "By Our Powers Combined": LocationData(1224, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "You Scratch Our Backs...": LocationData(1225, LocType.Master_Rank, 8, ["By Our Powers Combined"]),
    "Anjanath Antics": LocationData(1251, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Fool's Mate": LocationData(1252, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Nighty Night Nightshade": LocationData(1253, LocType.Master_Rank, 8, ["No Time for Naps", "Trapping the Tree Trasher"]),
    "Stick Your Nose Somewhere Else": LocationData(1263, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "A Queen At Heart": LocationData(1261, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "A Face Nightmares are Made Of": LocationData(1262, LocType.Master_Rank, 8, ["No Time for Naps"]),
    "Feisty Girl Talk": LocationData(1264, LocType.Master_Rank, 8, ["Pink Power Grab", "A Queen At Heart"]),
    "The Plight of Paolumu": LocationData(1271, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Pink Power Grab": LocationData(1272, LocType.Master_Rank, 8, ["Feisty Girl Talk"]),
    "Protip: Stay Hydrated": LocationData(1273, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "No Laughing Matter": LocationData(1281, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Bugger Off Bugs!": LocationData(1282, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Looking For That Glimmer": LocationData(1291, LocType.Master_Rank, 8, ["Ready to Strike", "Greetings from the Tundra"]),
    "Put That Red Cup Away": LocationData(1274, LocType.Master_Rank, 8, ["Feisty Girl Talk", "Poison and Paralysis Pinch"]), #Also need Waterproof Mantle
    # MR 3 Assigned Quests
    "Blizzard Blitz": LocationData(1301, LocType.Master_Rank, 10, ["No Time for Naps", "Play Both Ends"]), # Progress 10
    "Ever-present Shadow": LocationData(1302, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "The Scorching Blade": LocationData(1303, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Absolute Power": LocationData(1304, LocType.Master_Rank, 10, ["Ever-present Shadow", "The Scorching Blade"]),
    "A Smashing Cross Counter": LocationData(1305, LocType.Master_Rank, 10, ["Ever-present Shadow", "The Scorching Blade"]),
    "A Tale of Ice and Fire": LocationData(1306, LocType.Master_Rank, 10, ["A Smashing Cross Counter", "Absolute Power"]),
    # MR 3 Optional Quests
    "Remember That One Time?": LocationData(1321, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "The Purr-fect Room: Stone": LocationData(1322, LocType.Master_Rank, 10, ["Absolute Power"]),
    "Swoop to a New Low": LocationData(1351, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Nargacoulda, Should, Would": LocationData(1352, LocType.Master_Rank, 10, ["Ever-present Shadow"]),
    "The Secret to a Good Slice": LocationData(1353, LocType.Master_Rank, 10, ["The Scorching Blade"]),
    "Red and Black Aces": LocationData(1354, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Simmer and Slice": LocationData(1363, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),  # MR 11
    "Legiana Left Behind": LocationData(1371, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "The Black Wind": LocationData(1372, LocType.Master_Rank, 10, ["Ever-present Shadow"]),
    "Don't be a Jerk with the Jerky": LocationData(1381, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "A Roar that Shook the Vale": LocationData(1382, LocType.Master_Rank, 10, ["Absolute Power"]),
    "Runnin', Rollin', and Weepin'": LocationData(1383, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),  # MR 11 and Challenger
    "Everyone's a Critic": LocationData(1392, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Begone Uragaan": LocationData(1393, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Blast Warning In Effect!": LocationData(1391, LocType.Master_Rank, 10, ["A Smashing Cross Counter"]),
    "Secret of the Ooze": LocationData(1394, LocType.Master_Rank, 10, ["Ready to Strike", "A Smashing Cross Counter"]),  # Complete all deliveries
    "Festival of Explosions!": LocationData(1395, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),  # MR 11 & Fireproof mantle
    "Proud White Knight":
        LocationData(1323, LocType.Master_Rank, 10, ["Red and Black Aces", "Runnin', Rollin', and Weepin'", "Festival of Explosions!"]),  # MR 12 & Evasion Mantle as well
    "A Nasty Flesh Wound":
        LocationData(1373, LocType.Master_Rank, 10, ["Red and Black Aces", "Runnin', Rollin', and Weepin'", "Festival of Explosions!"]),  # MR 12 & Bandit Mantle as well
    # MR 4 Assigned Quests
    "When the Mist Taketh You": LocationData(1401, LocType.Master_Rank, 10, ["A Tale of Ice and Fire"]),
    "The Thunderous Troublemaker": LocationData(1405, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "The Disintegrating Blade": LocationData(1402, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "Bad Friends, Great Enemies": LocationData(1403, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "The Defense of Seliana":
        LocationData(1404, LocType.Master_Rank, 10, ["The Disintegrating Blade", "Bad Friends, Great Enemies"]),
    # MR 4 Optional Quests
    "Noblefrost Hunter": LocationData(1421, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Tundra Troublemaker": LocationData(1422, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "Duet of Rime": LocationData(1423, LocType.Master_Rank, 10, ["The Defense of Seliana"]),  # MR 16 and Iceproof
    "Treasure in the Snow": LocationData(1424, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "These Azure Eyes See All": LocationData(1451, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Misfortune in the Forest": LocationData(1452, LocType.Master_Rank, 10, ["Bad Friends, Great Enemies"]),
    "In the Heat of the Moment": LocationData(1461, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "A Shadowy Offender": LocationData(1471, LocType.Master_Rank, 10, ["Bad Friends, Great Enemies"]),
    "This Corroded Blade": LocationData(1481, LocType.Master_Rank, 10, ["The Disintegrating Blade"]),
    "The Purr-fect Room: Light Iron":
        LocationData(1482, LocType.Master_Rank, 10, ["The Disintegrating Blade", "The Purr-fect Room: Stone"]),
    "The Purr-fect Room: Dark Iron": LocationData(1483, LocType.Master_Rank, 10, ["The Purr-fect Room: Light Iron"]),
    "Blue Rathalos Blues": LocationData(1491, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Trap the Thunder Jaw": LocationData(1492, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),  # Thunder mantle
    "Piercing Black": LocationData(1462, LocType.Master_Rank, 10, ["Duet of Rime", "Trap the Thunder Jaw"]),  # Also MR 17 and Rocksteady
    # "Treasure in the Steam": LocationData(1424, LocType.Master_Rank, ["Available from event start time?"]),
    # MR 5 Assigned Quests
    "The Iceborne Wyvern": LocationData(1501, LocType.Master_Rank, 11, ["The Defense of Seliana"]), # Progress 11
    "The Second Coming": LocationData(1502, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Under the Veil of Death": LocationData(1503, LocType.Master_Rank, 11, ["The Second Coming"]),
    "A Light from the Abyss": LocationData(1504, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    # MR 5 Optional Quests
    "Clashing Swords Upon The Rime": LocationData(1521, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Mark of the Sun": LocationData(1592, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Royal Audience on the Sand": LocationData(1561, LocType.Master_Rank, 11, ["Mark of the Sun"]),
    "Wings of the Wind": LocationData(1591, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "The Harbringer of Clear Skies": LocationData(1551, LocType.Master_Rank, 11, ["Wings of the Wind"]),
    "It's the Afterlife for Me": LocationData(1581, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    "Memories of the Sea God": LocationData(1572, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "Seething with Anger": LocationData(1593, LocType.Master_Rank, 11, ["The Second Coming"]),
    "The Tyrant's Banquet": LocationData(1562, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "Lightning Crashes": LocationData(1571, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
    "The Purr-fect Room: Silver":
        LocationData(1594, LocType.Master_Rank, 11, ["The Iceborne Wyvern", "The Purr-fect Room: Light Iron"]),  # Actually only Light Iron
    "Here Comes the Deathmaker": LocationData(1552, LocType.Master_Rank, 11, ["Absolute Power", "Under the Veil of Death"]),  # Actually only Absolute
    # MR 6 Assigned Quests
    "To the Guided, A Paean": LocationData(1601, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "Paean of Guidance": LocationData(1602, LocType.Master_Rank, 11, ["To the Guided, A Paean"]),  # Master Rank Goal
}

arenaquest_database: Dict[str, LocationData] = {
    # Level 3
    "Special Arena: Pukei-Pukei": LocationData(331, LocType.Low_Rank, 2, ["One For The History Books"]),
    "Special Arena: Barroth": LocationData(332, LocType.Low_Rank, 2, ["Sinister Shadows In The Swamp"]),
    "Special Arena: Tobi-Kadachi": LocationData(333, LocType.Low_Rank, 2, ["The Encroaching Anjanath"]),
    # Level 4
    "Special Arena: Anjanath": LocationData(431, LocType.Low_Rank, 4, ["The Encroaching Anjanath"]),
    "Special Arena: Paolumu": LocationData(433, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    "Special Arena: Radobaan": LocationData(434, LocType.Low_Rank, 4, ["Ballooning Problems"]),
    # Level 5
    "Special Arena: Legiana": LocationData(531, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Special Arena: Odogaron":
        LocationData(532, LocType.Low_Rank, 4, ["Horned Tyrant Below The Sands", "A Fiery Throne Atop The Forest"]),
    "Special Arena: Rathalos":
        LocationData(533, LocType.Low_Rank, 4, ["Horned Tyrant Below The Sands", "A Fiery Throne Atop The Forest"]),
    "Special Arena: Diablos":
        LocationData(534, LocType.Low_Rank, 4, ["Horned Tyrant Below The Sands", "A Fiery Throne Atop The Forest"]),
    # Level 6
    "Special Arena: HR Pukei-Pukei": LocationData(631, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Special Arena: HR Barroth": LocationData(632, LocType.High_Rank, 5, ["Invader In The Waste"]),
    "Special Arena: HR Anjanath": LocationData(634, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Rathian": LocationData(635, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Tobi-Kadachi": LocationData(633, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Paolumu": LocationData(636, LocType.High_Rank, 5, ["Tickled Pink"]),
    "Special Arena: HR Radobaan": LocationData(637, LocType.High_Rank, 5, ["Tickled Pink"]),
    # Level 7
    "Special Arena: HR Pink Rathian": LocationData(731, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Special Arena: HR Legiana": LocationData(732, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Odogaron": LocationData(733, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Azure Rathalos": LocationData(736, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Diablos": LocationData(737, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Black Diablos": LocationData(738, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Uragaan": LocationData(734, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    "Special Arena: HR Rathalos": LocationData(735, LocType.High_Rank, 6, ["A Wound and a Thirst"]),
    # MR 1
    "Special Arena: MR Pukei-Pukei": LocationData(1131, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Special Arena: MR Barroth": LocationData(1132, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Special Arena: MR Tobi-Kadachi": LocationData(1133, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Special Arena: MR Banbaro": LocationData(1134, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    # MR 2
    "Special Arena: MR Anjanath": LocationData(1231, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Radobaan": LocationData(1232, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Coral Pukei-Pukei": LocationData(1233, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Special Arena: MR Viper Tobi-Kadachi": LocationData(1234, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Rathian": LocationData(1235, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Pink Rathian": LocationData(1236, LocType.Master_Rank, 8, ["Pink Power Grab"]),
    "Special Arena: MR Paolumu": LocationData(1237, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Special Arena: MR Nightshade Paolumu": LocationData(1238, LocType.Master_Rank, 8, ["No Time for Naps"]),
    # MR 3
    "Special Arena: MR Legiana": LocationData(1331, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Odogaron": LocationData(1332, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Uragaan": LocationData(1333, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Rathalos": LocationData(1334, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Diablos": LocationData(1335, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Barioth": LocationData(1336, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Special Arena: MR Nargacuga": LocationData(1337, LocType.Master_Rank, 10, ["Ever-present Shadow"]),
    "Special Arena: MR Glavenus": LocationData(1338, LocType.Master_Rank, 10, ["The Scorching Blade"]),
    "Special Arena: MR Brachydios": LocationData(1339, LocType.Master_Rank, 10, ["A Smashing Cross Counter"]),
    "Special Arena: MR Tigrex": LocationData(1340, LocType.Master_Rank, 10, ["Absolute Power"]),
    # MR 4
    "Special Arena: MR Azure Rathalos": LocationData(1431, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Special Arena: MR Black Diablos": LocationData(1432, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "Special Arena: MR Fulgur Anjanath": LocationData(1435, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    "Special Arena: MR Acidic Glavenus": LocationData(1433, LocType.Master_Rank, 10, ["The Disintegrating Blade"]),
    "Special Arena: MR Ebony Odogaron": LocationData(1434, LocType.Master_Rank, 10, ["Bad Friends, Great Enemies"]),
}

specialquest_database: Dict[str, LocationData] = {
    "The Food Chain Dominator": LocationData(50701, LocType.High_Rank, 7, ["Old World Monster In The New World"]),
    "The Blazing Sun": LocationData(50801, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Pandora's Arena": LocationData(50802, LocType.Master_Rank, 8, ["The Blazing Sun"]),
    "No Remorse, No Surrender": LocationData(50803, LocType.Master_Rank, 8, ["Pandora's Arena"]),
    "A Visitor from Another World": LocationData(50601, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Legendary Beast": LocationData(50905, LocType.Master_Rank, 8, ["A Visitor from Another World"]),
    "He Taketh It With His Eyes": LocationData(50906, LocType.Master_Rank, 8, ["The Legendary Beast"]),
    "Contract: Trouble in the Ancient Forest": LocationData(50910, LocType.Master_Rank, 8, ["Land of Convergence"]),
}

eventquest_database: Dict[str, LocationData] = {
    # Level 2
    "Up at the Crack of Dawn": LocationData(61101, LocType.Low_Rank, 2, ["A Kestodon Kerfuffle"]),
    "Chew the Fat": LocationData(66101, LocType.Low_Rank, 2, ["The Great Jagras Hunt"]),
    # Level 3
    "USJ: Gold Star Treatment": LocationData(67106, LocType.Low_Rank, 2, ["Sinister Shadows In The Swamp"]),
    "Where Sun Meets Moon": LocationData(61103, LocType.Low_Rank, 2, ["Sinister Shadows In The Swamp"]),
    # Level 4
    "Greeting the Gluttons": LocationData(66106, LocType.Low_Rank, 4, ["One For The History Books"]),
    "Ya-Ku With That?": LocationData(66102, LocType.Low_Rank, 4, ["One For The History Books"]),
    "Timberland Troublemakers": LocationData(61104, LocType.Low_Rank, 4, ["One For The History Books"]),
    # Level 5
    "Fleshed Cleaved to Bone": LocationData(66103, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Every Hunter's Dream": LocationData(61105, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "The Poison Posse": LocationData(66105, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Kirin the Myth": LocationData(66104, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    "Wicked Wildspire Warfare": LocationData(64101, LocType.Low_Rank, 4, ["The Embodiment of Legiana"]),
    # Level 6
    "Triple Threat Throwdown": LocationData(65605, LocType.High_Rank, 5, ["Old World Monster In The New World"]),
    "Wiggle Me This": LocationData(65604, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Egg Lovers United": LocationData(65603, LocType.High_Rank, 5, ["A Colossal Task"]),
    "A Flash in the Pan": LocationData(65602, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Scrapping with the Shamos": LocationData(65601, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Gaze Upon the Dawn": LocationData(62608, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Mosswinin' and Dinin'": LocationData(61605, LocType.High_Rank, 5, ["A Colossal Task"]),
    "Midnight Mayhem": LocationData(61601, LocType.High_Rank, 5, ["A Colossal Task"]),
    # Level 7
    "USJ Blazing Azure Stars!": LocationData(67604, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "A Rush of Blood": LocationData(67103, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Coral Waltz": LocationData(66603, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Wildspire Bolero": LocationData(66602, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Kings Know No Fear": LocationData(61604, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "A Royal Pain": LocationData(61603, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "This Is How Revolts Start": LocationData(66606, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Rock N' Roll Recess": LocationData(66605, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Rollin' With The Uragaan": LocationData(64601, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Effluvial Opera": LocationData(66604, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    "Deep Green Blues": LocationData(66601, LocType.High_Rank, 6, ["Old World Monster In The New World"]),
    # Level 8
    "Code: Red": LocationData(67605, LocType.High_Rank, 7, ["A Wound and a Thirst"]),
    # Level 9
    "Keeper of the Otherworld": LocationData(62609, LocType.Master_Rank, 8, ["Land of Convergence"]),
    # The following require high amount of HR, may disable or subcategorize
    "A Simple Task": LocationData(65606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Nose for an Eye": LocationData(66608, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "No Tomorrow for Usurpers": LocationData(66609, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Heralds of Destruction City": LocationData(62506, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "When Blue Dust Surpasses Red Lust": LocationData(62511, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Snow & Cherry Blossoms": LocationData(66607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Deathly Quiet Curtain": LocationData(62502, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Whisper of White Mane": LocationData(62503, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Relish the Moment": LocationData(62515, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Greatest Jagras": LocationData(61606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Name's Lavasioth": LocationData(61607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Scorn of the Sun": LocationData(62504, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Eye of the Storm": LocationData(62505, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Undying Alpenglow": LocationData(62606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Like a Moth to the Flame": LocationData(62607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "The Thronetaker": LocationData(66610, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Tracking the Delivery": LocationData(65607, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "A Visitor from Eorzea (Extreme)": LocationData(67606, LocType.Master_Rank, 8, ["Land of Convergence"]),
    "Contract: Woodland Spirit": LocationData(67610, LocType.Master_Rank, 8, ["Land of Convergence"]),
    # MR 1
    "Fetching Light Pearls": LocationData(66853, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "A Fish to Whet Your Appetite": LocationData(61816, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Skyward Snipers": LocationData(61815, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Flora Frostbite": LocationData(61811, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "Duffel Duty": LocationData(61805, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "A Bunch of Sticks in the Mud": LocationData(66803, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Desert Desserts": LocationData(66804, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Trophy Fishin'": LocationData(66801, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    "Pearl Snatchers": LocationData(61801, LocType.Master_Rank, 8, ["Banbaro Blockade"]),
    "The Lord of the Underworld Beckons": LocationData(66802, LocType.Master_Rank, 8, ["Baptism by Ice"]),
    # MR 2
    "Paolumu Lullabies": LocationData(61809, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Kadachi Twins": LocationData(66862, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Camoflawed": LocationData(66854, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Every Hunter's Dream II": LocationData(61802, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Ballon Fight": LocationData(64801, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "Colorful Carnival": LocationData(66806, LocType.Master_Rank, 8, ["Play Both Ends"]),
    "A New Troublemaker in Town": LocationData(66805, LocType.Master_Rank, 8, ["Ready to Strike"]),
    "Hunter-Blunder": LocationData(66807, LocType.Master_Rank, 8, ["Ready to Strike"]),
    # MR 3
    "Seeing is Believing": LocationData(66855, LocType.Master_Rank, 10, ["Absolute Power"]),
    "When the Swift Meets the Roar": LocationData(66834, LocType.Master_Rank, 10, ["Absolute Power"]),
    "50 Shades of White": LocationData(61813, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Every Hunter's Dream III": LocationData(61803, LocType.Master_Rank, 10, ["Absolute Power"]),
    "Fired-Up Bruisers": LocationData(66811, LocType.Master_Rank, 10, ["Absolute Power"]),
    "A Curious Experiment": LocationData(66809, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "Soaked and Shivering": LocationData(66810, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    "A Sky & Sea of Fire": LocationData(66808, LocType.Master_Rank, 10, ["Blizzard Blitz"]),
    # MR 4
    "Beef is Never a Mi-steak": LocationData(61812, LocType.Master_Rank, 10, ["The Defense of Seliana"]),
    "Servants of the Vale": LocationData(66814, LocType.Master_Rank, 10, ["The Defense of Seliana"]),
    "The Desert Dash": LocationData(66812, LocType.Master_Rank, 10, ["When the Mist Taketh You"]),
    "In the Depths of the Forest": LocationData(66813, LocType.Master_Rank, 10, ["The Thunderous Troublemaker"]),
    # MR 5
    "Scores of Ores": LocationData(61806, LocType.Master_Rank, 11, ["The Defense of Seliana"]),
    "A Chilling Entrance": LocationData(61807, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    "RE: Return of the Bioweapon": LocationData(67801, LocType.Master_Rank, 11, ["Under the Veil of Death"]),
    "A Reason Behind The Hunger": LocationData(66817, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "The Winter Blues": LocationData(66816, LocType.Master_Rank, 11, ["A Light from the Abyss"]),
    "We Three Kings": LocationData(66815, LocType.Master_Rank, 11, ["The Second Coming"]),
    "Talk About a Party Foul...": LocationData(66859, LocType.Master_Rank, 11, ["The Second Coming"]),
    "Old Dog, New Trick": LocationData(66867, LocType.Master_Rank, 11, ["The Iceborne Wyvern"]),
}

masterlocations_database: typing.Dict[str, LocationData] = {
    **quest_database,
    **arenaquest_database,
    **specialquest_database,
    **eventquest_database,
}

da_list = []
for key, location_data in masterlocations_database.items():
    if location_data.code in da_list:
        print(f"name = {key}, id = {location_data.code}")
    else:
        da_list.append(location_data.code)
