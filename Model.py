
#from PyQt4 import QtCore, QtGui

class Playlist ():
    
    def __init__ (self):
        self.playlist = []
        self.current = 0
        self.play_state = False

    def setData(self, files_names):
        for name in files_names:
            self.playlist.append(name)
            
    def remove_data(self, index_list):
        try:
            for index in index_list.__reversed__():
                self.playlist.pop(index)
        except TypeError:
            self.playlist.pop(index_list)
        except IndexError:
            ...
            # skip current index and continue with next
        except Exception:
            ...

    def get_current (self):
        return self.playlist[self.current]
    
    def set_current (self, index):
        if index not in range(len(self.playlist)): return False
        self.current = index
        return True
