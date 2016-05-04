import sqlite3


class Helper:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.print_all()

    def add(self, word):
        cursor = self.conn.execute('''SELECT * from WORDS where WORD=''' + word)
        count = cursor[0][1] + 1
        self.conn.execute("UPDATE WORDS set COUNT = " + str(count) + " where WORD=" + word)
        #except sqlite3.OperationalError:
        #    self.conn.execute('''INSERT INTO WORDS (WORD,COUNT) \
        #        VALUES (?, ?)''', (word, 1))
        self.conn.commit()

    def print_all(self):
        cursor = self.conn.execute("SELECT word, count from WORDS")
        for row in cursor:
            print row[0] + ':' + str(row[1])
