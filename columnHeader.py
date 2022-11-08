import time
import random

class DatabaseManagement:
    def __init__(self) -> None:
        self.columnHeader = ['NIM', 'NAMA', 'PRODI']

    def makeTable(self):
        # Namespace
        print('\n', end='\n+')

        for columnHeader in self.columnHeader:
            # Top-Outline
            print('-' * (len(columnHeader) + 2), end='+')
        print(' \n|', end='')

        for columnHeader in self.columnHeader:
            # Column-Header
            print(' ', columnHeader, ' |', sep='', end='')
        print('\n+', end='')

        for columnHeader in self.columnHeader:
            # Bottom-Outline
            print('-' * (len(columnHeader) + 2), end='+')
        print(' \n', end='')


DBMS = DatabaseManagement()
DBMS.makeTable()
