from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
        QRadioButton, QHBoxLayout, QVBoxLayout, QStyleFactory, QLineEdit, 
        QTextEdit, QLabel, QPushButton, QTabWidget, QWidget, QButtonGroup,
        QDateEdit)
from database import saveEntry

#TODO
#-own tab for newsletter in english
#-correct lables in both languages

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        languageSelectionTabWidget = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()

        self.createCategorySelectionGroupBox()
        self.createTextEditLayout()
        self.createButtonLayout()

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.categorySelectionLayout, 0, 0)
        mainLayout.addLayout(self.textEditLayout, 1, 0)
        mainLayout.addLayout(self.buttonLayout, 2, 0)
        #self.setLayout(mainLayout)

        tab1.setLayout(mainLayout)
        languageSelectionTabWidget.addTab(tab1, "Finnish")
        languageSelectionTabWidget.addTab(tab2, "English")

        mainMainLayout = QHBoxLayout()
        mainMainLayout.addWidget(languageSelectionTabWidget)
        self.setLayout(mainMainLayout)

        QApplication.setStyle(QStyleFactory.create("cleanlooks"))
        self.setWindowTitle("Fk-tiedotin")



    def createCategorySelectionGroupBox(self):
        categorySelectionGroupBox = QGroupBox("Category")
        self.categorySelectionButtonGroup = QButtonGroup()

        radioButton1 = QRadioButton("Killan tapahtumat")
        radioButton2 = QRadioButton("AYY ja Aalto")
        radioButton3 = QRadioButton("Yleistä")
        radioButton1.setChecked(True)

        self.categorySelectionButtonGroup.addButton(radioButton1)
        self.categorySelectionButtonGroup.addButton(radioButton3)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(radioButton1)
        buttonLayout.addWidget(radioButton2)
        buttonLayout.addWidget(radioButton3)
        categorySelectionGroupBox.setLayout(buttonLayout)
        
        self.dateEdit = QDateEdit()
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)

        dateLabel = QLabel("Date")
        dateLabel.setBuddy(self.dateEdit)

        self.categorySelectionLayout = QVBoxLayout()
        self.categorySelectionLayout.addWidget(categorySelectionGroupBox)
        self.categorySelectionLayout.addWidget(dateLabel)
        self.categorySelectionLayout.addWidget(self.dateEdit)



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
            })
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
