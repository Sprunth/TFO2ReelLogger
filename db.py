import sqlite3
import Scraper


def create_db():
    conn = sqlite3.connect('reellog.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE reellog
    (lure text, body text, location text, species text, level integer, weight real, class text,
    unique(lure, body, location, species, level, weight, class))''')

    conn.commit()
    conn.close()


def sample_db_entry():
    scrape_data = "'Culprit Worm', 'Amazon River', 'Baia de Santa Rosa', 'Matrincha', '6', '0.062', 'Wimpy III'"
    command = "INSERT INTO reellog VALUES (%s)" % scrape_data

    conn = sqlite3.connect('reellog.db')
    c = conn.cursor()

    c.execute(command)

    conn.commit()
    conn.close()


def parse_and_store():
    conn = sqlite3.connect('reellog.db')
    c = conn.cursor()

    to_write = Scraper.scrape()

    for row in to_write:
        command = "INSERT INTO reellog VALUES (%s)" % row
        try:
            c.execute(command)
        except sqlite3.IntegrityError:
            print('duplicate entry: %s', row)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    # create_db()
    parse_and_store()
    # sample_db_entry()

    print('Done')
