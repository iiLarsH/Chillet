import sqlite3

con = sqlite3.connect("Database/Paldata.db")
cur = con.cursor()

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Relaxaurus", "Sparkit", "Relaxaurus Lux"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Sparkit", "Relaxaurus", "Relaxaurus Lux"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Incineram", "Maraith", "Incineram Noct"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Maraith", "Incineram", "Incineram Noct"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Pengullet", "Mau", "Mau Cryst"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Mau", "Pengullet", "Mau Cryst"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Foxcicle", "Vanwyrm", "Vanwyrm Cryst"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Vanwyrm", "Foxcicle", "Vanwyrm Cryst"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Surfent", "Eikthyrdeer", "Eikthyrdeer Terra"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Eikthyrdeer", "Surfent", "Eikthyrdeer Terra"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Hangyu", "Elphidran", "Elphidran Aqua"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Elphidran", "Hangyu", "Elphidran Aqua"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Pyrin", "Katress", "Pyrin Noct"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Katress", "Pyrin", "Pyrin Noct"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Wumpo", "Mammorest", "Mammorest Cryst"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Mammorest", "Wumpo", "Mammorest Cryst"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Grizzbolt", "Mossanda", "Mossanda Lux"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Mossanda", "Grizzbolt", "Mossanda Lux"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Rayhound", "Dinossom", "Dinossom Lux"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Dinossom", "Rayhound", "Dinossom Lux"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Jolthog", "Pengullet", "Jolthog Cryst"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Pengullet", "Jolthog", "Jolthog Cryst"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Frostallion", "Helzephyr", "Frostallion Noct"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Helzephyr", "Frostallion", "Frostallion Noct"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Kingpaca", "Reindrix", "Ice Kingpaca"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Reindrix", "Kingpaca", "Ice Kingpaca"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Lyleen", "Menasting", "Lyleen Noct"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Menasting", "Lyleen", "Lyleen Noct"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Leezpunk", "Flambelle", "Leezpunk Ignis"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Flambelle", "Leezpunk", "Leezpunk Ignis"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Blazehowl", "Felbat", "Blazehowl Noct"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Felbat", "Blazehowl", "Blazehowl Noct"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Robinquill", "Fuddler", "Robinquill Terra"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Fuddler", "Robinquill", "Robinquill Terra"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Broncherry", "Fuack", "Broncherry Aqua"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Fuack", "Broncherry", "Broncherry Aqua"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Surfent", "Dumud", "Surfent Terra"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Dumud", "Surfent", "Surfent Terra"))	

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Gobfin", "Rooby", "Gobfin Ignis"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Rooby", "Gobfin", "Gobfin Ignis"))	

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Suzaku", "Jormuntide", "Suzaku Aqua"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Jormuntide", "Suzaku", "Suzaku Aqua"))	

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Foxcicle", "Reptyro", "Ice Reptyro"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Reptyro", "Foxcicle", "Ice Reptyro"))	

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Hangyu", "Swee", "Hangyu Cryst"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Swee", "Hangyu", "Hangyu Cryst"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Mossanda", "Petallia", "Lyleen"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Petallia", "Mossanda", "Lyleen"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Vanwyrm", "Anubis", "Faleris"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Anubis", "Vanwyrm", "Faleris"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Mossanda", "Rayhound", "Grizzbolt"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Rayhound", "Mossanda", "Grizzbolt"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Grizzbolt", "Relaxaurus", "Orserk"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Relaxaurus", "Grizzbolt", "Orserk"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Astegon", "Kitsun", "Shadowbeak"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Kitsun", "Astegon", "Shadowbeak"))

cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Frostallion", "Frostallion", "Frostallion"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Jetragon", "Jetragon", "Jetragon"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Paladius", "Paladius", "Paladius"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Necromus", "Necromus", "Necromus"))
cur.execute("INSERT INTO unique_combo(parent1, parent2, child) VALUES(?, ?, ?)", ("Jormuntide Ignis", "Jormuntide Ignis", "Jormuntide Ignis"))

con.commit()
con.close()