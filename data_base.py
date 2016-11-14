import psycopg2
from tabulate import tabulate

conn = psycopg2.connect("dbname=test user=zacharyferguson host=/tmp/")
cur = conn.cursor()


def create_table():
    create_t = ("""CREATE TABLE IF NOT EXISTS dnddata (
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
    cur.execute(create_t)


def dumb_add():

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Zach', 'human', 'paladin', 'lawful good',
    25, 73, 12, 'soldier', 'order of the gauntlet')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Cameron', 'halfling', 'rogue', 'chaotic good',
    30, 38, 08, 'guild thief', 'the zhentarim')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Autumn', 'half-elf', 'cleric', 'lawful good',
    24, 53, 09, 'acolyte', 'the lords alliance')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Cody', 'dragonborn', 'warlock', 'chaotic evil',
    100, 58, 16, 'mercenary', 'the zhentarim')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Audri', 'elf', 'bard', 'true neutral',
    160, 52, 15, 'entertainer', 'the harpers')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Pheobe', 'gnome', 'sorcerer', 'neutral evil',
    80, 42, 12, 'noble', 'the lords alliance')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Roger', 'elf', 'sorceror', 'neutral good',
    120, 53, 11, 'traveler', 'the lords alliance')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('John', 'half-elf', 'ranger', 'chaotic good',
    38, 69, 10, 'traveler', 'emerald enclave')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Josiah', 'half-orc', 'barbarian', 'lawful evil',
    30, 60, 05, 'outlander', 'the harpers')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Tracy', 'half-elf', 'druid', 'lawful neutral',
    84, 52, 09, 'traveler', 'emerald enclave')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Max', 'human', 'monk', 'lawful good',
    30, 68, 11, 'sailor', 'order of the gauntlet')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Sam', 'human', 'fighter', 'neutral good',
    32, 70, 14, 'mercenary', 'order of the gauntlet')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Cameron', 'human', 'warlock', 'chaotic good',
    30, 68, 11, 'acolyte', 'the harpers')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Kevin', 'tiefling', 'wizard', 'neutral evil',
    90, 65, 15, 'noble', 'the zhentarim')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Roger', 'dwarf', 'rogue', 'true neutral',
    110, 43, 11, 'urchin', 'the harpers')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Zach', 'dwarf', 'barbarian', 'neutral evil',
    115, 44, 14, 'noble', 'the harpers')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Sarah', 'halfling', 'bard', 'chaotic neutral',
    29, 36, 01, 'jester', 'the lords alliance')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Daniel', 'half-orc', 'fighter', 'chaotic evil',
    34, 62, 01, 'outlander', 'order of the gauntlet')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Matt', 'dragonborn', 'paladin', 'lawful good',
    97, 58, 18, 'knight', 'order of the gauntlet')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Ryan', 'gnome', 'cleric', 'chaotic good',
    76, 44, 05, 'acolyte', 'the zhentarim')"""
    cur.execute(stats)

    stats = """INSERT INTO dnddata
    (name, race, heroclass, alignment, age, height, level, background, faction)
    VALUES('Josh', 'elf', 'ranger', 'true neutral',
    150, 53, 11, 'soldier', 'order of the gauntlet')"""
    cur.execute(stats)


def show_hero_data():
    print(tabulate(cur, tablefmt="fancy_grid",
                   headers=['name', 'race', 'heroclass', 'alignment',
                            'age', 'height', 'level',
                            'background', 'faction']))


def main():
    create_table()
    dumb_add()


if __name__ == "__main__":
    main()

conn.commit()

cur.close()
conn.close()
