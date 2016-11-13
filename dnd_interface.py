# import sys
import os
import psycopg2
from data_base import *
from tabulate import tabulate

conn = psycopg2.connect("dbname=test user=zacharyferguson host=/tmp/")

cur = conn.cursor()


# class HeroInterface:
#
#     def __init__(self):
#         pass
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class DatabaseInteraction:
    def __init__(self):
        pass

    def add_hero(self):
        name = input("Name? ")
        race = input("Race? ")
        heroclass = input("Class? ")
        alignment = input("Alignment? ")
        age = input("Age? ")
        height = input("Height? ")
        level = input("Level? ")
        background = input("Background? ")
        faction = input("Faction? ")

        sql = "INSERT INTO dnddata (name, race, heroclass, alignment, age, height, level, background, faction) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (name, race, heroclass, alignment, age, height, level, background, faction))
        conn.commit()

    def show_hero_data(self):
        cur.execute("SELECT * FROM dnddata ORDER BY id ASC;")
        # print(tabulate(cur.fetchall(), tablefmt="fancy_grid", headers = ['name', 'race', 'heroclass', 'alignment', 'age', 'height', 'level', 'background', 'faction']))
        print(tabulate(cur, tablefmt="fancy_grid", headers =['name',
        'race', 'heroclass', 'alignment', 'age', 'height', 'level',
        'background', 'faction' ]))

    def delete_hero(self):
        # show_hero_data(self)
        hero_id = input("which name would you like to delete? ")
        sql = "DELETE FROM dnddata WHERE id =%s"
        cur.execute(sql, (hero_id,))
        conn.commit()

    def update_hero(self):
        # self.show_hero_data()
        ui_id = int(input("which id would you like to update? "))
        select = ("SELECT * FROM dnddata WHERE id=%s")
        cur.execute(select, (ui_id, ))
        clear()
        print(tabulate(cur, tablefmt="fancy_grid", headers =['name',
        'race', 'heroclass', 'alignment', 'age', 'height', 'level',
        'background', 'faction' ]))
        print("What would you like to change?")
        spec = input(
        """Select what you would like to update:
        (N)ame\n(R)ace\n(H)eroclass\n(Al)ignment\n(A)ge\n(He)ight\n(L)evel\n(B)ackground\n(F)action\n """).lower()
        new_name = input("Enter a new value ")
        if spec == 'n':
            change = ("UPDATE dnddata SET name=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'r':
            change = ("UPDATE dnddata SET race=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'h':
            change = ("UPDATE dnddata SET heroclass=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'al':
            change = ("UPDATE dnddata SET alignment=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'a':
            change = ("UPDATE dnddata SET age=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'he':
            change = ("UPDATE dnddata SET height=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'l':
            change = ("UPDATE dnddata SET level=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'b':
            change = ("UPDATE dnddata SET background=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        elif spec == 'f':
            change = ("UPDATE dnddata SET faction=%s WHERE id=%s")
            cur.execute(change, (new_name, ui_id))
            conn.commit()
        clear()
        self.show_hero_data()
        # return_to_main() #make into a funcrtion

def main():
    h_db = DatabaseInteraction()
    # h_db.add_hero()
    h_db.update_hero()
    # h_db.show_hero_data()
    # h_db.delete_hero()

main()
