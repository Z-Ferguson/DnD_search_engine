import psycopg2
from tabulate import tabulate

conn = psycopg2.connect("dbname=test user=zacharyferguson host=/tmp/")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS dnddata (
id serial PRIMARY KEY,
name text,
race text,
heroclass text,
alignment text,
age numeric,
height numeric,
level numeric,
background text,
faction text);""")

def import_dnd_data():
    with open("initial_data.csv") as f:
        fieldnames = ['name', 'race', 'heroclass', 'alignment', 'age', 'height', 'level', 'background', 'faction']
        dnd_data_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter = ', ')
        for row in dnd_data_reader:
            print(row)
        return dnd_data_reader
# cur.execute("""INSERT INTO dnddata (
# name, race, heroclass, alignment, age, height, level, background, faction)
#  VALUES ('Zach', 'human', 'paladin', 'lawful good', 26, 73, 20, 'coder', 'engineers')""")
#
#
# cur.execute("""INSERT INTO dnddata (
# name, race, heroclass, alignment, age, height, level, background, faction)
#  VALUES ('Cameron', 'elf', 'rogue', 'chaotic evil', 30, 71, 18, 'rapscallion', 'neutral')""")

# cur.execute("DELETE FROM dnddata;")

conn.commit()
cur.execute("SELECT * FROM dnddata;")

# print(tabulate(cur.fetchall(), tablefmt="fancy_grid", headers = ['name', 'race', 'heroclass', 'alignment', 'age', 'height', 'level', 'background', 'faction']))

if __name__ == '__main__':
    import_dnd_data()
