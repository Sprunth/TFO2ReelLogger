from bs4 import BeautifulSoup
from pprint import pprint
from functools import reduce
import sys


def scrape(html_file_path):

    soup = BeautifulSoup(open(html_file_path), 'html.parser')

    rows = soup.find_all('tr')

    commands = list()

    for row in rows[1:]:
        cols = row.find_all('td')

        lure_string = list(cols[0].descendants)[0]
        lure = lure_string.find_all('img')[0].string.strip()

        body_of_water = cols[1].string

        location = cols[2].string

        fish_string = cols[3]
        fish_type = fish_string.font.string
        fish_level = fish_string.img.string.split()[-1]

        size_strings = list(map(lambda x: x.string, cols[4].find_all('font')))
        weight_idx = -1
        for idx in range(len(size_strings)):
            if 'lb' in size_strings[idx]:
                weight_idx = idx
                break
        weight = size_strings[weight_idx].split()[0]
        fish_class = reduce(lambda x, y: "%s %s" % (x, y), size_strings[weight_idx+1:])
        if 'L e g e n d a r y' in fish_class:
            fish_class = 'Legendary'
        elif 'B R U I S E R' in fish_class:
            fish_class = 'Bruiser'

        # size not stored for now
        # size = reduce(lambda x, y: "%s %s" % (x, y), size_strings[:-3])

        command = "'%s', '%s', '%s', '%s', '%s', '%s', '%s'" % (lure, body_of_water, location, fish_type, fish_level,
                                                                weight, fish_class)
        commands.append(command)

    return commands

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Need one argument: path to html_file", file=sys.stderr)
        sys.exit(1)

    scrape_data = scrape(sys.argv[1])
    pprint(scrape_data)
