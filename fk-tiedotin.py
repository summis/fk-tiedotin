from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
        QRadioButton, QHBoxLayout, QVBoxLayout, QStyleFactory, QLineEdit, 
        QTextEdit, QLabel, QPushButton, QTabWidget, QWidget, QButtonGroup,
        QDateEdit, QCheckBox)
from database import saveEntry

#TODO
#-own tab for newsletter in english
#-correct lables in both languages

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #languageSelectionTabWidget = QTabWidget(self)
        #tab1 = QWidget()
        #tab2 = QWidget()

        self.createCategorySelectionGroupBox()
        self.createTextEditLayout()
        self.createButtonLayout()

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.categorySelectionLayout, 0, 0)
        mainLayout.addLayout(self.textEditLayout, 1, 0)
        mainLayout.addLayout(self.buttonLayout, 2, 0)
        self.setLayout(mainLayout)

        #tab1.setLayout(mainLayout)
        #languageSelectionTabWidget.addTab(tab1, "Finnish")
        #languageSelectionTabWidget.addTab(tab2, "English")

        #mainMainLayout = QHBoxLayout()
        #mainMainLayout.addWidget(languageSelectionTabWidget)
        ##self.setLayout(mainMainLayout)

        QApplication.setStyle(QStyleFactory.create("cleanlooks"))
        self.setWindowTitle("Fk-tiedotin")



    def createCategorySelectionGroupBox(self):
        self.languageCheckBox = QCheckBox("Put entry to English news letter", self)
        self.languageCheckBox.stateChanged.connect(self.languageCheckBoxClicked)

        categorySelectionGroupBox = QGroupBox("Category")
        self.categorySelectionButtonGroup = QButtonGroup()

        self.radioButton1 = QRadioButton("Killan tapahtumat")
        self.radioButton2 = QRadioButton("Muut yhdistykset")
        self.radioButton3 = QRadioButton("Yleistä")
        self.radioButton4 = QRadioButton("Opinnot")
        self.radioButton1.setChecked(True)

        self.categorySelectionButtonGroup.addButton(self.radioButton1)
        self.categorySelectionButtonGroup.addButton(self.radioButton2)
        self.categorySelectionButtonGroup.addButton(self.radioButton3)
        self.categorySelectionButtonGroup.addButton(self.radioButton4)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.radioButton1)
        buttonLayout.addWidget(self.radioButton2)
        buttonLayout.addWidget(self.radioButton3)
        buttonLayout.addWidget(self.radioButton4)
        categorySelectionGroupBox.setLayout(buttonLayout)

        self.dateEdit = QDateEdit()
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)

        dateLabel = QLabel("Date")
        dateLabel.setBuddy(self.dateEdit)

        self.categorySelectionLayout = QVBoxLayout()
        self.categorySelectionLayout.addWidget(self.languageCheckBox)
        self.categorySelectionLayout.addWidget(categorySelectionGroupBox)
        self.categorySelectionLayout.addWidget(dateLabel)
        self.categorySelectionLayout.addWidget(self.dateEdit)


    def languageCheckBoxClicked(self,state):
        if state == QtCore.Qt.Checked:
            self.radioButton1.setText("Guild's events")
            self.radioButton2.setText("Other organizations")
            self.radioButton3.setText("General")
            self.radioButton4.setText("Studies")
        else:
            self.radioButton1.setText("Killan tapahtumat")
            self.radioButton2.setText("Muut yhdistykset")
            self.radioButton3.setText("Yleistä")
            self.radioButton4.setText("Opinnot")


    def createTextEditLayout(self):
        self.textEditLayout = QVBoxLayout()

        self.headerLineEdit = QLineEdit()
        self.contentTextEdit = QTextEdit()

        headerLabel = QLabel("Header")
        headerLabel.setBuddy(self.headerLineEdit)

        contentLabel = QLabel("Content")
        contentLabel.setBuddy(self.contentTextEdit)

        self.textEditLayout.addWidget(headerLabel)
        self.textEditLayout.addWidget(self.headerLineEdit)
        self.textEditLayout.addWidget(contentLabel)
        self.textEditLayout.addWidget(self.contentTextEdit)



    def createButtonLayout(self):
        self.buttonLayout = QHBoxLayout()

        savePushButton = QPushButton("Save")
        savePushButton.clicked.connect(self.save)

        clearPushButton = QPushButton("Clear")
        clearPushButton.clicked.connect(self.clear)

        self.buttonLayout.addWidget(clearPushButton)
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(savePushButton)


    def save(self):
        category = self.categorySelectionButtonGroup.checkedButton().text()
        date = [self.dateEdit.date().day(), self.dateEdit.date().month(), self.dateEdit.date().year()]
        header = self.headerLineEdit.text()
        content = self.contentTextEdit.toPlainText()

        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.headerLineEdit.clear()
        self.contentTextEdit.clear()

        saveEntry({
            'category': category,
            'date': date,
            'header': header,
            'content': content
            }, self.languageCheckBox.isChecked())
        print ("Saved entry.")


    def clear(self):
        self.headerLineEdit.clear()
        self.contentTextEdit.clear()
        self.dateEdit.setDateTime(QDateTime.currentDateTime())

        print("Cleared entry.")



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    tiedotin = MainWindow()
    tiedotin.show()
    sys.exit(app.exec_()) 
