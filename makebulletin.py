from jinja2 import Environment, PackageLoader, select_autoescape, Markup
from database import entriesFromCategory, week, allEntries

# Tell ninja to look templates from templates-folder, manual escaping is used
env = Environment(
    loader=PackageLoader('fk-tiedotin', 'templates'),
)

# Function that changes linebreaks to <br /> tags. This is added to env's filters.
# Note the use of Markup-string: it is necessary so that <br> tags won't be escaped
def nl2br(s):
    return s.replace('\n', Markup('<br/>\n'))

env.filters['nl2br'] = nl2br


template = env.get_template('bulletin.html')
all_entries = allEntries(False)
all_entries_english = allEntries(True)
variables = {
    "title": "Fyysikkokillan viikkotiedote",
    "header": "Kilta tiedottaa / Guild News \nviikko / week " + week,
    "all_entries": all_entries,
    "all_entries_english": all_entries_english
}


tiedote = template.render(variables)
with open('bulletin.html', 'w') as f:
    f.write(tiedote)


print(tiedote)
