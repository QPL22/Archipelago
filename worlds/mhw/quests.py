
from .locations import LocationData, LocType, MHWLocation, LOCATION_ID_OFFSET, \
    ENDEMIC_ID_OFFSET, grindy_database, specializedtools_database
from .options import MonsterHunterWorldOptions
from typing import Dict, List, TYPE_CHECKING
from worlds.AutoWorld import Random

# Decide between generating text or text inputs here or on client
# bring in list of locations that will be played to mitigate redundant work
# not dealing with maps for now
# Have to take in account of the map of vanilla since will affect logic eventually.
# Monsters have to be done here for future stuff
#
# public byte[] ObjectiveIDs = { 0x00, 0x01, 0x02, 0x11, 0x21, 0x31 }; public string[] ObjectiveList = { "None", "Multi monster quest", "Deliver", "Capture", "Slay", "Hunt" };
# public byte[] QuestTypeIDs = { 0x01, 0x02, 0x04, 0x08, 0x10, 0x20 }; public string[] QuestTypeList = {"Hunting quest (Table spawn)","Slaying quest (Table spawn)","Capture quest (Table spawn)",
#             "Delivery quest (Table spawn)","Hunting quest (Sequential spawn)","Special quest (Table spawn)"};
# dictionary to be sent: quest id(-1400000000 + front 0?) , Monster Info[QuestType/(-1 == hint only, 0 == no change), Objective, Map(0=Nochange], MonsterID1, MonsterID2, MonsterID3, MonsterChance3, MonsterID4, MonsterChance4...]
# Make totally random first then balanced for crafting players


# 15 (behemoth), 23 (leshen), 26 (xeno'jjiva), 51 (ancient leshen)
BigMonsterIDs = [0, 1, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                 36, 37, 39]
LowRankBigMonsterIDs = [0, 1, 7, 9, 12, 14, 21, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35]
UncaptureableMonsterIDs = [14, 15, 16, 17, 18, 23, 25, 26, 36, 51, 70, 75, 79, 80, 81, 87, 97, 101]

HighRankMonsters = [10, 11, 13, 16, 17, 18, 19, 20, 22, 25, 36, 37, 39]
IBHighRankOnlyMonsters = [7, 10, 20, 25, 36, 39]

BigMonsterIDsIB = [0, 1, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 61, 62,
                   63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 88, 89, 90, 91, 93, 94, 95,
                   96, 99, 100]

goal_quests = [804, 504, 1602, 401]  # Maybe include 401
story_quest = [102, 103, 201, 205, 301, 302, 305, 306, 401, 405, 407, 408, 501, 502, 503, 504, 601, 605, 607, 805,
               50701]
slay_story_quest = [701, 801, 802, 803, 804, 806, 50801, 50802, 50803, 50601, 50906, 50910, 1404, 1501, 1503, 1504,
                    1601, 1602, 1605, 51601, 51602, 51606, 51611, 51612, 51613]
multi_object = [552, 753, 764, 774, 795, 996, 997, 998, 61103, 61105, 61603, 61604, 66102, 66103, 66606, 66607, 66608,
                67604]
multi_monster = [992, 64101, 65605, 66105, 66106, 66601, 66602, 66603, 66604, 66605, 67103, 67605, 67608]
duplicate = [961, 5003, 61104, 64601, 65602, 66101, 67106]
slay = [572, 851, 861, 871, 881, 891, 892, 893, 894, 895, 896, 971, 3001, 3002, 3031, 3032, 3033, 3034, 3101, 62502,
        62503, 62504, 62505, 62506, 62511, 62607, 62609, 63038, 63039, 63052, 63101, 63102, 63103, 63107, 63108, 63130,
        63131, 67610, 1521, 1551, 1552, 1561, 1571, 1572, 1581, 1591, 1592, 1661, 1691, 3071, 3072, 3073, 3091, 3171,
        51622, 63073,
        63074, 63143, 63150, 66836, 67801, 66847, 66840, 66841, 66842, 66843, 66844, 66850, 66858, 66863, 67806]
slay_multi_object = [3051, 3052, 50861, 50891, 50892, 63002, 63031, 63051]
slay_multi_monster = [995, 63001, 63104, 63105, 63106, 63109, 63110, 66610, 1651, 1671, 1692, 3074, 3092, 61807, 63071,
                      63072, 63149, 66815, 66816]
slay_dupe = [63032, 66104, 61808, 66801, 66803]
capture = [261, 365, 475, 582, 656, 63104, 1123, 1155, 1222, 1253, 1322, 1394, 1482, 1492, 1594, 61803]
# master rank NOTE = Might be unnessary
ib_slay_story_quest = [1404, 1501, 1503, 1504, 1601, 1602, 1605, 51601, 51602, 51606, 51611, 51612, 51613]
ib_story_quest = [1101, 1102, 1201, 1202, 1203, 1301, 1302, 1303, 1304, 1305, 1306, 1401, 1402, 1403, 1405, 1502, 51603,
                  51604, 51607]
ib_quest = [1121, 1122, 1131, 1132, 1133, 1134, 1151, 1152, 1153, 1154, 1161, 1162, 1163, 1164, 1171, 1181, 1191, 1192,
            1221, 1224, 1225, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1251, 1252, 1261, 1262, 1263, 1271, 1272,
            1273, 1274, 1281, 1321, 1323, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1351, 1352, 1353,
            1361, 1362, 1371, 1372, 1373, 1381, 1382, 1391, 1392, 1393, 1421, 1422, 1431, 1432, 1433, 1434, 1435, 1451,
            1452, 1461, 1462, 1471, 1481, 1491, 1562, 1593, 1606, 1632, 1633, 1634, 1635, 1636, 51621, 51623, 61806,
            61809, 61813, 64802, 66817, 66818, 66819, 66820, 66821, 66822, 66824, 66825, 66832, 66835, 66859, 66860,
            67807, 66846, 66854, 66855, 66856, 66857, 66861, 66867, 67809, 66865, 66866]
ib_multi_object = [1264, 1354, 1363, 1383, 1395, 1423, 1483, 1603, 1604, 61802, 61812, 64801, 66805, 66807, 66808,
                   66809,
                   66810, 66811, 66812, 66813, 66814, 66862]
ib_multi_monster = [1631, 1642, 61814, 66806, 66826, 66827, 66828, 66829, 66830, 66831, 66834, 66864]
ib_dupe = [61808, 66801, 66803]
ib_slay = [1521, 1551, 1552, 1561, 1571, 1572, 1581, 1591, 1592, 1661, 1691, 3071, 3072, 3073, 3091, 3171, 51622, 63073,
           63074, 63143, 63150, 66836, 67801, 66847, 66840, 66841, 66842, 66843, 66844, 66850, 66858, 66863, 67806]
ib_slay_multi_mon = [1651, 1671, 1692, 3074, 3092, 61807, 63071, 63072, 63149, 66815, 66816]
ib_capture = [1123, 1155, 1222, 1253, 1322, 1394, 1482, 1492, 1594, 61803]

coral_quest_ids = [405, 408, 607, 806, 472, 473, 571, 671, 672, 771, 772, 773, 572, 871, 971, 475, 774, 1203, 1403,
                   1504,
                   1171, 1271, 1272, 1273, 1274, 1371, 1372, 1373, 1471, 1571, 1572, 1671, 5003, 62503, 61803, 61814,
                   66104, 66603, 66607, 66810, 66816, 66818, 66828, 66847]

hoarfrost_quest_ids = [1101, 1102, 1121, 1122, 1123, 1201, 1221, 1222, 1224, 1225, 1301, 1321, 1322, 1323, 1401, 1405,
                       1421, 1422, 1423, 1501, 1521, 51602, 51607, 51623, 66801, 66831, 66846, 66857, 67809]

quest_dict: Dict[str, List[int]] = {}

mon_pool_low = []
mon_pool_high = []
mon_pool_master = []
remove_mon = []
low_clear = False
high_clear = False
master_clear = False


# options_dataclass = MonsterHunterWorldOptions
# options: MonsterHunterWorldOptions


def questid_to_str(locid):
    questid = LOCATION_ID_OFFSET - locid
    if questid < 1000:
        return str("00" + str(questid))
    elif questid < 10000:
        return str("0" + str(questid))
    else:
        return str(questid)


# Include default quest settings here?
# Rank sorting might not be required
def quest_sorter(world, loc_data, questrand, icequest, questhint):
    # If quest rando is off but quest hint is on add to dict with hint mark

    if not questrand and questhint:
        quest_dict[questid_to_str(loc_data.code)] = [-1]
        return
    elif not questrand and not questhint:
        return

    # If not randomizing iceborne quest and master rank and quest hint is on put in dict with hint mark
    if not icequest and loc_data.loc_type.Master_Rank:
        if questhint:
            quest_dict[questid_to_str(loc_data.code)] = [-1]
            return
        else:
            return

    quest_id = LOCATION_ID_OFFSET - loc_data.code

    if world.options.noslay.value == 0 and (quest_id in slay_story_quest or
                                      quest_id in slay or
                                      quest_id in slay_multi_monster or
                                      quest_id in slay_dupe or
                                      quest_id in slay_multi_object):
        if ((world.world.options.multimonster.value == 0 and quest_id in slay_multi_monster) or
                (world.options.multiobjective.value == 0 and quest_id in slay_multi_object)):
            if questhint:
                quest_dict[questid_to_str(loc_data.code)] = [-1]
            return
        else:
            if loc_data.loc_type.Master_Rank:
                world.master_rank.append(loc_data)
                return
            elif loc_data.loc_type.High_Rank:
                world.high_rank.append(loc_data)
                return
            else:
                world.low_rank.append(loc_data)
                return

    if quest_id in capture:
        if world.options.nocap.value == 1:
            if loc_data.loc_type.Master_Rank:
                world.master_rank.append(loc_data)
                return
            elif loc_data.loc_type.High_Rank:
                world.high_rank.append(loc_data)
                return
            else:
                world.low_rank.append(loc_data)
                return
        elif questhint:
            quest_dict[questid_to_str(loc_data.code)] = [-1]
        return

    if quest_id in multi_object:
        if world.options.multiobjective.value == 1:
            if loc_data.loc_type.Master_Rank:
                world.master_rank.append(loc_data)
                return
            elif loc_data.loc_type.High_Rank:
                world.high_rank.append(loc_data)
                return
            else:
                world.low_rank.append(loc_data)
                return
        elif questhint:
            quest_dict[questid_to_str(loc_data.code)] = [-1]
        return

    if quest_id in multi_monster:
        if world.options.multimonster.value == 1:
            if loc_data.loc_type.Master_Rank:
                world.master_rank.append(loc_data)
                return
            elif loc_data.loc_type.High_Rank:
                world.high_rank.append(loc_data)
                return
            else:
                world.low_rank.append(loc_data)
                return
        elif questhint:
            quest_dict[questid_to_str(loc_data.code)] = [-1]
        return

    if quest_id in duplicate:
        if world.options.same_monster.value == 1:
            if loc_data.loc_type.Master_Rank:
                world.master_rank.append(loc_data)
                return
            elif loc_data.loc_type.High_Rank:
                world.high_rank.append(loc_data)
                return
            else:
                world.low_rank.append(loc_data)
                return
        elif questhint:
            quest_dict[questid_to_str(loc_data.code)] = [-1]
        return

    if quest_id in goal_quests and questhint:
        quest_dict[questid_to_str(loc_data.code)] = [-1]
        return

    # IF probably redundant
    if questrand:
        if loc_data.loc_type.Master_Rank:
            world.master_rank.append(loc_data)
            return
        elif loc_data.loc_type.High_Rank:
            world.high_rank.append(loc_data)
            return
        else:
            world.low_rank.append(loc_data)
            return
    # Error Catcher
    else:
        quest_dict[questid_to_str(loc_data.code)] = [-1]
        print(questid_to_str(loc_data.code) + " not sorted properly.")
        return

    # Steps


# Add to temp array for each rank
# Apply settings here. If not applied send to final array
# After regions set up go through each temp array and rando monster


def monster_pool_maker(world, rank) -> list[int]:
    # Apparently inefficent
    monster_pool = set()

    # Checks if pool is for master or if monsters in master rank are allowed in other ranks
    if rank == 2 or world.options.mastermon.value == rank:
        monster_pool.update(BigMonsterIDsIB)
        # Remove Brachy from low and high ranks
        if world.options.mastermon.value < 2 and rank != 2:
            monster_pool.remove(96)
        if world.options.shara.value == 1:
            monster_pool.add(81)
        if world.options.rajang.value == 1:
            monster_pool.add(92)
        if world.options.alatreon.value == 1:
            monster_pool.add(87)
        # If rank 2 and Ice mon only remove big monster id
        if world.options.ice_mon.value == 1 and rank == 2:
            monster_pool -= set(BigMonsterIDs)
            return list(monster_pool)
    # If high rank or all monsters for master or high in low rank
    elif rank == 1 or world.options.high_in_low_mon.value == 1 or world.options.ice_mon.value == 2:
        monster_pool.update(BigMonsterIDs)
        if world.options.leshen.value == 1:
            monster_pool.add(23)
            monster_pool.add(51)
        if world.options.xeno.value == 1:
            monster_pool.add(26)
        if world.options.behemoth.value == 1:
            monster_pool.add(15)
    # Only low rank monster if no fun settings are on.
    else:
        monster_pool.update(LowRankBigMonsterIDs)

    return list(monster_pool)


def quest_total_rando(world):
    # dictionary to be sent: quest id(-1400000000 + front 0?) , Monster Info[QuestType/(-1 == hint only, 0 == no change), Objective, Map(0=Nochange], MonsterID1, MonsterID2, MonsterID3, MonsterChance3, MonsterID4, MonsterChance4...]
    mon_pool_low.extend(monster_pool_maker(world, 0))
    mon_pool_high.extend(monster_pool_maker(world, 1))
    mon_pool_master.extend(monster_pool_maker(world, 2))

    for quest in world.low_rank + world.high_rank + world.master_rank:
        pool = []
        # Call monster_pool_maker for low rank
        # Determine Quest Object/Quest Type
        # For now set 0 if no change
        # Roll Map
        # For now set to 0 for no change but must determine vanilla.
        # Roll the monsters
        # Add to dictionary
        # Do first?
        quest_id = LOCATION_ID_OFFSET - quest.code
        # If here for changing Quest Type and Object
        quest_type = 0
        objective = 0
        # If here for map roll
        map_id = 0

        if quest.loc_type.Low_Rank:
            rank = 0
            pool = mon_pool_low.copy()
        elif quest.loc_type.High_Rank:
            rank = 1
            pool = mon_pool_high.copy()
        else:
            rank = 2
            pool = mon_pool_master.copy()
        # For loop for all monsters, universal function with parameters. Need monster_pool, map_id, quest_id, quest_type
        # If any param is 0 it should pass the vanilla value through instead
        # There should be a static pool and mutable pool, for true random just static is fine
        quest_dict[questid_to_str(quest.code)] = [quest_type, objective, map_id,
                                                  total_rando_mon(world, pool, map_id, quest_id, quest_type, rank)]


def mon_sort(world, pool, map_id, quest_id, quest_type, rank) -> list[int]:
    global low_clear, high_clear, master_clear
    mon_list = []
    # Probably inefficent, fix later
    if not pool:
        mon_list.extend(monster_pool_maker(world, rank))
        if rank == 0:
            low_clear = True
        elif rank == 1:
            high_clear = True
        else:
            master_clear = True
    else:
        mon_list = pool.copy()

    # Previous monster id?
    # Alatreon and Leshen (87, 23, 51) cannot be on coral
    if map_id == 3 or (map_id == 0 and quest_id in coral_quest_ids):
        mon_list = [m for m in mon_list if m not in (23, 51, 87)]
    # Hoarfrost cannot have alatreon
    if map_id == 8 or (map_id == 0 and quest_id in hoarfrost_quest_ids):
        mon_list = [m for m in mon_list if m != 87]
    # 301 cannot have 33 or 25 or 9
    if quest_id == 301:
        mon_list = [m for m in mon_list if m not in (9, 25, 33)]
    # 501 cannot have 29 or 35
    if quest_id == 501:
        mon_list = [m for m in mon_list if m not in (29, 35)]
    # 803 cannot have jyura
    if quest_id == 803:
        mon_list = [m for m in mon_list if m != 29]
    if world.options.nocap == 0 and (quest_type == 4 or (quest_id == 0 and (quest_id in capture or quest_id in ib_capture))):
        mon_list = [m for m in mon_list if m not in UncaptureableMonsterIDs]

    # Catch if no monsters apply but still have some monsters in pool
    if not mon_list:
        mon_list.extend(monster_pool_maker(world, rank))
        mon_list = [m for m in mon_list if m not in (9, 23, 25, 29, 33, 35)]
        mon_list = [m for m in mon_list if m not in UncaptureableMonsterIDs]

    return mon_list


def total_rando_mon(world, pool, map_id, quest_id, quest_type, rank) -> list[int]:
    # Monster rando
    mon_param = []
    mon_list = mon_sort(world, pool, map_id, quest_id, quest_type, rank)
    for i in range(7):
        # Check if pool empty
        if not mon_list:
            mon_list = mon_sort(world, pool, map_id, quest_id, quest_type, rank)

        mon_id = mon_list[world.random.randint(0, (len(mon_list)-1))]
        if i == 0:
            mon_param.append(mon_id)

        if i == 1:
            # On 301 monster 2 must be rath == 9
            if quest_id == 301:
                mon_param.append(9)
                continue
            # Same monster on dupe quests
            if (quest_id in ib_dupe or
                    quest_id in slay_dupe or
                    quest_id in duplicate):
                mon_param.append(mon_param[0])
                continue
            # Add second monster on multi quests, skip if not
            if (quest_id in slay_story_quest or
                    quest_id in slay or
                    quest_id in slay_multi_monster or
                    quest_id in slay_dupe or
                    quest_id in slay_multi_object):
                mon_param.append(mon_id)
            else:
                mon_param.append(-1)

        # 50920 monster 3 must be 23
        if i == 2 and quest_id == 50920:
            mon_param.append(23)
            mon_param.append(100)
            continue

        if i >= 2:
            # Set monster to be spawned in with same spawn percentage
            if (quest_id in multi_object or quest_id in multi_monster or quest_id in slay_multi_object or 
                    quest_id in ib_multi_monster or quest_id in ib_multi_object or quest_id in ib_slay_multi_mon):
                mon_param.append(mon_id)
                mon_param.append(-1)
                # Need more in depth quest anaylsis for better algo
            else:
                # Set the percentage of subsequent spawns for normal quests. Make spawns 100% for now.
                # If 2 check if monster spawn based on mon chan
                if i == 2 and world.options.thirdmon.value > world.random.randint(1, 100):
                    mon_param.append(mon_id)
                    mon_param.append(100)
                    continue
                # Check if previous monster was spawned and then run respective chance
                if i > 2 and len(mon_param) >= 2 and mon_param[-2] != -1:
                    if i == 3 and world.options.fourthmon.value > world.random.randint(1, 100):
                        mon_param.append(mon_id)
                        mon_param.append(100)
                        continue
                    elif i == 4 and world.options.fifthmon.value > world.random.randint(1, 100):
                        mon_param.append(mon_id)
                        mon_param.append(100)
                        continue
                    elif i == 5 and world.options.sixthmon.value > world.random.randint(1, 100):
                        mon_param.append(mon_id)
                        mon_param.append(100)
                        continue
                    elif i == 6 and world.options.seventhmon.value > world.random.randint(1, 100):
                        mon_param.append(mon_id)
                        mon_param.append(100)
                        continue
                    else:
                        mon_param.append(-1)
                        mon_param.append(-1)
                        continue
                # If 3 or later check if monster was spawned in previous slot
                # Default for now
                mon_param.append(-1)
                mon_param.append(-1)
                continue

        # Everything after this will be different for the algo
        # Don't allow dups on story quests
        if world.options.dup_mon.value == 1 or quest_id in ib_story_quest or quest_id in slay_story_quest or quest_id in ib_slay_story_quest or quest_id in story_quest:
            mon_list.remove(mon_id)

        # Add ifs here if not totally random monster.
        if world.options.sortalgo.value == 1:
            # Remove Mon ID if algo is 1 and clear is false
            if rank == 0 and low_clear is False:
                mon_pool_low.remove(mon_id)
            if rank == 1 and high_clear is False:
                mon_pool_high.remove(mon_id)
            if master_clear is False and rank == 2:
                mon_pool_master.remove(mon_id)

    return mon_param

# Check if pool empty
# Refill Pool
# Sort pool again
# Flip pool to false
# No longer remove from pool