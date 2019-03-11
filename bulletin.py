from functools import partial

from jinja2 import Environment, FileSystemLoader, select_autoescape, Markup
from utils import grouper, category_sort, categories, categories_en, week, all_entries


# Define template behaviour.
env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    )


def nl2br(s):
    """Change linebreaks to <br /> tags.""" 
    return s.replace('\n', Markup('<br/>\n'))   


env.filters['nl2br'] = nl2br    # Add function to env's filters.


# Sort first by category to enable grouping.
entries = all_entries(False)
entries_en = all_entries(True)
entries = sorted(entries, key=partial(category_sort, cats=categories))
entries_en = sorted(entries_en, key=partial(category_sort, cats=categories_en))


# Group entries.
pairs = grouper(entries, categories)
pairs_en = grouper(entries_en, categories_en)


template = env.get_template('cells.html')
variables = {
    "title": "Fyysikkokillan viikkotiedote",
    "header": week+"/2019\n"+"Kilta tiedottaa - Guild News",
    "category_events": pairs,
    "category_events_en": pairs_en,
    }
tiedote = template.render(variables)
with open('mails/kilta-tiedottaa-viikko-'+week+'.html', 'w') as f:
    f.write(tiedote)


print("Bulletin made succesfully.")
