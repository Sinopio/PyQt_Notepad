import sys
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor
from PyQt5 import uic 
from PyQt5 import QtCore
from PyQt5 import QtGui

form_class = uic.loadUiType("C:\\Users\\tjddn\\Notepad\\Notepad.ui")[0]

class FindClass(QDialog):
    # checkBox_Upper_Lower
    def __init__(self, parent):
        super(FindClass, self).__init__(parent)
        uic.loadUi("C:\\Users\\tjddn\\Notepad\\Find.ui", self)
        self.show()
        
        self.parent = parent
        self.cursor = self.parent.Text_Plane.textCursor()
        self.TP = self.parent.Text_Plane
        self.upDown = "Down"
        
        self.pushButton_Find.clicked.connect(self.findNext)
        self.pushButton_Cancle.clicked.connect(self.close)
        self.radioButton_Up.clicked.connect(self.updownButton)
        self.radioButton_Down.clicked.connect(self.updownButton)

    def updownButton(self):
        if self.radioButton_Up.isChecked():
            self.upDown = "Up"
            # print("up, {}".format(self.upDown))
        elif  self.radioButton_Down.isChecked():
            self.upDown = "Down"
            # print("down, {}".format(self.upDown))
            
    def findNext(self):
        # print("findNext")        
        pattern = self.lineEdit.text()
        text = self.TP.toPlainText()
        # print(pattern, text)
        regExp = QtCore.QRegExp(pattern)
        self.cursor = self.parent.Text_Plane.textCursor() 

        if self.checkBox_Upper_Lower.isChecked():
            upperLower = QtCore.Qt.CaseSensitive
        else:
            upperLower = QtCore.Qt.CaseInsensitive   
        regExp.setCaseSensitivity(upperLower)
        cursorPos = self.cursor.position()
        
        if self.upDown == "Down":
            index = regExp.indexIn(text, cursorPos)
            # print("{}".format(self.upDown))
        # lastIndexIn이 작동을 안하네?
        else:
            index = regExp.lastIndexIn(text, cursorPos)
            # print("{}".format(self.upDown))
            
        # print(index, cursorPos)
            
        # if match result
        if index != -1:
            self.setCursor(index, len(pattern)+index)
            
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Notepad")
            msgBox.setText(" \"{}\"을(를) 찾을 수 없습니다.". format(self.lineEdit.text()))
            msgBox.addButton("확인", QMessageBox.YesRole)
            msgBox.exec_()

    def keyReleaseEvent(self, event):
        if self.lineEdit.text():
            self.pushButton_Find.setEnabled(True)
        else:
            self.pushButton_Find.setEnabled(False)
            
    def setCursor(self, start, end):
        self.cursor.setPosition(start)
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end-start)
        self.TP.setTextCursor(self.cursor)
        
class ReplaceClass(QDialog):
    def __init__(self, parent):
        super(ReplaceClass, self).__init__(parent)
        uic.loadUi("C:\\Users\\tjddn\\Notepad\\Replace.ui", self)
        self.show()
        
        self.parent = parent
        self.cursor = self.parent.Text_Plane.textCursor()
        self.TP = self.parent.Text_Plane
        
        self.pushButton_Find.clicked.connect(self.findFunction)
        self.pushButton_Replace.clicked.connect(self.replaceFunction)
        self.pushButton_Cancle.clicked.connect(self.close)
        
    def findFunction(self):
        pattern = self.lineEdit_Find.text()
        text = self.TP.toPlainText()
        regExp = QtCore.QRegExp(pattern)
        self.cursor = self.parent.Text_Plane.textCursor()
        
        if self.checkBox_Upper_Lower.isChecked():
            upperLower = QtCore.Qt.CaseSensitive
        else:
            upperLower = QtCore.Qt.CaseInsensitive   
        regExp.setCaseSensitivity(upperLower)
        cursorPos = self.cursor.position()
        index = regExp.indexIn(text, cursorPos)
        
        if index != -1:
            self.setCursor(index, len(pattern)+index)
            
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Notepad")
            msgBox.setText(" \"{}\"을(를) 찾을 수 없습니다.". format(self.lineEdit_Find.text()))
            msgBox.addButton("확인", QMessageBox.YesRole)
            msgBox.exec_()
            
    def replaceFunction(self):
        replacewords = self.lineEdit_Replace.text()
        self.parent.Text_Plane.textCursor().removeSelectedText()
        self.parent.Text_Plane.textCursor().insertText(replacewords)
    
    def keyReleaseEvent(self, event):
        if self.lineEdit_Find.text():
            self.pushButton_Find.setEnabled(True)
        else:
            self.pushButton_Find.setEnabled(False)    
        
    def setCursor(self, start, end):
        self.cursor.setPosition(start)
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end-start)
        self.TP.setTextCursor(self.cursor)    
        
        
class TextFormClass(QDialog):
    def __init__(self, parent):
        super(TextFormClass, self).__init__(parent)
        uic.loadUi("C:\\Users\\tjddn\\Notepad\\TextForm.ui", self)
        self.show()
        
        self.parent = parent
        # self.cursor = self.parent.Text_Plane.textCursor()
        # self.TP = self.parent.Text_Plane
        
        # self.style = self.comboBox_Style.text()
        # self.size = self.comboBox_Size.text()
        
        self.fontComboBox.currentFontChanged.connect(self.textFontFunction)
        self.comboBox_Style.currentIndexChanged.connect(self.textStyleFunction)
        self.comboBox_Size.currentIndexChanged.connect(self.textSize)
        
    def textFontFunction(self):
        self.textEdit_box.setFont(self.fontComboBox.currentFont())
        self.parent.Text_Plane.setFont(self.fontComboBox.currentFont())
            
        
    def textSize(self):
        self.size = int(self.comboBox_Size.itemText(self.comboBox_Size.currentIndex()))
        # print(self.size)
        # print(self.comboBox_Size.itemText(self.comboBox_Size.currentIndex()))
        # self.parent.Text_Plane.setFont((self.fontComboBox.currentFont(), size))
        self.parent.Text_Plane.setFontPointSize(self.size)
        self.textEdit_box.setFontPointSize(self.size)
        
    def textStyleFunction(self):
        if self.comboBox_Style.currentIndex() == 0:
            self.parent.Text_Plane.setFontWeight(QtGui.QFont.Normal)
            self.parent.Text_Plane.setFontItalic(False)
            self.textEdit_box.setFontWeight(QtGui.QFont.Normal)
            self.textEdit_box.setFontItalic(False)
            
        elif self.comboBox_Style.currentIndex() == 1:
            self.parent.Text_Plane.setFontWeight(QtGui.QFont.Bold)
            self.parent.Text_Plane.setFontItalic(False)
            self.textEdit_box.setFontWeight(QtGui.QFont.Bold)
            self.textEdit_box.setFontItalic(False)
            
        elif self.comboBox_Style.currentIndex() == 2:
            self.parent.Text_Plane.setFontWeight(QtGui.QFont.Normal)
            self.parent.Text_Plane.setFontItalic(True)
            self.textEdit_box.setFontWeight(QtGui.QFont.Normal)
            self.textEdit_box.setFontItalic(True)
            
        elif self.comboBox_Style.currentIndex() == 3:
            self.parent.Text_Plane.setFontWeight(QtGui.QFont.Bold)
            self.parent.Text_Plane.setFontItalic(True)
            self.textEdit_box.setFontWeight(QtGui.QFont.Bold)
            self.textEdit_box.setFontItalic(True)
            
        # print("textStyleFunction")
        
        
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.opened = False
        self.opened_file_name = '제목 없음'
        self.cursor = self.Text_Plane.textCursor()
        
        # menu_File
        self.action_New_FIle.triggered.connect(self.newFileFunction)
        self.action_Open.triggered.connect(self.openFunction)
        self.action_Save.triggered.connect(self.saveFunction)
        self.action_Save_As_New.triggered.connect(self.saveAsNewFunction)
        self.action_Close.triggered.connect(self.close)
        
        # menu_Edit
        self.action_Undo.triggered.connect(self.undoFunction)
        self.action_Cut.triggered.connect(self.cutFunction)
        self.action_Copy.triggered.connect(self.copyFunction)
        self.action_Paste.triggered.connect(self.pasteFunction)
        self.action_Del.triggered.connect(self.delFunction)
        self.action_Find.triggered.connect(self.findFunction)
        self.action_Replace.triggered.connect(self.replaceFunction)
        self.action_Select_All.triggered.connect(self.selectAllFunction)
        self.action_Day_Time.triggered.connect(self.dayTimeFunction)
        
        # menu_Form
        self.action_Auto_Line.triggered.connect(self.autoLineFunction)
        self.action_Word_Format.triggered.connect(self.wordFormatFunction)
        
        # menu_View
        self.action_Zoom_In.triggered.connect(self.zoomInFunction)
        self.action_Zoom_Out.triggered.connect(self.zoomOutFunction)
        self.action_State.triggered.connect(self.stateFunction)
        
        # menu_Help
        # self.action_See_Help.triggered.connect(self.seeHelpFunction)
        self.action_See_Help.triggered.connect(lambda: webbrowser.open('https://support.microsoft.com/ko-kr/windows/%EB%A9%94%EB%AA%A8%EC%9E%A5%EC%9D%98-%EB%8F%84%EC%9B%80%EB%A7%90-4d68c388-2ff2-0e7f-b706-35fb2ab88a8c'))
        self.action_Send_Feedback.triggered.connect(self.sendFeedbackFunction)
        self.action_Info.triggered.connect(self.infoFunction)
        
        self.Text_Plane.setLineWrapMode(QTextEdit.NoWrap)
        
    def checkChangedBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Notepad")
        msgBox.setText("변경 내용을 {}에 저장하시겠습니까?". format(self.opened_file_name))
        msgBox.addButton('저장', QMessageBox.YesRole) # return 0 value
        msgBox.addButton('저장 안함', QMessageBox.NoRole) # return 1 value
        msgBox.addButton('취소', QMessageBox.RejectRole) # return 2 value
        res = msgBox.exec_()
        
        if res == 0:
            self.saveFunction()         
        else:
            return res
        
    def isChanged(self):
        if not self.opened:
            if self.Text_Plane.toPlainText().strip():
                return True
            return False
        
        current_data = self.Text_Plane.toPlainText()
        with open(self.opened_file_name, encoding='UTF8') as f:
            file_data = f.read()
        
        if current_data == file_data:
            return False
        else:
            return True
        
    def closeEvent(self, event):
        if self.isChanged():
            res = self.checkChangedBox()

            if res == 2:
                event.ignore()
    
    def saveFile(self, fname):
        data = self.Text_Plane.toPlainText()
        
        with open(fname, 'w', encoding='UTF8') as f:
            f.write(data)
        data = self.Text_Plane.toPlainText()
        
        self.opened = True
        self.opened_file_name = fname
        # print("save {}".format(fname))
        
    def openFile(self, fname):
        with open(fname, encoding='UTF8') as f:
            data = f.read()
        self.Text_Plane.setPlainText(data)       
        
        self.opened = True
        self.opened_file_name = fname
        # print("open {}".format(fname))
        
    # menu_File_Function
    def newFileFunction(self):
        if self.isChanged():
            res = self.checkChangedBox()
                
        self.Text_Plane.clear()
        # print("new file")
        
    def openFunction(self):
        if self.isChanged():
            res = self.checkChangedBox()
              
        fname =  QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")
        
        if fname[0]:
           self.openFile(fname[0])
        
    def saveFunction(self):
        # already oppened >>
        if self.opened:
            self.saveFile(self.opened_file_name)
            
        else:
            self.saveAsNewFunction()
        
    def saveAsNewFunction(self):
        fname =  QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")
       
        if fname[0]:
            self.saveFile(fname[0])
        
    # menu_Edit_Function
    def undoFunction(self):
        self.Text_Plane.undo()
        # print("undoFunction")
    
    def cutFunction(self):
        self.Text_Plane.cut()
        # print("cutFunction")
        
    def copyFunction(self):
        self.Text_Plane.copy()
        # print("copyFunction")  
        
    def pasteFunction(self):
        self.Text_Plane.paste()
        # print("pasteFunction")
        
    def delFunction(self):
        self.Text_Plane.textCursor().removeSelectedText()
        # print("delFunction")
        
    def findFunction(self):
        FindClass(self)
        # print("findFunction")
        
    def replaceFunction(self):
        ReplaceClass(self)
        print("replaceFunction")
    
    def selectAllFunction(self):
        self.Text_Plane.selectAll()
        # print("selectAllFunction")
    
    def dayTimeFunction(self):
        
        print("dayTimeFunction")
        
    # menu_Form_Function
    def autoLineFunction(self):
        if self.action_Auto_Line.isChecked():
            self.Text_Plane.setLineWrapMode(QTextEdit.WidgetWidth)
            
        else:
            self.Text_Plane.setLineWrapMode(QTextEdit.NoWrap)
        # print("autoLineFunction, {}".format(self.action_Auto_Line.isChecked()))
    
    def wordFormatFunction(self):
        TextFormClass(self)
        # print("wordFormatFunction")
    
    # menu_View_Function
    def zoomInFunction(self):
        self.Text_Plane.zoomIn(1)
        # print("zoomInFunction")
        
    def zoomOutFunction(self):
        self.Text_Plane.zoomOut(1)
        # print("zoomOutFunction")
    
    def stateFunction(self):
        print("stateFunction")
        
    # menu_Help_Function
    # def seeHelpFunction(self):
    #     print("seeHelpFunction")
    
    def sendFeedbackFunction(self):
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Notepad")
        msgBox.setText("문제가 발생하면 아래 메일로 알려주세요\n tjddns1016@naver.com")
        msgBox.addButton("확인", QMessageBox.YesRole)
        msgBox.exec_()          
            
        # print("sendFeedbackFunction")
    
    def infoFunction(self):
        print("infoFunction")    
        
app = QApplication(sys.argv)
# show Window
mainWindow = WindowClass()
mainWindow.show()
# run app
app.exec_()