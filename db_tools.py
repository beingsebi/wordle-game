import sqlite3


def disk_db():
    try:
        return sqlite3.connect('words.db')
    except Exception as e:
        print(e)
        return None


# def mem_db():
#     try:
#         new_db = sqlite3.connect(':memory:')
#         old_db = disk_db()
#         query = "".join(line for line in old_db.iterdump())
#         new_db.executescript(query)
#         return new_db
#     except Exception as e:
#         print(e)
#         return None


def print_words(conn):
    try:
        # conn = sqlite3.connect('words.db')
        c = conn.cursor()
        c.execute("SELECT * FROM words")
        for x in c.fetchall():
            print(x)
        conn.close()
    except Exception as e:
        print(e)
        return None


def get_word_by_id(id, conn):
    try:
        # conn = sqlite3.connect('words.db')
        c = conn.cursor()
        c.execute("SELECT word FROM words where id=?", (id,))
        return c.fetchone()[0]
    except Exception as e:
        print(e)
        return None


def get_all_words(conn):
    try:
        # conn = sqlite3.connect('words.db')
        c = conn.cursor()
        c.execute("SELECT word FROM words")
        axc = [x[0] for x in c.fetchall()]
        if len(axc):
            return axc
    except Exception as e:
        print(e)
        return None


# print(len(get_all_words(disk_db())))
# l = get_all_words(disk_db())
# for i in l:
#     if len(i) != 5 or not i.isupper() or not i.isalpha:
#         print(i)
