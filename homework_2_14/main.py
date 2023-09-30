import sqlite3
import random

toy_names = [['Teddy', 'Stuffed Animal'],
            ['Barbie', 'Fashion Doll'],
            ['LEGO', 'Building Blocks'],
            ['Hot Wheels', 'Die-cast Cars'],
            ['Mr. Potato Head', 'Action Figure'],
            ['Cabbage Patch Kids', 'Doll'],
            ['Rubik\'s Cube', 'Puzzle Toy'],
            ['Beanie Babies', 'Plush Collectibles'],
            ['Etch A Sketch', 'Drawing Toy'],
            ['G.I. Joe', 'Action Figure'],
            ['My Little Pony', 'Collectible Figurine'],
            ['Furby', 'Electronic Toy'],
            ['Nerf Blaster', 'Foam Dart Gun'],
            ['Play-Doh', 'Modeling Compound'],
            ['Tickle Me Elmo', 'Interactive Plush Toy']]

with sqlite3.connect('homework_2_14\\toys.db') as db:
    cr = db.cursor()
    cr.execute('''
        CREATE TABLE IF NOT EXISTS toys (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT,
            price REAL,
            stock_quantity INTEGER
        )
    ''')

    a = 0
    for _ in range(15):
        cr.execute('''
            INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)''', (toy_names[a][0], toy_names[a][1], round(random.uniform(0.50, 100.00), 2), random.randint(0, 100)))
        a += 1

    cr.execute("SELECT * FROM toys")
    for row in cr.fetchall():
        print(row)

    cr.execute('''
        DELETE FROM toys
        WHERE stock_quantity <= 0
    ''')

    cr.execute('''
        UPDATE toys
        SET stock_quantity = stock_quantity + 5
        WHERE id = 3 
    ''') # Не зрозуміла, під "Збільште кількість на складі на 5 одиниць." мається на увазі для всіх товарів чи тільки одного. У коді зробила для одного, а щоб збільшити для всіх, потрібно прибрати рядок "WHERE id = 3"

    cr.execute('''
        SELECT name FROM toys
    ''')
    for row in cr.fetchall():
        print(row)

    cr.execute('''
        SELECT name, price FROM toys
        WHERE price < 20
    ''')
    for row in cr.fetchall():
        print(row)

    cr.execute('''
        SELECT type, COUNT(*) AS stock_quantity FROM toys
        GROUP BY type
    ''')
    for row in cr.fetchall():
        print(row)

    cr.execute('''
        SELECT name, stock_quantity FROM toys
        WHERE stock_quantity < 10
    ''')
    for row in cr.fetchall():
        print(row)