import sqlite3

def calc(parent1, parent2):
    con = sqlite3.connect("Database/Paldata.db")
    cur = con.cursor()
    unique_Combo = False

    data_child = cur.execute("SELECT child FROM unique_combo WHERE parent1 = ? and parent2 = ?", (parent1, parent2,))
    name_child = data_child.fetchone()

    if(name_child is None):
        unique_Combo = True
    else:
        name_child = name_child[0]

    data_parent1 = cur.execute("SELECT paldecknr, palnr_suffix, name, breedingpower FROM pal WHERE name = ?", (parent1,))        
    paldecknr1, palnr_suffix1, name1, breedingpower1 = data_parent1.fetchone()

    data_parent2 = cur.execute("SELECT paldecknr, palnr_suffix, name, breedingpower FROM pal WHERE name = ?", (parent2,))
    paldecknr2, palnr_suffix2, name2, breedingpower2 = data_parent2.fetchone()

    if(unique_Combo):    
        breedingpower_child = (breedingpower1+breedingpower2)/2
        data_child  = cur.execute("SELECT paldecknr, palnr_suffix, name FROM pal WHERE palnr_suffix is NULL AND name NOT IN (SELECT child FROM unique_combo) ORDER BY ABS(? - breedingpower) LIMIT 1", (breedingpower_child,))
        paldecknr_child, palnr_suffix_child, name_child = data_child.fetchone()

    else:
        data_child = cur.execute("Select paldecknr, palnr_suffix, name FROM pal WHERE name = ?", (name_child,))
        paldecknr_child, palnr_suffix_child, name_child = data_child.fetchone()
        
    con.close()

    return name1, name2, name_child

def fill_all_combo():
    con = sqlite3.connect("Database/Paldata.db")
    cur = con.cursor()

    all_names = cur.execute("SELECT name FROM pal")
    namelist1 = all_names.fetchall()
    namelist2 = namelist1

    all_combo_list = []
    for i in namelist1:
        parent1 = i[0]
        for j in namelist2:
            parent2 = j[0]
            parentname1, parentname2, childname = calc(parent1, parent2)
            combotuple = (parentname1, parentname2, childname)
            all_combo_list.append(combotuple)

    #print(all_combo_list)
    cur.executemany("INSERT INTO all_combo_pal_breeding(parent1, parent2, child) VALUES(?,?,?)", all_combo_list)
    con.commit()
    con.close()

fill_all_combo()