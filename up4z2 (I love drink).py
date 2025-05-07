import sqlite3

# БД
con = sqlite3.connect("I_love_drink.db")
cursor = con.cursor()

# ингредиенты
cursor.execute("""CREATE TABLE IF NOT EXISTS ingredient
            (name TEXT PRIMARY KEY,
            price REAL,
            quantity REAL,
            drink INTEGER,
            strength REAL)
            """)
#  quantity для напитков рассчитывается в мл

# коктейль
cursor.execute("""CREATE TABLE IF NOT EXISTS cocktail
            (name TEXT PRIMARY KEY,
            price REAL,
            strength REAL)
            """)

# состав
cursor.execute("""CREATE TABLE IF NOT EXISTS ingred_cock
            (ingred_name TEXT REFERENCES ingredient (name),
            cock_name TEXT REFERENCES cocktail (name),
            cost REAL)
            """)
# cost - сколько ингредиента затрачивается на коктейль

# + кок
def cock_add(name, price):
    total_strength = 0
    total_V = 0
    # общий объём и крепость коктейля

    #создание состава
    ingred_name = "0"
    while ingred_name != "":
        ingred_name = input("ingredient name ")
        if ingred_name == "":
            break
        cost = float(input("cost "))
        cursor.execute("SELECT drink, strength FROM ingredient WHERE name=?", (ingred_name,))
        drink, strength = cursor.fetchone()

        if drink == 1:
            total_strength += strength / 100 * cost
            total_V += cost
        cursor.execute('''
                    INSERT INTO ingred_cock (ingred_name, cock_name, cost)
                    VALUES (?, ?, ?)
                ''', (ingred_name, name, cost))
        con.commit()
    total_strength = total_strength / total_V * 100
    # создание коктейля
    cursor.execute('''
                INSERT INTO cocktail (name, price, strength)
                VALUES (?, ?, ?)
            ''', (name, price, total_strength))
    con.commit()

# + ингред
def ingred_add(name, price, quantity, drink, strength):
    con = sqlite3.connect('I_love_drink.db')
    cursor = con.cursor()
    cursor.execute('''
                INSERT INTO ingredient (name, price, quantity, drink, strength)
                VALUES (?, ?, ?, ?, ?)''', (name, price, quantity, drink, strength))
    con.commit()

def check_ingred():
    con = sqlite3.connect('I_love_drink.db')
    cursor = con.cursor()
    cursor.execute('SELECT name, price, quantity FROM ingredient')
    for i in cursor.fetchall():
        print(i)

def check_cock():
    con = sqlite3.connect('I_love_drink.db')
    cursor1 = con.cursor()
    cursor2 = con.cursor()
    cursor1.execute('SELECT * FROM cocktail')
    for i in cursor1.fetchall():
        print(i)
        cursor2.execute('SELECT ingred_name FROM ingred_cock WHERE cock_name=?', (i[0], ))
        for j in cursor2.fetchall():
            print(j)

def sale(cock, quantity):
    cursor2 = con.cursor()
    cursor.execute('SELECT ingred_name, cost FROM ingred_cock WHERE cock_name=?', (cock, ))
    for i in cursor.fetchall():
        cursor2.execute('UPDATE ingredient SET quantity=? WHERE name=?', (i[1] * quantity, i[0]))
        con.commit()

# приход
def upd(ingred, quantity):
    cursor.execute('SELECT quantity FROM ingredient WHERE name=?', (ingred,))
    quantity += cursor.fetchone()[0]
    cursor.execute('UPDATE ingredient SET quantity=? WHERE name=?', (quantity, ingred))
    con.commit()

while True:
    comm = input("1 cock 2 ingred\ninfo 3 ingred 4 cock\nop 5 sale 6 upd\n- exit\n")
    if comm == "1":
        name = input("name ")
        price = float(input("price "))
        cock_add(name, price)
    elif comm == "2":
        name = input("name ")
        price = float(input("price "))
        quantity = float(input("quantity "))
        drink = int(input("1 drink - not "))
        strength = float(input("strength "))
        ingred_add(name, price, quantity, drink, strength)
    elif comm == "3":
        check_ingred()
    elif comm == "4":
        check_cock()
    elif comm == "5":
        cock = input("cock ")
        quantity = int(input("quantity "))
        sale(cock, quantity)
    elif comm == "6":
        ingred = input("name ")
        quantity = float(input("quantity "))
        upd(ingred, quantity)

    else:
        break


