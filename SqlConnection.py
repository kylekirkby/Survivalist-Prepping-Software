
from PyQt4.QtSql import *

class SQLConnection:
    
    """Handles the conncetion to the SQL database"""
    
    def __init__(self,path):

        self.path = path

        self.db = None

    def open_database(self):
        
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)

        opened_ok = self.db.open()

        return opened_ok
    
    def close_database(self):
        
        if self.db:
            self.db.close()
            #remove the database from the QSqlDatabase object - "conn" is the default
            #database name
            QSqlDatabase.removeDatabase("conn")
            closed = self.db.open()

            return True
        
        else:

            return False

    def closeEvent(self,event):
        self.close_database()

    def show_all_items(self):
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM PrepItems""")
        query.exec_()
        return query

    def find_products_by_number(self,values):
        
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM PrepItems WHERE PrepItemID =? """)
        query.addBindValue(values[0])
        query.exec_()
        return query
