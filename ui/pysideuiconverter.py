# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pysideuiconverter.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, 
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QFileDialog,QLabel, QMessageBox

from PySide2.QtCore import Slot
import os
import subprocess
from datetime import datetime
import webbrowser

from pathlib import Path
firstrun = True
currentDirectory = str(Path(__file__).parent.absolute()).replace("\\","/")
SettingsLocation = currentDirectory + "/settings"
pysideloc = currentDirectory + "/Scripts/pyside2-uic.exe"

exportAppend = "_converted"
LauncherTemplate = currentDirectory + "/settings/templates/LauncherTemplate.py"
LauncherBAT_Template = currentDirectory + "/settings/templates/Launcher_BAT_Template.bat"
TemplatePrefix = currentDirectory + "/settings/templatefile_"
TemplateLaunchPrefix =  "/LauncherTemplate_"
TemplateExtension = ".ini"

buttonstyle = u"\
                QPushButton {   \
                    color:rgb(0, 170, 255);    \
                    border: 1px solid white;   \
                }   \
                QPushButton:checked{\
                    color:rgb(0, 170, 255);    \
                    background-color: rgb(0, 89, 179);\
                    border: 1px solid white; \
                }\
                QPushButton:hover{  \
                    background-color: rgb(0, 26, 51); \
                    color:rgb(0, 170, 255);    \
                    border: 1px solid white;  \
                }  \
                "

# Greetings
# def getfile(file_ext='', text='', button_caption='', button_type=0, title=''):
#     filter = {
#         '': '',
#         'txt': 'File (*.txt)',
#         'dbf': 'Table/DBF (*.dbf)',
#     }.get(file_ext, '*.' + file_ext)
#     t = QFileDialog()
#     t.setFilter('All Files (*.*);;' + filter)
#     t.selectFilter(filter or 'All Files (*.*);;')
#     if text:
#         (next(x for x in t.findChildren(QLabel) if x.text() == 'File &name:')).setText(text)
#     if button_caption:
#         t.setLabelText(QFileDialog.Accept, button_caption)
#     if title:
#         t.setWindowTitle(title)
#     t.exec_()
#     return t.selectedFiles()[0]

def getFiles(directory, searchTerm):
    from os import walk

    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        for file in filenames:
            if file.endswith(searchTerm):
                f.append(str(os.path.join(dirpath, file)))

                # print(os.path.join(dirpath, file))
            # print(file)

            # if searchTerm in filenames:
    # f.extend(filenames)
    return f
    

class Ui_MainWindow(object):
    @Slot()
    def set_uisource(self):
        t = QFileDialog()
        t.setNameFilter("*.ui")
        if t.exec_():
            fileNames = t.selectedFiles()
        print(fileNames[0])
        # print("On")
        filename = fileNames[0]
        if ".ui" not in fileNames[0]:
            filename = fileNames[0] + ".ui"
        self.lineEdit.setText(filename)
        print("Yup")
        return 
            # print(firstrun)
    @Slot()
    def set_pythonsource(self):
        t = QFileDialog()
        t.setNameFilter("*.py")
        if t.exec_():
            fileNames = t.selectedFiles()
        filename = fileNames[0]
        if ".py" not in fileNames[0]:
            filename = fileNames[0] + ".py"
        self.lineEdit_3.setText(filename)
        
        print(fileNames[0])
        print("On")
        return 
        # print(firstrun)
    @Slot()
    def set_pysidelocation(self):
        t = QFileDialog()
        t.setNameFilter("*pyside2-uic.exe")
        if t.exec_():
            fileNames = t.selectedFiles()
        filename = fileNames[0]
        
        self.lineEdit_2.setText(filename)
        
        print(fileNames[0])
        print("On")
        return 
        # print(firstrun)
    @Slot()
    def set_savetemplate(self):
        firstline = str(self.lineEdit_3.text()).replace("\n", "")
        secondline = str(self.lineEdit.text()).replace("\n", "")
        print(firstline)
        today = datetime.now()
        d1 = str(today.strftime("%Y%m%d_%H%M%S"))
        # secondline = self.lineEdit_3
        root_ext = os.path.splitext(firstline) 

        firstfilename = str(os.path.basename(firstline.replace('\\','/'))).replace(root_ext[1],"")
        fulltext = [d1,"\n" + firstfilename.replace('\\','/') , "\n" + secondline.replace('\\','/') , "\n" + firstline]
        tempatefilename = TemplatePrefix + d1 +"_"+ firstfilename+ TemplateExtension
        if not os.path.exists(tempatefilename):
            with open(tempatefilename, 'w') as file:
                file.writelines(fulltext)
                # for line in tempatefilename:
                #     file.write(line)
                file.close()
                
        else:

            with open(tempatefilename, "w") as file:
                file.writelines(fulltext)

                # for line in tempatefilename:
                #     file.write(line)
                file.close()
        print(fulltext)
        print("On")
        return 
        # print(firstrun)
    @Slot()
    def loadrecenttempaltes(self, MainWindow):

        print(currentDirectory)
        if os.path.exists(currentDirectory):
            print("EXISTS")
        print(SettingsLocation)
        print(os.path.exists(SettingsLocation))
        recentfiles = getFiles(SettingsLocation, TemplateExtension)
        print(len(recentfiles))
        for recent in recentfiles:
            print(recent)
            root_ext = os.path.splitext(recent) 

            firstfilename = str(os.path.basename(recent.replace('\\','/'))).replace(root_ext[1],"")
            splitt = firstfilename.split('_')[3]
            self.recentscomboBox.addItem(splitt)
        if len(recentfiles) > 0 :
            self.loadrecenttemplate(MainWindow)
        return 
        # print(firstrun)


    @Slot()
    def startconvert(self, MainWindow):
        # pysidepath = os.path.abspath(self.lineEdit_2.text())
        argumentt = "\"" +  pysideloc +  "\" \"" +  self.lineEdit.text() +  "\" -o \"" +  self.lineEdit_3.text() + "\""
        print(argumentt)
        # subprocess.run("pbcopy", universal_newlines=True, input=argumentt)

        argumenttorun = 'cmd /c ' +argumentt  
        cmd='echo '+argumenttorun.strip()+'|clip'

        subprocess.check_call(cmd, shell=True)
        subprocess.call([pysideloc, self.lineEdit.text(), '-o', self.lineEdit_3.text()])
        firstname = str(self.lineEdit.text())
        secondnam = str(self.lineEdit_3.text())
        containingdir = str(os.path.basename(os.path.dirname(secondnam)))
        # os.system(os.path.dirname(self.lineEdit_3.text()))
        path = os.path.dirname(firstname)
        print(path)
        root_ext = os.path.splitext(firstname) 
        firstfilename = str(os.path.basename(firstname)).replace(root_ext[1],"")
        
        contents = []
        with open(LauncherTemplate) as f:
            contents = f.readlines()
            f.close()
        launcherfile = str(Path(path).parent) + TemplateLaunchPrefix + firstfilename + ".py"
        print(launcherfile + "|     HH")
        with open(launcherfile, 'w') as file:
                # file.writelines(fulltext)
                for line in contents:
                    file.write(line.replace("$UIFile", firstfilename).replace("$UFolder", containingdir))
                file.close()


        with open(LauncherBAT_Template) as f:
            contents = f.readlines()
            f.close()
        launcherfile = str(Path(path).parent) + TemplateLaunchPrefix + firstfilename + ".bat"
        print(launcherfile + "|     HH")
        with open(launcherfile, 'w') as file:
                # file.writelines(fulltext)
                for line in contents:
                    file.write(line.replace("$LAUNCHPY", TemplateLaunchPrefix.replace('/', "") + firstfilename + ".py"))
                file.close()

        msgBox = QMessageBox();
        msgBox.setText("Your files have been converted and created. You can LAUNCH your gui by opening the .bat file");
        msgBox.exec();
        webbrowser.open('file:///' +  str(Path(path).parent))
        # os.system(f'start {os.path.realpath(path)}')

        # os.system(argumentt)
        # subprocess.call(argumentt)
        return 
        # print(firstrun)




    @Slot()
    def loadrecenttemplate(self, MainWindow):

        recentfiles = getFiles(SettingsLocation, TemplateExtension)
        print(len(recentfiles))
        indexx = self.recentscomboBox.currentIndex()

      
        content = []
        with open(recentfiles[indexx]) as f:
            content = f.readlines()
        print("YOOO")
        # print("LAST IS |" + uiname[uilonglength] )
        self.lineEdit.setText(content[2].replace('\n', ""))
        self.lineEdit_3.setText(content[3])

        print(content[2])
        print(content[3])
        print("YOOO")
        return 
        # print(firstrun)

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 250)
        MainWindow.setStyleSheet(u"background-color: rgb(37, 50, 63);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.actionSave_Template = QAction(MainWindow)
        self.actionSave_Template.setObjectName(u"actionSave_Template")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 160, 571, 31))


        
#         self.pushButton.setStyleSheet(u"border: 1px solid white;\n""QPushButton:checked { background-color: red;} \n"
# "color: rgb(0, 170, 255);")

        self.pushButton.setStyleSheet(buttonstyle)


        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 431, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 141, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 420, 141, 21))

        self.lineEdit_2.setGeometry(QRect(40, 450, 431, 20))

        self.FindFileButton = QPushButton(self.centralwidget)
        self.FindFileButton.setObjectName(u"FindFileButton")
        self.FindFileButton.setGeometry(QRect(460, 50, 21, 21))
        self.FindFileButton.setStyleSheet(buttonstyle)
        self.FindpysideButton = QPushButton(self.centralwidget)
        self.FindpysideButton.setObjectName(u"FindpysideButton")
        self.FindpysideButton.setGeometry(QRect(480, 450, 21, 21))

        # self.FindpysideButton.setGeometry(QRect(460, 190, 21, 21))
        self.FindpysideButton.setStyleSheet(buttonstyle)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 120, 431, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 90, 141, 21))
        self.FindFileButton_2 = QPushButton(self.centralwidget)
        self.FindFileButton_2.setObjectName(u"FindFileButton_2")
       

        self.FindFileButton_2.setGeometry(QRect(460, 120, 21, 21))
        self.FindFileButton_2.setStyleSheet(buttonstyle)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(490, 120, 101, 17))
        self.recentscomboBox = QComboBox(self.centralwidget)
        self.recentscomboBox.setObjectName(u"recentscomboBox")
        self.recentscomboBox.setGeometry(QRect(498, 0, 121, 22))
        self.loadRecentButton = QPushButton(self.centralwidget)
        self.loadRecentButton.setObjectName(u"loadRecentButton")
        self.loadRecentButton.setGeometry(QRect(400, 0, 91, 21))
        self.loadRecentButton.setStyleSheet(buttonstyle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 627, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")


        # Set Buttons
        self.FindFileButton_2.clicked.connect(self.set_pythonsource)
        self.FindFileButton.clicked.connect(self.set_uisource)
        self.FindpysideButton.clicked.connect(self.set_pysidelocation)
        self.pushButton.clicked.connect(self.startconvert)
        self.loadRecentButton.clicked.connect(self.loadrecenttemplate)
        self.actionSave_Template.triggered.connect(self.set_savetemplate)
        # connect(self.actionSave_Template  , SIGNAL("triggered()"), self, SLOT("open()"))
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave_Template)
        self.retranslateUi(MainWindow)
        self.loadrecenttempaltes( MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_Template.setText(QCoreApplication.translate("MainWindow", u"Save Template", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File to Convert:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"/Scripts/pyside2-uic.exe", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"pyside2-uic.exe Location:", None))
        self.FindFileButton.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.FindpysideButton.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Export Path:", None))
        self.FindFileButton_2.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Same as Source", None))
        self.loadRecentButton.setText(QCoreApplication.translate("MainWindow", u"Load Recent", None))

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
    

