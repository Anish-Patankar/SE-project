from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn=sqlite3.connect('employee.db')
curr=conn.cursor()


class Ui_MainWindow9(object):
    def setup9(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 391, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 161, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(220, 40, 141, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 40, 160, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 40, 70, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 70, 70, 17))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(220, 40, 131, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 129, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(220, 20, 47, 13))
        self.label_8.setObjectName("label_8")
        
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.tabWidget.setCurrentIndex(0)
        MainWindow.setWindowTitle("Employee")
        self.label.setText("ID")
        self.label_2.setText("Name")
        self.label_3.setText("Address")
        self.label_4.setText("Post")
        self.label_5.setText("Salary")
        self.pushButton.setText("Enter details")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),"Enter")
        self.label_6.setText("Name")
        self.label_7.setText("Id")
        self.label_8.setText("Results")
        self.pushButton_2.setText("Search")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Search")
        self.textEdit = QtWidgets.QTextEdit()
        self.scrollArea.setWidget(self.textEdit)
        
        self.pushButton.clicked.connect(self.clickEnter)
        self.pushButton_2.clicked.connect(self.clickSearch)
    def clickEnter(self):
        a=self.lineEdit.text()
        b=self.lineEdit_2.text()
        c=self.lineEdit_3.text()
        d=self.lineEdit_4.text()
        e=int(self.lineEdit_5.text())
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        curr.execute('Insert into employee values(?,?,?,?,?)',(a,b,c,d,e))
        conn.commit()
        z="Insert successful \nId:"+a+"\nName:"+b+"\nAddress:"+c+"\nPost:"+d+"\nSalary: Rs."+str(e)
        self.textEdit.setText(z)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()



    def clickSearch(self):
        if (self.checkBox.isChecked() and self.checkBox_2.isChecked()):
            a=self.lineEdit_6.text()
            b=self.lineEdit_7.text()
            z=""
            curr.execute('select * from employee where name = ? and ID = ?',(a,b))
            rows=curr.fetchall()
            conn.commit()
            if len(rows)>0:
                row=rows[0]
                z="Employee Information \n\nId:"+row[0]+"\nName:"+row[1]+"\nAddress:"+row[2]+"\nPost:"+row[3]+"\nSalary: Rs."+str(row[4])
            else:
                z="No such employee works here"
            self.textEdit.setText(z)
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
        elif(self.checkBox.isChecked()):
            a=self.lineEdit_6.text()
            curr.execute('select * from employee where name = ?',(a,))
            rows=curr.fetchall()
            conn.commit()
            print(rows)
            if len(rows)>0:
                  z="Employee Information \n\n"
                  for row in rows:
                      z+="Id:"+row[0]+"\nName:"+row[1]+"\nAddress:"+row[2]+"\nPost:"+row[3]+"\nSalary: Rs."+str(row[4])+"\n\n"
                  
            else:
                  z="No such employee works here"
            self.textEdit.setText(z)
            self.lineEdit_6.clear()
        elif(self.checkBox_2.isChecked()):
            b=self.lineEdit_7.text()
            z=""
            curr.execute('select * from employee where ID = ?',(b,))
            rows=curr.fetchall()
            conn.commit()
            if len(rows)>0:
                row=rows[0]
                z="Employee Information \n\nId:"+row[0]+"\nName:"+row[1]+"\nAddress:"+row[2]+"\nPost:"+row[3]+"\nSalary: Rs."+str(row[4])
            else:
                z="No such employee works here"
            self.textEdit.setText(z)
            
            self.lineEdit_7.clear()
        else:
            z="Please tick a checkbox!!"
            self.textEdit.setText(z)
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow9()
    ui.setup9(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
