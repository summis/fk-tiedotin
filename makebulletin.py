from jinja2 import Environment, PackageLoader, select_autoescape, Markup
from database import entriesFromCategory, week, allEntries
from itertools import groupby
from tinydb import *
from datetime import date

# TODO: consider replacing lambdas with own functions, category sort and datesort
# TODO: consider only one big database where relevant events are queried only by date
# TODO: consider one utlis.py file which contains all helper functions and categories etc.
# TODO: maybe split template to smaller part

# Tell ninja to look templates from templates-folder, manual escaping is used
env = Environment(
    loader=PackageLoader('fk-tiedotin', 'templates'),
)

# Function that changes linebreaks to <br /> tags. This is added to env's filters.
# Note the use of Markup-string: it is necessary so that <br> tags won't be escaped
def nl2br(s):
    return s.replace('\n', Markup('<br/>\n'))

env.filters['nl2br'] = nl2br

# TODO: define these only in one place
categories = ["Killan tapahtumat", "Muut tapahtumat", "Opinnot", "Yleistä"]
categoriesEn = ["Guild's events", "Other events", "Studies", "General"]


# sort first by category to enable grouping
all_entries = sorted(allEntries(False), key=lambda k: categories.index(k['category']))
all_entries_en = sorted(allEntries(True), key=lambda k: categoriesEn.index(k['category']))
pairs = []
pairs_en = []

for k, g in groupby(all_entries, key=lambda k: categories.index(k['category'])):
    #then sort by date to
    events_sorted = sorted(list(g), key=lambda k: date(k['date'][2], k['date'][1], k['date'][0]))
    # note the +1 that is added to date: python starts indexing week from 0
    this_week = [e for e in events_sorted if int(date(e['date'][2], e['date'][1], e['date'][0]).strftime('%U')) +1 == int(week)]
    following_week = [e for e in events_sorted if int(date(e['date'][2], e['date'][1], e['date'][0]).strftime('%U')) + 1 > int(week)]
    a = (categories[k], (this_week, following_week))
    pairs.append(a)

for k, g in groupby(all_entries_en, key=lambda k: categoriesEn.index(k['category'])):
    #then sort by date to
    events_sorted = sorted(list(g), key=lambda k: date(k['date'][2], k['date'][1], k['date'][0]))
    # note the +1 that is added to date: python starts indexing week from 0
    this_week = [e for e in events_sorted if int(date(e['date'][2], e['date'][1], e['date'][0]).strftime('%U')) +1 == int(week)]
    following_week = [e for e in events_sorted if int(date(e['date'][2], e['date'][1], e['date'][0]).strftime('%U')) + 1 > int(week)]
    a = (categoriesEn[k], (this_week, following_week))
    pairs_en.append(a)

template = env.get_template('bulletin.html')
all_entries_english = sorted(allEntries(True), key=lambda k: categoriesEn.index(k['category']))
variables = {
    "title": "Fyysikkokillan viikkotiedote",
    "header": "Kilta tiedottaa / Guild News \nviikko / week " + week,
    "all_entries": all_entries,
    "category_events": pairs,
    "category_events_en": pairs_en,
    "all_entries_english": all_entries_english,
}

tiedote = template.render(variables)
with open('bulletin.html', 'w') as f:
    f.write(tiedote)

print("Bulletin made succesfully.")
