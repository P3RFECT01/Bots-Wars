import curses
from curses import wrapper
from curses import *
import json

with open('json\playerData.json','r') as f:
    data=json.load(f)


arena=f'''
 ________________________________________________________ 
|                  |                  |                  |
|     Attacker     |      Tank        |    Speedster     |
|------------------|------------------|------------------|
| Stats:           | Stats:           | Stats:           |
| Health: 00       | Health: 00       | Health: 00       |
|__________________|__________________|__________________|
|__________________|__________________|__________________|
|                  |                  |                  |
|     Attacker     |      Tank        |    Speedster     |
|------------------|------------------|------------------|
| Stats:           | Stats:           | Stats:           |
| Health:  {data["player"][0]["health"]}      | Health:  {data["player"][1]["health"]}      | Health:  {data["player"][2]["health"]}      |
| Attack:  {data["player"][0]["attack"]}      | Attack:  {data["player"][1]["attack"]}      | Attack:  {data["player"][2]["attack"]}      |
| Defence: {data["player"][0]["defence"]}      | Defence: {data["player"][1]["defence"]}      | Defence: {data["player"][2]["defence"]}      |
| Speed:   {data["player"][0]["speed"]}      | Speed:   {data["player"][0]["defence"]}      | Speed:   {data["player"][0]["defence"]}      |
|__________________|__________________|__________________|
|                  |       [X]        |                  |
|░░░░░░░░░░░░░░░░░░|      MOVES       |░░░░░░░░░░░░░░░░░░|
|__________________|__________________|__________________| 

'''

movesBox='''

'''

def main(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.addstr(arena)

wrapper(main)


