import sqlite3
import Scraper
import sys


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


def parse_and_store(html_file_path):
    conn = sqlite3.connect('reellog.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(*) from reellog")
    (old_entry_count, ) = c.fetchone()

    to_write = Scraper.scrape(html_file_path)

    for row in to_write:
        command = "INSERT INTO reellog VALUES (%s)" % row
        try:
            c.execute(command)
            print('+ %s' % row)
        except sqlite3.IntegrityError:
            print('= %s' % row)

    conn.commit()

    c.execute("SELECT COUNT(*) from reellog")
    (new_entry_count,) = c.fetchone()

    conn.close()

    print("%i new entries added" % (int(new_entry_count) - int(old_entry_count)))


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Need one argument: path to html_file", file=sys.stderr)
        sys.exit(1)

    # create_db()
    parse_and_store(sys.argv[1])
    # sample_db_entry()

    print('Done')
