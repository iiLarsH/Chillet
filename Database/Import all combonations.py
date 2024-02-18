import csv, sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

with open("csv's/Palworld breeding All Combos.csv") as datafile:
    data = csv.DictReader(datafile)

    count = 0
    for i in data:
        if(count == 0):
            parent1 = i['1']
            parent2 = list(i.values())
            count+=1
        else:
            child = i['1']
            message = parent1 + f" + {parent2[count]} = " + child
            count+=1
            print(message)

    #     to_db = [
    #         parent1,
    #         parent2,
    #         child
    #     ]
    #     cur.execute("INSERT INTO pal_images VALUES(?, ?, ?);", to_db)
    # con.commit()
    # con.close()    

import csv, sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

with open("csv's/Palworld breeding All Combos.csv") as datafile:
    data = csv.DictReader(datafile)

    for i in data:
        if(i['0'] != ""):
            y_axis = i['0'] # Y axis
            print(y_axis)

    # count = 1 
    # for i in data:
    #     x_axis = list(i.values()) # Y axis
    #     print(x_axis[count])
    # # Y axis of all pal names
