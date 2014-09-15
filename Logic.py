
from PyQt4 import QtCore, QtGui
import pygame
import os
import Model

class PlayerService ():
    
    def __init__(self):
        pygame.init()
        pygame.mixer.get_init()
        pygame.mixer.music.set_volume(1.0)

    def __del__(self):
        pygame.mixer.music.stop()
    
    def play(self, QplayList):
        index = self.getFirstSelected(QplayList)    #get which track will be played
        filename = QplayList.item(index).text()
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1) #loops = -1 (no loop), pos = 0.0
        
    def stop(self):
        pygame.mixer.music.stop()

    def add (self, QplayList, PlistData):
        soundpath = os.getcwd() + r"/sound"
        filenames = QtGui.QFileDialog.getOpenFileNames(QplayList, 'Open file(s)',
                                                       soundpath)
        QplayList.addItems(filenames)

    def remove (self, QplayList):
        items = QplayList.count()
        rangeList = range(items).__reversed__()
        for index in rangeList:
            if QplayList.isItemSelected (QplayList.item(index)) is True:
                QplayList.takeItem(index)

    def getFirstSelected(self, QplayList):
        for index in range(QplayList.count()):
            if QplayList.isItemSelected (QplayList.item(index)) is True:
                return index
        return 0
