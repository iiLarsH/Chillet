import csv, sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

with open("csv's/Partner skills.csv") as datafile:
    data = csv.DictReader(datafile)
    for i in data:
        palname = i['Pal']
        data = cur.execute("SELECT paldecknr FROM pal WHERE name = ?", (palname.strip(),))
        nr = data.fetchone()
        partnerskill = i['Partner Skill']
        desc = i['Description']

        to_db = [
            nr[0],
            palname,
            partnerskill,
            desc
        ]
        cur.execute("INSERT INTO pal_partner_skills VALUES(?, ?, ?, ?);", to_db)
    con.commit()
    con.close()    
