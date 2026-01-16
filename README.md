# Contact Tracker  
Logan, Logan  

## Dice Thingy Description  
This program simulates rolling multiple dice and continues rerolling until all dice show the same value.  
It uses helper functions to roll dice, display them, count frequencies, find the mode, and reroll unmatched dice.

### Dice Thingy Flowchart
mermaid
graph TD;
  Main-->first_roll;
  first_roll-->output_dice;
  first_roll-->find_mode;
  find_mode-->list_unmatched_dice;
  list_unmatched_dice-->reroll_many;
  reroll_many-->output_dice;
  reroll_many-->find_mode;

## Function Diagrams
| `main`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: none` | takes no input                |       |
| `.returns: none`  |                               |       |
| `description`     | controls overall program flow |       |

| `output_dice`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: dice` | a list of dice                |       |
| `.returns: none`  |                               |       |
| `description`     | outputs die in  the list |       |

| `roll_die`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: none` | takes no input                |       |
| `.returns: int`  |         returns integer                  |       |
| `description`     | generates random integer from 1-6 |       |

| `first_roll`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: none` | takes no input                |       |
| `.returns: list`  |      list         |       |
| `description`     | uses roll_die to generate list of 12 int |       |
    
| `count_frequency`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: dice, die` | list of 12 int, target die               |       |
| `.returns: int`  |      frequency         |       |
| `description`     | how often target dice occurs in list |       |
  
| `find_mode`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: dice` | dice: list               |       |
| `.returns: int`  |      mode       |       |
| `description`     | uses count_frequency to determine how often each dice occurs |       |

| `list_unmatched_dice`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: dice` | dice: list               |       |
| `.returns: list`  |      list of indexes to reroll       |       |
| `description`     | determines which dice need rerolled |       |

| `reroll_one`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: dice, index` | dice: list index: int              |       |
| `.returns: list`  |      list of indexes to reroll       |       |
| `description`     | uses roll_die to reroll that index, replaces index with new roll and returns list |       |

| `reroll_many`            |                               | logan |
| ----------------- | ----------------------------- | ----- |
| `.argument: dice` | dice: list               |       |
| `.returns: list`  |      list of rerolled die      |       |
| `description`     | calls list_unmatched_dice() and reroll_one() to reroll each die|       |