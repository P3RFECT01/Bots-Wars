#imports 
import json
import random
#import enemy

#json file refrence
with open('json\playerData.json','r') as f:
    data=json.load(f)

#player: bot's health
pl_attackerHealth=data["player"][0]["health"]
pl_sppedsterHealth=data["player"][1]["health"]
pl_tankHealth=data["player"][2]["health"]

pl_attackerAttack=data["player"][0]["attack"]
pl_speedsterAttack=data["player"][1]["attack"]
pl_tankAttack=data["player"][2]["attack"]

#player: bot's defence
pl_attackerDefence=6
pl_speedsterDefence=3
pl_tankDefence=10

#player: Damage to bots
def pl_dmg(attacker_dmg:int,speedster_dmg:int,tank_dmg:int):

    #player_attacker: Damage given & updating it
    new_attackerHealth=pl_attackerHealth-attacker_dmg
    pl_healthUpdate.attacker_healthUpdate(new_attackerHealth)

    #player_speedster: Damage given & updating it
    new_speedsterHealth=pl_sppedsterHealth-speedster_dmg
    pl_healthUpdate.speedster_healthUpdate(new_speedsterHealth)

    #player_tank: Damage given & updating it
    new_tankHealth=pl_tankHealth-tank_dmg
    pl_healthUpdate.tank_healthUpdate(new_tankHealth)

#player: bot's health reset -> "50"
def pl_healthReset():

    data["player"][0]["health"]=50
    data["player"][1]["health"]=50
    data["player"][2]["health"]=50

    with open('playerData.json','w') as f:
        json.dump(data,f)


class pl_healthUpdate():
    def attacker_healthUpdate(updateAttacker:int):

        data["player"][0]["health"]=updateAttacker
        with open('playerData.json','w') as f:
            json.dump(data,f)

    def speedster_healthUpdate(updateSpeedster:int):
        data["player"][1]["health"]=updateSpeedster
        with open('playerData.json','w') as f:
            json.dump(data,f)

    def tank_healthUpdate(updateTank:int):
        data["player"][2]["health"]=updateTank
        with open('playerData.json','w') as f:
            json.dump(data,f)

#def pl_attack(attackAttacker:bool,attackSpeedster:bool,attackTank:bool):
#    if attackAttacker==True:
#        enemy.en_dmg(pl_attackerAttack,0,0)
#    else:
#        pass
#
#    if attackSpeedster==True:
#        enemy.en_dmg(0,pl_speedsterAttack,0)
#    else:
#        pass
#
#    if attackTank==True:
#        enemy.en_dmg(0,0,pl_tankAttack)
#    else:
#        pass
    


def pl_block(blockerAttacker:bool,blockerSpeedster:bool,blockerTank:bool):
    
    if blockerAttacker==True:
        blockageAttacker=random.randint(0,pl_attackerDefence)
    elif blockerAttacker==False:
        blockageAttacker=0

        
    if blockerSpeedster==True:
        blockageSpeedster=random.randint(0,pl_speedsterDefence)
    elif blockerSpeedster==False:
        blockageSpeedster=0

        
    if blockerTank==True:
        blockageTank=random.randint(0,pl_tankDefence)
    elif blockerTank==False:
        blockageTank=0

        pl_dmg(+blockageAttacker,+blockageSpeedster,+blockageTank)