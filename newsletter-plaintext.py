from database import entriesFromCategory, week
from string import Template
from datetime import date, timedelta

first_paragraph = ""
table_of_contents = ""
contents = ""
first_paragraph_en = ""
table_of_contents_en = ""
contents_en = ""


# TODO
# - use Jinja for templating
# - sort entries by date
# - english version
# - some smart way to make first paragraph
# - maybe categories could be defined only in one place instead of two


categories = ["Killan tapahtumat", "Muut yhdistykset", "Opinnot", "Yleistä"]
idx = 1
for category in categories:
    entries = entriesFromCategory(category)
    if entries:
        table_of_contents += f"""{category}\n"""
        for entry in entries:
            table_of_contents += f"  {idx}) {entry['header']}\n"
            contents += f"""{idx}) {entry['header']}\n{entry['content']}\n\n\n"""
            idx += 1

        table_of_contents += "\n"



categories_en = ["Guild's events", "Other organizations", "Studies", "General"]
idx = 1
for category in categories_en:
    entries = entriesFromCategory(category, True)
    if entries:
        table_of_contents_en += f"""{category}\n"""
        for entry in entries:
            table_of_contents_en += f"  {idx}) {entry['header']}\n"
            contents_en += f"""{idx}) {entry['header']}\n{entry['content']}\n\n\n"""
            idx += 1

        table_of_contents_en += "\n"



newsLetter = first_paragraph + table_of_contents + "\n\n" + contents + "\n\n\n\n*************************\n\n\n\n" + first_paragraph_en + table_of_contents_en + "\n" + contents_en

with open(f'kilta-tiedottaa-viikko-{week}.txt', 'w') as f:
    f.write(newsLetter)

print(newsLetter)
