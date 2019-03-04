from database import entriesFromCategory, week
from string import Template
from datetime import date, timedelta
from config import *


with open("kilta-tiedottaa-template.html", 'r') as f:
    txt = f.read()
template = Template(txt)


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


#categories = ["Killan tapahtumat", "Muut yhdistykset", "Opinnot", "Yleistä"]
# index for unique id:s to create links
idx = 1
for category in categories:
    entries = entriesFromCategory(category)
    if entries:
        table_of_contents += f"""<tr> 
            <td style="color: #201E1E; font-family: Georgia; font-size: 24px;">
            <i>{category}</i> 
            </td>
            </tr>\n"""

        table_of_contents += """<tr>
            <td style="padding: 10px 0px 15px 0px; font-family: Calibri; font-size: 16px;">
            <ul style=" margin: 0;">\n"""

        for entry in entries:
            # escape some characters and change linebreaks to html
            formattedHeader = entry['header'].replace("&","&amp;")\
                    .replace("<","&lt;").replace(">", "&gt;")\
                    .replace("\"","&quot;").replace("\'","&apos;") 
            formattedContent = entry['content'].replace("&","&amp;")\
                    .replace("<","&lt;").replace(">", "&gt;")\
                    .replace("\"","&quot;").replace("\'","&apos;").replace("\n", "<br/>")

            table_of_contents += f"<li><a href='#id{idx}'>{formattedHeader}</a></li>\n"

            contents += f"""<tr>
                <td id='id{idx}' style="padding: 10px 0px 15px 0px; font-family: Calibri; font-size: 16px;">
                <b>{formattedHeader}</b><br/>
                {formattedContent}
                </td>
                </tr>\n"""
            idx += 1

        table_of_contents += "</ul>\n</td>\n</tr>\n"

#categories_en = ["Guild's events", "Other organizations", "Studies", "General"]
for category in categoriesEn:
    entries = entriesFromCategory(category, True)
    if entries:
        table_of_contents_en += f"""<tr> 
            <td style="color: #201E1E; font-family: Georgia; font-size: 24px;">
            <i>{category}</i> 
            </td>
            </tr>\n"""

        table_of_contents_en += """<tr>
            <td style="padding: 10px 0px 15px 0px; font-family: Calibri; font-size: 16px;">
            <ul style=" margin: 0;">\n"""

        for entry in entries:
            formattedHeader = entry['header'].replace("&","&amp;")\
                    .replace("<","&lt;").replace(">", "&gt;")\
                    .replace("\"","&quot;").replace("\'","&apos;") 
            formattedContent = entry['content'].replace("&","&amp;")\
                .replace("<","&lt;").replace(">", "&gt;")\
                .replace("\"","&quot;").replace("\'","&apos;").replace("\n", "<br/>")

            table_of_contents_en += f"<li><a href='#id{idx}'>{formattedHeader}</a></li>\n"

            contents_en += f"""<tr>
                <td id='id{idx}' style="padding: 10px 0px 15px 0px; font-family: Calibri; font-size: 16px;">
                <b>{formattedHeader}</b><br/>
                {formattedContent}
                </td>
                </tr>\n"""
            idx += 1

        table_of_contents_en += "</ul>\n</td>\n</tr>\n"


d = {
        'WEEK': week,
        'FIRST_PARAGRAPH': first_paragraph,
        'TABLE_OF_CONTENTS': table_of_contents,
        'CONTENTS': contents,
        'FIRST_PARAGRAPH_EN': first_paragraph_en,
        'TABLE_OF_CONTENTS_EN': table_of_contents_en,
        'CONTENTS_EN': contents_en
        }
newsLetter = template.substitute(d)


with open(f'mails/kilta-tiedottaa-viikko-{week}.html', 'w') as f:
    f.write(newsLetter)

print(newsLetter)
