from tinydb import TinyDB, Query
from datetime import date, timedelta

""" 
To make an newsletter for a specific week (eg week 1) last possible occasion 
to do it is on Monday of that specific week (week 1). On Tuesday newsletter is made for the 
following week (week 2). Timdelta correction below takes into account this and a fact 
that datetime library consideres week 1 to be the year's first week that starts from Monday,
which differs from finnish convention. Correction is different every year.
"""
week = (date.today() + timedelta(days=13)).strftime('%W')


# TODO 
# -save also a preview for contents of news letter. This could be shown in GUI to 
#  give an idea how much content there already is in the news letter.
entries = Query()


def saveEntry(dict, isEnglish=False):
    if isEnglish:
        path = f'data/week{week}-en.json'
    else:
        path = f'data/week{week}.json'

    db = TinyDB(path)
    db.insert(dict)



def entriesFromCategory(cat, isEnglish=False):
    if isEnglish:
        path = f'data/week{week}-en.json'
    else:
        path = f'data/week{week}.json'

    db = TinyDB(path)
    return db.search(entries.category == cat)



def allEntries(isEnglish=False):
    if isEnglish:
        path = 'data/week' + week + '-en.json'
    else:
        path = 'data/week' + week + '.json'
    db = TinyDB(path)
    return db.all()

