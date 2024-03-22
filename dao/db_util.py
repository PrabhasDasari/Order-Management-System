import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=PRABHASDASARI;'
                            'Database=OMS;'
                            'Trusted_Connection=yes;')
            return conn
        except:
            print("Connection failed")