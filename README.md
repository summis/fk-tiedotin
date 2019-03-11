# FK-tiedotin
Tool for making a structured weekly bulletin. Information about events is fed to the GUI (information includes short description, date, category of event and long description) and entry is saved to a database. Formatted html-file is created from database entries that can be used in emails and websites. 

## Installation
Clone the repository.

### Dependecies
FK-tiedotin is written in Python and uses following libraries: PyQt5, TinyDB, Jinja2.
These can be installed with

`pip3 install pyqt5 tinydb Jinja2`

## Usage
Open GUI to add entries to database:

`python gui.py`

Create bulletin form database entries:

`python bulletin.py`

Entries are saved as json in data-folder and ready emails are saved in mails-folder. For every week new database and a new mail are created.

## Remarks
HTML used in the email must be written in a style that it looks similar in (almost) all email clients. 
