import sqlite3


class Helper:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.print_all()

    def increment(self, word):
        self.conn.execute("INSERT OR REPLACE INTO WORDS(word, count) \
                    VALUES('" + word + "', \
                    COALESCE((SELECT COUNT FROM WORDS WHERE \
                    WORD='" + word + "'), 0));"
        )
        self.conn.execute("UPDATE WORDS SET COUNT=COUNT+1 WHERE WORD='" + word + "';")


        #except sqlite3.OperationalError:
        #    self.conn.execute('''INSERT INTO WORDS (WORD,COUNT) \
        #        VALUES (?, ?)''', (word, 1))
        self.conn.commit()

    def print_all(self):
        cursor = self.conn.execute("SELECT word, count from WORDS")
        for row in cursor:
            print row[0] + ':' + str(row[1])
