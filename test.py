import sqlite3
def test(palname):       
    con = sqlite3.connect("Database/Paldata.db")
    cur = con.cursor()
    data = cur.execute("SELECT  paldecknr, palnr_suffix, name, size, element_1, element_2, hp, range_atk, defense, ai_response, slow_walk_speed, walk_speed, run_speed, ride_sprint_speed, max_stomach, food_amount, nocturnal, stamina, maleprob, breedingpower, igniting, watering, planting, electricity, handiwork, gathering, logging, mining, medicine, cooling, transporting, farming, mount, mounttype FROM pal WHERE name = ?", (palname,))
    paldecknr, palnr_suffix, name, size, ele1, ele2, hp, rangeatk, defense, ai_response, slow_walk_speed, walk_speed, run_speed, ride_sprint_speed, max_stomach, food_amount, nocturnal, stamina, maleprob, breedingpower, igniting, watering, planting, electricity, handiwork, gathering, logging, mining, medicine, cooling, transporting, farming, mount, mounttype = data.fetchone()

    data = cur.execute("SELECT imagelink FROM pal_images WHERE name = ?", (palname, ))
    img = data.fetchone()
    print(img[0])

    print("Paldecknr:", paldecknr)
    print("Palnr_suffix:", palnr_suffix)
    print("Name:", name)
    print("Size:", size)
    print("Element 1:", ele1)
    print("Element 2:", ele2)
    print("HP:", hp)
    print("Attack:", rangeatk)
    print("Defense:", defense)
    print("AI Response:", ai_response)
    print("Slow Walk Speed:", slow_walk_speed)
    print("Walk Speed:", walk_speed)
    print("Run Speed:", run_speed)
    print("Ride Sprint Speed:", ride_sprint_speed)
    print("Max Stomach:", max_stomach)
    print("Food Amount:", food_amount)
    print("Nocturnal:", nocturnal)
    print("Stamina:", stamina)
    print("Male/Female:", str(maleprob) + "/" + str(100-maleprob))
    print("Breeding Power:", breedingpower)
    print("Igniting:", igniting)
    print("Watering:", watering)
    print("Planting:", planting)
    print("Electricity:", electricity)
    print("Handiwork:", handiwork)
    print("Gathering:", gathering)
    print("Logging:", logging)
    print("Mining:", mining)
    print("Medicine:", medicine)
    print("Cooling:", cooling)
    print("Transporting:", transporting)
    print("Farming:", farming)
    print("Mount:", mount)
    print("Mount Type:", mounttype)

test("Mossanda")

#overall
# paldecknr + suffix, name, size, ele1 and 2, nocturnal, male prob, breedingpower

# combat
# hp, atk, def, ai response

# speeds
# all speed stuff plus mount, stamina, 

# work
# the work suitabilities and food

#partner skill
# partner skill with desc