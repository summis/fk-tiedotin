# FK-tiedotin

Tool for making a structured weekly bulletin. Information about events are fed to the GUI (information includes header, date, category of event and date) and they are saved to a database. Formatted html-file is created from database entries that can be used in emails and websites. 

Tool is still under construction.

## Installation
Clone the repository.

**Dependecies**
Fk-tiedotin is written in Python and uses following libraries: PyQt5, TinyDB.
These can be installed with

`pip3 install pyqt5 tinydb`

## Usage
Open GUI to add entries to database:

`python fk-tiedotin.py`

Create bullettin form database entries:

`python newsletter.py`

Entries are saved as json in data-folder and ready emails are saved in mails-folder. For every week new database and a new mail are created.
