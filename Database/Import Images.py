import csv, sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

with open("csv's/image import.csv") as datafile:
    data = csv.DictReader(datafile)
    for i in data:
        paldecknr = int(i['ZukanIndex'])
        name = i['Name']
        imagelink = i['imagelink']

        to_db = [
            paldecknr,
            name,
            imagelink
        ]
        cur.execute("INSERT INTO pal_images VALUES(?, ?, ?);", to_db)
    con.commit()
    con.close()    
