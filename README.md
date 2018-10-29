#  TFO2 Reel Logger

A python script that stores the Reel Log from [Trophy Fishing Online 2](http://trophyfishingonline.com/) into an SQLite database.

# To Run
Save your Reel Log as an HTML file (no need for images, etc--Not "Complete" in Chrome)
Run `db.py` from a python console with BeautifulSoup4 installed (pip install beautifulsoup4 or use the pipenv pipfile)
A single argument is needed for execution--the path the the HTML file (relative to the `db.py` script).
A reellog.db file will be produced in the same directory.

Use any SQLite3 viewer to view, such as [DB Browser for SQLite](http://sqlitebrowser.org/)
