[iha ok mut ootko kattonu...](https://github.com/NikoDaGreat/fk-tiedotin)




# FK-tiedotin
Tool for making a structured weekly bulletin. Information about events are fed to the GUI (information includes header, date, category of event and date) and they are saved to a database. Formatted html-file is created from database entries that can be used in emails and websites. 

Tool is still under construction.

## Installation
Clone the repository.

### Dependecies
Fk-tiedotin is written in Python and uses following libraries: PyQt5, TinyDB, Jinja2.
These can be installed with

`pip3 install pyqt5 tinydb Jinja2`

## Usage
Open GUI to add entries to database:

`python fk-tiedotin.py`

Create bulletin form database entries:

`python makebulletin.py`

Entries are saved as json in data-folder and ready emails are saved in mails-folder. For every week new database and a new mail are created.

## Remarks
HTML used in the email must be written in a style that it looks similar in (almost) all email clients. 
