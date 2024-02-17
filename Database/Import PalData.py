import csv, sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

with open("PalData.csv") as datafile:
    data = csv.DictReader(datafile)
    for i in data:
        paldecknr = int(i['ZukanIndex'])
        if(paldecknr == -1):
            break

        palnr_suffix = i['ZukanIndexSuffix']
        name = i['Name']
        size = i['Size'][14:]
        element_1 = i['ElementType1'][17:] 
        element_2 = i['ElementType2'][17:]
        hp = int(i['HP'])
        melee_atk = int(i['MeleeAttack'])
        range_atk = int(i['ShotAttack'])
        defense = int(i['Defense'])
        support = int(i['Support'])
        craftspeed = int(i['CraftSpeed'])
        ai_response = i['AIResponse']
        slowwalk = int(i['SlowWalkSpeed'])
        walk = int(i['WalkSpeed'])
        run = int(i['RunSpeed'])
        ride = int(i['RideSprintSpeed'])
        maxstomach = int(i['MaxFullStomach'])
        foodamount = int(i['FoodAmount'])
        nocturnal = i['Nocturnal']
        stam = int(i['Stamina'])
        maleprob = int(i['MaleProbability'])
        breedpower = int(i['CombiRank'])
        ignite = int(i['WorkSuitability_EmitFlame'])
        watering = int(i['WorkSuitability_Watering'])
        planting = int(i['WorkSuitability_Seeding'])
        elec = int(i['WorkSuitability_GenerateElectricity'])
        handiwork = int(i['WorkSuitability_Handcraft'])
        gathering = int(i['WorkSuitability_Collection'])
        logging = int(i['WorkSuitability_Deforest'])
        mining = int(i['WorkSuitability_Mining'])
        oil = int(i['WorkSuitability_OilExtraction'])
        medicine = int(i['WorkSuitability_ProductMedicine'])
        cooling = int(i['WorkSuitability_Cool'])
        transporting = int(i['WorkSuitability_Transport'])
        farming = int(i['WorkSuitability_MonsterFarm'])
        mount = i['Mount']
        mounttype = i['Mount Type']

        if (i['ZukanIndexSuffix'] == ''):
            palnr_suffix = None
        if(i['ElementType2'] == ''):
            element_2 = None
        if(i['Mount'] == ''):
            mount = False
        if(i['Mount Type'] == ''):
            mounttype = None

        to_db = [
            paldecknr,
            palnr_suffix,
            name,
            size,
            element_1,
            element_2,
            hp,
            melee_atk,
            range_atk,
            defense,
            support,
            craftspeed,
            ai_response,
            slowwalk,
            walk,
            run,
            ride,
            maxstomach,
            foodamount,
            nocturnal,
            stam,
            maleprob,
            breedpower,
            ignite,
            watering,
            planting,
            elec,
            handiwork,
            gathering,
            logging,
            mining,
            oil,
            medicine,
            cooling,
            transporting,
            farming,
            mount,
            mounttype
        ]
        cur.execute("INSERT INTO pal VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

    con.commit()
    con.close()