

import sys, os
from PyQt4 import QtCore
from PyQt4 import QtGui

import Logic, Model
                
class BMOplayer (QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.Player = Logic.PlayerService ()
        self.PlistData = Model.Playlist()

       #---------general window --------------
        self.setGeometry (300, 300, 500, 350)
        self.setFixedSize (500, 350)
        self.setWindowTitle ('BMO player')
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#009999"))
        pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#009999"))
        self.setPalette(pal)
        self.setWindowIcon(QtGui.QIcon('bmo_icon.gif'))
#        self.setToolTip ('useless tooltip')
#        QtGui.QToolTip.setFont (QtGui.QFont ('OldEnglish', 10))
#        self.setWindowIcon ('path')
        #---------player buttons and layout--------------
        self.btnPrevious = QtGui.QPushButton ("<<") #add QIcon as 1st argument
        self.btnPlay = QtGui.QPushButton (">")
        self.btnPause = QtGui.QPushButton ("||")
        self.btnStop = QtGui.QPushButton ("[stop]")
        self.btnNext = QtGui.QPushButton (">>")
        self.hbox_player_buttons = QtGui.QHBoxLayout ()
        self.hbox_player_buttons.addWidget (self.btnPrevious)        
        self.hbox_player_buttons.addWidget (self.btnPlay)        
        self.hbox_player_buttons.addWidget (self.btnPause)        
        self.hbox_player_buttons.addWidget (self.btnStop)        
        self.hbox_player_buttons.addWidget (self.btnNext)
        #-------add delete buttons and layot------------
        self.btnAdd = QtGui.QPushButton ("+")
        self.btnDel = QtGui.QPushButton ("-")
        self.hbox_adddel_buttons = QtGui.QHBoxLayout ()
        self.hbox_adddel_buttons.addStretch (1)
        self.hbox_adddel_buttons.addWidget (self.btnAdd)
        self.hbox_adddel_buttons.addWidget (self.btnDel)
        #--------playlist and general layout-------------
        self.playList = QtGui.QListWidget ()
        
        self.playList.setSelectionMode (QtGui.QAbstractItemView.MultiSelection)
        self.playList.scrollBarWidgets
        #self.playList.setVerticalScrollBar()   #argument QScrollBar
        self.playList.setStyleSheet ("background-color: #408080;")
        #self.playList.setStyleSheet("background-image:url(:bg15.png);")
        self.vbox_general = QtGui.QVBoxLayout ()
        self.vbox_general.addLayout (self.hbox_player_buttons)
        self.vbox_general.addWidget (self.playList)
        self.vbox_general.addLayout (self.hbox_adddel_buttons)
        
        self.setLayout (self.vbox_general)
        
        #-------playlist manipulations---------------
        self.connect (self.btnDel, QtCore.SIGNAL("clicked()"), QtCore.SLOT("clicked_del()"))
        self.connect (self.btnAdd, QtCore.SIGNAL("clicked()"), QtCore.SLOT("clicked_add()"))
        #-------audio buttons manipulations----------
        self.connect (self.btnPlay, QtCore.SIGNAL("clicked()"), QtCore.SLOT("clicked_play()"))
        self.connect (self.btnStop, QtCore.SIGNAL("clicked()"), self.on_stop)

    def closeEvent(self, event):    #overloaded
        self.Player.stop()
        if self.canExit():
            event.accept()
        else:
            event.ignore()

    @QtCore.pyqtSlot()
    def clicked_play (self):
        self.Player.play(self.playList)
        
    def on_stop (self):
        self.Player.stop()

    @QtCore.pyqtSlot()
    def clicked_del (self):
        self.Player.remove (self.playList)
        
    @QtCore.pyqtSlot()
    def clicked_add (self):
        self.Player.add (self.playList, self.PlistData)

if __name__ == '__main__':

    try:       
        app = QtGui.QApplication(sys.argv)
        
        player = BMOplayer ()
        player.show()

    finally:
        app.quit()
        sys.exit(app.exec_())
