from tinydb import TinyDB, Query
from datetime import date, timedelta

""" 
To make an newsletter for a specific week (eg week 1) last possible occasion 
to do it is on Monday of that specific week (week 1). On Tuesday newsletter is made for a 
following week (week 2). Timdelta correction below takes into account this and a fact 
that datetime library consideres week 1 to be the year's first week that starts from Monday,
which differs from finnish convention. Correction is different every year.
"""
week = (date.today() + timedelta(days=13)).strftime('%W')


# TODO 
# -save also a preview for contents of news letter. This could be shown in GUI to 
#  give an idea how much content there already is in the news letter.
db = TinyDB(f'data/week{week}.json')
entries = Query()

def saveEntry(dict):
    db.insert(dict)

def allEntries():
    return db.all()

def entriesFromCategory(cat):
    return db.search(entries.category == cat)
