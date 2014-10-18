import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from SqlConnection import *

class MainWindow(QMainWindow):

    """Survival software main window"""

    def __init__(self):
        
        super().__init__()
        
        self.setWindowTitle("Ultimate Survival Software")
        self.resize(800,500)

        self.icon = QIcon(QPixmap("./images/icon.png"))
        self.setWindowIcon(self.icon)

        self.connection = None

        #run the main settings method - toolbar and menu bar etc...
        self.mainSettings()

    
    #MainWindow settings method  - toolbar,statusbar and action bar etc.
    def mainSettings(self):
        #actions
        self.createDatabase = QAction("Create Database",self)
        self.openDatabase = QAction("Open Database",self)
        self.closeDatabase = QAction("Close Database",self)

        self.addItem = QAction("Add Item",self)
        self.editItem = QAction("Edit Item",self)
        self.findItem = QAction("Find Item",self)
        

        #setup the menu bar

        self.menuBar = QMenuBar()

        #menus in menu bar
        self.storeMenu = self.menuBar.addMenu("Prep Store")
        self.connectionMenu  = self.menuBar.addMenu("DB Connection")

        #add actions to menus
        self.storeMenu.addAction(self.addItem)
        self.storeMenu.addAction(self.editItem)
        self.storeMenu.addAction(self.findItem)
        

        self.connectionMenu.addAction(self.createDatabase)
        self.connectionMenu.addAction(self.openDatabase)
        self.connectionMenu.addAction(self.closeDatabase)

        #set the menu bar
        self.setMenuBar(self.menuBar)
    

        #set the toolbar

        self.prepToolBar = QToolBar()

        #add actions to toolbar
        self.prepToolBar.addAction(self.openDatabase)
        self.prepToolBar.addAction(self.closeDatabase)
        self.prepToolBar.addSeparator()
        self.prepToolBar.addAction(self.addItem)
        self.prepToolBar.addAction(self.editItem)
        self.prepToolBar.addAction(self.findItem)
        self.prepToolBar.addSeparator()

        #add the toolbar
        self.addToolBar(self.prepToolBar)

        #setup the status bar
        self.prepStatusBar = QStatusBar()

        self.setStatusBar(self.prepStatusBar)

        self.prepStatusBar.showMessage("Ready")


        #pyqt connections

        self.openDatabase.triggered.connect(self.open_connection)
        self.closeDatabase.triggered.connect(self.close_connection)

    def open_connection(self):
        
        path = QFileDialog.getOpenFileName()
        
        self.connection = SQLConnection(path)
        
        opened = self.connection.open_database()
        
        if opened == True:
            self.prepStatusBar.showMessage("DB Opened Successfully!")
        else:
            self.prepStatusBar.showMessage("DB did not open successfully!")
    def close_connection(self):
        
        if self.connection:
            
            closed = self.connection.close_database()
            if closed == True:
                self.prepStatusBar.showMessage("DB closed successfully!")
            else:
                self.prepStatusBar.showMessage("DB did not close correctly!")
            
        else:
            self.prepStatusBar.showMessage("There is no DB to close!")
            




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.raise_()
    window.show()
    app.exec_()
