from datetime import date, timedelta
from functools import partial
from itertools import groupby

from tinydb import TinyDB, Query


# Define categories for entries and current week.

# To make a newsletter for a specific week (eg week 1), last possible occasion 
# to do it is on Monday of that specific week (week 1).  On Tuesday newsletter is made for the 
# following week (week 2).  timedelta correction below takes into account this and a fact 
# that datetime library consideres week 1 to be the year's first week that starts from Monday,
# which differs from finnish convention.  Correction is different every year.
week = (date.today()+timedelta(days=13)).strftime('%W')

categories = ["Killan tapahtumat", "Muut tapahtumat", "Opinnot", "Yleistä"]
categories_en = ["Guild's events", "Other events", "Studies", "General"]



# Database logic.

def save_entry(dict, isEnglish=False):
    """Save entry to database."""
    if isEnglish:
        path = 'data/week'+week+'-en.json'
    else:
        path = 'data/week'+week+'.json'
    db = TinyDB(path)
    db.insert(dict)


def all_entries(isEnglish=False):
    """Return all events from database for this week."""
    if isEnglish:
        path = 'data/week'+week+'-en.json'
    else:
        path = 'data/week'+week+'.json'
    db = TinyDB(path)
    return db.all()



# Functions for grouping and sorting database entries.

def category_sort(x, cats):
    """Return index of database entry's category from a given list."""
    return cats.index(x['category'])


def date_sort(x):
    """Return date of database-entry."""
    return date(x['date'][2], x['date'][1], x['date'][0])


def in_current_week(x):
    """Test whether entry's date is on current week."""
    return int((date(x['date'][2], x['date'][1], x['date'][0]) - timedelta(days=1)).strftime('%U')) + 1 == int(week)


def grouper(entries, cats):
    """Return tuple, which consists of string and another tuple, which consist of two lists.
    First entries are grouped by category and sorted by date. Then they are sorted even 
    further to events that happen this week and events that happen later in the future.
    """
    category_and_events = []
    for k, g in groupby(entries, key=partial(category_sort, cats=cats)):
        events_sorted = sorted(list(g), key=date_sort)
        this_week = [e for e in events_sorted if in_current_week(e)]
        following_week = [e for e in events_sorted if not in_current_week(e)]
        category_and_events.append((cats[k], (this_week, following_week)))
    return category_and_events
