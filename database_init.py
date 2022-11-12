import sqlite3
import words


def create_table_once():
    try:
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        command = """ CREATE TABLE IF NOT EXISTS words (
                                        id integer PRIMARY KEY,
                                        word text NOT NULL ); """
        c.execute(command)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return None


def insert_words_once():
    try:
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        lw = [(x,) for x in words.get_words()]
        c.executemany("INSERT INTO words (word) VALUES(?);", lw)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        return None


# create_table_once()
# insert_words_once()
# import db_tools
# db_tools.print_words()
