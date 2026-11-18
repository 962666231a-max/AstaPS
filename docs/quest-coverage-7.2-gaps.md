# Quest coverage audit — what still cannot complete (7.2.0)

A quest step completes only if its `QuestContent` / `QuestExec` type has **both** an enum name and a
registered handler. Types that pass the first check but fail the second — or fail both — never fire:
the loader keeps the row, but nothing evaluates it, so the step stays open forever.

This audit measures the pinned 7.2.0 quest table against the current source tree (`main` +
the quest conditions/execs PR). It is a census of what is still missing, not a plan.

## Totals

| | condition rows | exec rows |
|---|---:|---:|
| used by the 7.2.0 quest table | 46004 | 25138 |
| reachable today (enum + handler) | 43909 (95.4%) | 23886 (95.0%) |
| **not reachable** | **2095** across 47 types | **1252** across 51 types |

## Conditions that cannot complete (47 types / 2095 rows)

| type | rows | subquests | missing | example (subId / mainId / param) |
|---|---:|---:|---|---|
| `QUEST_CONTENT_GADGET_STATE_CHANGE` | 917 | 834 |  + handler | 7710244 / 77102 / `[133707072, 72010]` |
| `QUEST_CONTENT_MAIN_COOP_ENTER_SAVE_POINT` | 665 | 560 |  + handler | 1900103 / 19001 / `[101401, 10201]` |
| `QUEST_CONTENT_SCENE_LEVEL_TAG_EQ` | 93 | 58 |  + handler | 7006401 / 70064 / `[0, 0]` |
| `QUEST_CONTENT_ACTIVITY_TRIGGER_UPDATE` | 67 | 64 |  + handler | 4008106 / 40081 / `[2017, 4008106]` |
| `QUEST_CONTENT_SCENERY_STATE_EQUAL` | 51 | 50 | enum + handler | 4022221 / 40222 / `[101001, 0]` |
| `QUEST_CONTENT_MAIN_COOP_ENTER_ANY_SAVE_POINT` | 32 | 32 |  + handler | 1902101 / 19021 / `[103601, 0]` |
| `QUEST_CONTENT_GCG_LEVEL_WIN` | 30 | 21 | enum + handler | 4010914 / 40109 / `[50301, 1]` |
| `QUEST_CONTENT_PARENT_QUEST_STATE_EQUAL` | 22 | 16 | enum + handler | 7710407 / 77104 / `[77104, 1]` |
| `QUEST_CONTENT_ACTIVITY_TRIGGER_FAILED` | 21 | 21 |  + handler | 4112102 / 41121 / `[5006, 0]` |
| `QUEST_CONTENT_LEAVE_VEHICLE` | 20 | 19 | enum + handler | 1504005 / 15040 / `[45004105, 0]` |
| `QUEST_CONTENT_ABYSS_WAR_LEVEL_STATE_EQUAL` | 18 | 14 | enum + handler | 501129 / 5011 / `[1, 3]` |
| `QUEST_CONTENT_ABYSS_WAR_LIMIT_REIGON_STATE_EQUAL` | 18 | 18 | enum + handler | 501132 / 5011 / `[20238002, 3]` |
| `QUEST_CONTENT_ENTER_MY_HOME_WORLD` | 17 | 17 |  + handler | 1908305 / 19083 / `[0, 0]` |
| `QUEST_CONTENT_ENTER_ROGUE_DUNGEON` | 11 | 11 |  + handler | 4002012 / 40020 / `[1, 0]` |
| `QUEST_CONTENT_QUEST_CHECK_EQUAL` | 10 | 5 | enum + handler | 1918224 / 19182 / `[1009, 1]` |
| `QUEST_CONTENT_TIME_VAR_PASS_REFRESH_POLICY` | 10 | 10 | enum + handler | 7766005 / 77660 / `[77660, 1]` |
| `QUEST_CONTENT_LEAVE_SCENE_RANGE_AND_ROOM` | 8 | 8 | enum + handler | 300814 / 3008 / `[3, 230]` |
| `QUEST_CONTENT_FINISH_ANY_FOOD_COOK` | 8 | 7 | enum + handler | 7603301 / 76033 / `[133601030, 30001]` |
| `QUEST_CONTENT_EVENTS_ITEM_STATUS` | 6 | 6 | enum + handler | 400207 / 4002 / `[4001, 1]` |
| `QUEST_CONTENT_LEAVE_FEATURE_TAG_VEHICLE` | 6 | 5 | enum + handler | 502606 / 5026 / `[30014, 0]` |
| `QUEST_CONTENT_ENTER_FEATURE_TAG_VEHICLE` | 5 | 4 | enum + handler | 1501915 / 15019 / `[30014, 0]` |
| `QUEST_CONTENT_SHOP_SELL_OUT` | 5 | 5 | enum + handler | 7411101 / 74111 / `[1103, 1]` |
| `QUEST_CONTENT_FISHING_SUCC` | 4 | 4 |  + handler | 7066104 / 70661 / `[1, 0]` |
| `QUEST_CONTENT_GCG_GUIDE_PROGRESS` | 4 | 2 | enum + handler | 7066505 / 70665 / `[1, 0]` |
| `QUEST_CONTENT_IRODORI_FINISH_FLOWER_COMBINATION` | 4 | 4 |  + handler | 7268702 / 72687 / `[1, 0]` |
| `QUEST_CONTENT_EXHIBITION_ACCUMULATE_GT_EQ` | 4 | 4 | enum + handler | 7402526 / 74025 / `[13502001, 0]` |
| `QUEST_CONTENT_UNLOCK_ANY_TRANS_POINT` | 4 | 4 | enum + handler | 7466802 / 74668 / `[3, 0]` |
| `QUEST_CONTENT_NOT_UNLOCKED_RECIPE` | 3 | 1 |  + handler | 4001503 / 40015 / `[0, 0]` |
| `QUEST_CONTENT_IRODORI_POETRY_REACH_MIN_PROGRESS` | 3 | 3 |  + handler | 7269102 / 72691 / `[1, 0]` |
| `QUEST_CONTENT_IRODORI_POETRY_FINISH_FILL_POETRY` | 3 | 3 |  + handler | 7269104 / 72691 / `[1, 0]` |
| `QUEST_CONTENT_AVATAR_CAPTURE_ANIMAL` | 3 | 3 | enum + handler | 7618903 / 76189 / `[0, 0]` |
| `QUEST_CONTENT_QUEST_VAR_NOT_EQUAL` | 3 | 1 | enum + handler | 80062 / 800 / `[0, 1]` |
| `QUEST_CONTENT_OBTAIN_VARIOUS_ITEM` | 2 | 2 |  + handler | 1916115 / 19161 / `[0, 0]` |
| `QUEST_CONTENT_UNLOCKED_RECIPE` | 2 | 2 |  + handler | 4001503 / 40015 / `[0, 0]` |
| `QUEST_CONTENT_ACTIVITY_END` | 2 | 2 | enum + handler | 4023401 / 40234 / `[2045001, 0]` |
| `QUEST_CONTENT_CITY_LEVEL_UP` | 2 | 2 |  + handler | 46902 / 469 / `[1, 2]` |
| `QUEST_CONTENT_CALL_PLAYER_TRAIN_IN_RANGE` | 2 | 2 | enum + handler | 701326 / 7013 / `[3, 9]` |
| `QUEST_CONTENT_AVATAR_RENAME_COMPLETE` | 1 | 1 | enum + handler | 303202 / 3032 / `[1, 0]` |
| `QUEST_CONTENT_OBTAIN_MATERIAL_WITH_SUBTYPE` | 1 | 1 |  + handler | 40702 / 407 / `[9, 0]` |
| `QUEST_CONTENT_CAPTURE_USE_MATERIAL_LIST` | 1 | 1 |  + handler | 7267203 / 72672 / `[220043, 0]` |
| `QUEST_CONTENT_SPECIFIC_WIDGET_ATTACHED` | 1 | 1 | enum + handler | 701129 / 7011 / `[220133, 0]` |
| `QUEST_CONTENT_MISC_RENAME_COMPLETE` | 1 | 1 | enum + handler | 7500007 / 75000 / `[2, 0]` |
| `QUEST_CONTENT_ITEM_NUM_LESS` | 1 | 1 | enum + handler | 80061 / 800 / `[100051, 10]` |
| `QUEST_CONTENT_QUEST_GLOBAL_VAR_LESS` | 1 | 1 | enum + handler | 80321 / 803 / `[1003, 8]` |
| `QUEST_CONTENT_ACHIEVEMENT_STATE_EQUAL` | 1 | 1 | enum + handler | 80402 / 804 / `[81233, 1]` |
| `QUEST_CONTENT_ACHIEVEMENT_ISACHIEVED` | 1 | 1 | enum + handler | 80402 / 804 / `[81230, 1]` |
| `QUEST_CONTENT_USE_WIDGET` | 1 | 1 |  + handler | 99809 / 998 / `[220009, 0]` |

## Execs that can never run (51 types / 1252 rows)

| type | rows | subquests | missing | example (subId / mainId / param) |
|---|---:|---:|---|---|
| `QUEST_EXEC_SET_MAP_LAYER_UNLOCK_STATE` | 195 | 153 | enum + handler | 7710202 / 77102 / `['1901', '1']` |
| `QUEST_EXEC_MODIFY_WEATHER_AREA` | 147 | 123 |  + handler | 701207 / 7012 / `['7043', '1']` |
| `QUEST_EXEC_UPDATE_PARENT_QUEST_REWARD_INDEX` | 95 | 93 |  + handler | 1504423 / 15044 / `['1']` |
| `QUEST_EXEC_ADD_ABYSS_WAR_ACCOUNT_DATA` | 79 | 41 | enum + handler | 501101 / 5011 / `['1001', '18,18']` |
| `QUEST_EXEC_SET_DAILY_TASK_VAR` | 68 | 54 |  + handler | 2000405 / 20004 / `['29400', '1', '0']` |
| `QUEST_EXEC_EXIT_VEHICLE` | 67 | 57 | enum + handler | 701220 / 7012 / `['45007002']` |
| `QUEST_EXEC_CHANGE_SCENE_LEVEL_TAG` | 53 | 49 |  + handler | 302115 / 3021 / `['69']` |
| `QUEST_EXEC_UNHIDE_SCENE_POINT` | 44 | 34 | enum + handler | 401108 / 4011 / `['3', '831']` |
| `QUEST_EXEC_SET_ABYSS_WAR_LEVEL_STATE` | 44 | 34 | enum + handler | 501103 / 5011 / `['106', '1']` |
| `QUEST_EXEC_UNLOCK_EVENTS_ITEM` | 43 | 43 | enum + handler | 400107 / 4001 / `['4001', '10107']` |
| `QUEST_EXEC_INC_DAILY_TASK_VAR` | 34 | 34 |  + handler | 2000313 / 20003 / `['29400', '1']` |
| `QUEST_EXEC_SET_ABYSS_WAR_LIMIT_REGION_STATE` | 33 | 26 | enum + handler | 501102 / 5011 / `['20238006', '4']` |
| `QUEST_EXEC_MODIFY_ARANARA_COLLECTION_STATE` | 31 | 30 |  + handler | 7309001 / 73090 / `['1', '1', '1']` |
| `QUEST_EXEC_CLEAR_VEHICLE` | 28 | 23 | enum + handler | 701220 / 7012 / `['3', '45007002']` |
| `QUEST_EXEC_ACTIVE_DAMSELETTE_FREE_MOON_PHASE` | 28 | 28 | enum + handler | 602502 / 6025 / `[]` |
| `QUEST_EXEC_ENTER_VEHICLE` | 23 | 23 | enum + handler | 701257 / 7012 / `['45007002', '3', '[3_18185:7662.397,221.350,7738.283,0.000,80.512,0.000]']` |
| `QUEST_EXEC_DEL_SCENE_TEMP_RES` | 21 | 21 | enum + handler | 701219 / 7012 / `['3', '0', '0']` |
| `QUEST_EXEC_REFRESH_WORLD_QUEST_FLOW_GROUP_SUITE` | 21 | 21 | enum + handler | 7301415 / 73014 / `['133303011,4']` |
| `QUEST_EXEC_ACTIVE_ACTIVITY_COND_STATE` | 18 | 16 |  + handler | 4000202 / 40002 / `['1001', '10017']` |
| `QUEST_EXEC_INACTIVE_ACTIVITY_COND_STATE` | 18 | 17 |  + handler | 4000205 / 40002 / `['1001', '10017']` |
| `QUEST_EXEC_REGISTER_DYNAMIC_GROUP_ONLY` | 17 | 17 |  + handler | 701207 / 7012 / `['133705072,133705078']` |
| `QUEST_EXEC_SET_TPS_GLASSES_CHAT_PROGRESS` | 15 | 15 | enum + handler | 7710233 / 77102 / `['10', '1']` |
| `QUEST_EXEC_CLEAR_FEATURE_TAG_VEHICLE` | 15 | 13 | enum + handler | 1504005 / 15040 / `['30019', '3']` |
| `QUEST_EXEC_MODIFY_CLIMATE_AREA` | 14 | 13 |  + handler | 1204209 / 12042 / `['3', '4', '0']` |
| `QUEST_EXEC_LOCK_MIRROR_AVATAR_TEAM` | 14 | 14 | enum + handler | 1503607 / 15036 / `['10035,10031;10035,10032', '1', '3']` |
| `QUEST_EXEC_RANDOM_CLOSED_QUEST_VAR` | 11 | 10 | enum + handler | 2400301 / 24003 / `['1', '1', '3']` |
| `QUEST_EXEC_MODIFY_DUNGEON_EXIT_POINT` | 9 | 9 | enum + handler | 303401 / 3034 / `['1314', '3', '2061']` |
| `QUEST_EXEC_HIDE_SCENE_POINT` | 8 | 8 | enum + handler | 7005101 / 70051 / `['3', '1218']` |
| `QUEST_EXEC_CHANGE_PLAYER_TRAIN_FIGURE_SGV` | 7 | 7 | enum + handler | 7767601 / 77676 / `['3', '14', '1']` |
| `QUEST_EXEC_ACTIVATE_SCENERY` | 6 | 6 | enum + handler | 4022301 / 40223 / `['10100102']` |
| `QUEST_EXEC_CLEAR_PERSISTENT_DUNGEON_SCENE` | 4 | 4 | enum + handler | 701218 / 7012 / `['51327']` |
| `QUEST_EXEC_LOCK_AVATAR_TEAM` | 4 | 4 |  + handler | 1110204 / 11102 / `['10000026']` |
| `QUEST_EXEC_CHANGE_SKILL_DEPOT` | 4 | 2 |  + handler | 200102 / 2001 / `['3']` |
| `QUEST_EXEC_GRANT_TRIAL_AVATAR_BATCH_AND_LOCK_TEAM_V2` | 4 | 4 | enum + handler | 4012419 / 40124 / `['1', '10013,72,73,74', '0']` |
| `QUEST_EXEC_GRANT_TRIAL_AVATAR_AND_LOCK_TEAM` | 3 | 3 |  + handler | 1202605 / 12026 / `['32']` |
| `QUEST_EXEC_GRANT_TRIAL_AVATAR_AND_LOCK_TEAM_V2` | 3 | 3 | enum + handler | 1302710 / 13027 / `['2', '63']` |
| `QUEST_EXEC_OPTIONAL_REVIVAL_TEAM` | 3 | 3 | enum + handler | 302825 / 3028 / `['1']` |
| `QUEST_EXEC_LOCK_AVATAR_TEAM_V2` | 3 | 3 | enum + handler | 4012407 / 40124 / `['1', '10000025', '10000080']` |
| `QUEST_EXEC_CREATE_VEHICLE` | 2 | 2 | enum + handler | 201002 / 2010 / `['45001001', '3', 'Q201002_Skiff']` |
| `QUEST_EXEC_ADD_ALCHEMY_SIM_CROP` | 2 | 2 | enum + handler | 4014402 / 40144 / `['1,4,16', '10,10,10']` |
| `QUEST_EXEC_ACTIVATE_PERSISTENT_DUNGEON_SCENE` | 2 | 2 | enum + handler | 501005 / 5010 / `['20238']` |
| `QUEST_EXEC_CHANGE_AVATAR_COSTUME` | 2 | 2 | enum + handler | 601714 / 6017 / `['10000005', '200501']` |
| `QUEST_EXEC_SHOW_MAP_LAYER_GROUP` | 2 | 2 | enum + handler | 7323205 / 73232 / `['33104']` |
| `QUEST_EXEC_UNLOCK_TPS_AVATAR` | 1 | 1 | enum + handler | 701215 / 7012 / `[]` |
| `QUEST_EXEC_ENTER_AQUARIUM_DIVING_DUNGEON` | 1 | 1 | enum + handler | 7470001 / 74700 / `['99']` |
| `QUEST_EXEC_SET_LIMIT_REGION_STATE` | 1 | 1 | enum + handler | 1504301 / 15043 / `['31001001', '0']` |
| `QUEST_EXEC_UNIQUE_RANDOM_QUEST_VAR` | 1 | 1 | enum + handler | 2503601 / 25036 / `['1,2,3', '1', '6']` |
| `QUEST_EXEC_SET_SCENE_VAR` | 1 | 1 | enum + handler | 7716008 / 77160 / `['3', 'Scenevar_GZJR', '0']` |
| `QUEST_EXEC_FINISH_ABYSS_WAR_ACCOUNT_PERFORMANCE` | 1 | 1 | enum + handler | 501308 / 5013 / `[]` |
| `QUEST_EXEC_SET_IS_DIVEABLE` | 1 | 1 | enum + handler | 7466801 / 74668 / `['1']` |
| `QUEST_EXEC_UNLOCK_SCENE_MP` | 1 | 1 | enum + handler | 7609623 / 76096 / `['103']` |

## How this was measured

```
python tools/quest-coverage-audit.py <resources dir>
# covered = enum constant exists in enums/QuestContent.java|QuestExec.java
#           AND a handler in quest/content|quest/exec carries @QuestValue(Content|Cond|Exec)(<type>)
# counts   = rows in QuestExcelConfigData.json finishCond/failCond (conditions)
#                                       beginExec/finishExec/failExec (execs)
```

Machine-readable form: `docs/quest-coverage-7.2-gaps.json`.

## Notes on scope

* Row counts are data volume, not importance; a single missing type can gate a whole story chain
  (`QUEST_CONTENT_GADGET_STATE_CHANGE` alone appears in 834 subquests).
* Implementing a type is two separate jobs: add the enum name, then find the **event source**
  (gadget state change, save point entry, weather area change, …) and fire the trigger from there.
  An enum name alone changes nothing.
* Example params in the tables are the first occurrence in the table and are meant as a starting
  point for semantic analysis, not as a specification.
