import csv, sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

with open("csv's/PalData.csv") as datafile:
    data = csv.DictReader(datafile)
    for i in data:
        paldecknr = int(i['ZukanIndex'])
        if(paldecknr == -1):
            break

        name = i['Name']
        code = i['CodeName']

        to_db = [
            name,
            code
        ]
        cur.execute("INSERT INTO palname_to_code VALUES(?, ?);", to_db)

    con.commit()
    con.close()