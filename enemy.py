import enemy
import json

with open('enemyData.json','r') as f:
    data=json.load(f)

en_attackerHealth=data["enemy"][0]["health"]
en_sppedsterHealth=data["enemy"][1]["health"]
en_tankHealth=data["enemy"][2]["health"]

def en_dmg(attacker_dmg:int,speedster_dmg:int,tank_dmg:int):

    new_attackerHealth=en_attackerHealth-attacker_dmg
    en_healthUpdate.attacker_healthUpdate(new_attackerHealth)

    new_speedsterHealth=en_sppedsterHealth-speedster_dmg
    en_healthUpdate.speedster_healthUpdate(new_speedsterHealth)

    new_tankHealth=en_tankHealth-tank_dmg
    en_healthUpdate.tank_healthUpdate(new_tankHealth)

class en_healthUpdate():
    def attacker_healthUpdate(updateAttacker:int):

        data["enemy"][0]["health"]=updateAttacker  
        with open('enemyData.json','w') as f:
            json.dump(data,f)

    def speedster_healthUpdate(updateSpeedster:int):
        data["enemy"][1]["health"]=updateSpeedster
        with open('enemyData.json','w') as f:
            json.dump(data,f)

    def tank_healthUpdate(updateTank:int):
        data["enemy"][2]["health"]=updateTank
        with open('enemyData.json','w') as f:
            json.dump(data,f)