#Abdirahman Mohamed CSC 335 Project 6
class SymbolTable(object):
    def __init__(self):
        """Initilizes symbols that is associated with memory locations"""
        self._symbols \
            = {'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,
               'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
               'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13, 'R14':14, 'R15':15,
               'SCREEN':0x4000, 'KBD':0x6000}

    def add_entry(self, symbol, address):
        """Equals the symbols to an address variable"""
        self._symbols[symbol] = address

    def contains(self, symbol):
        """Returns the symbol in the symbols dictionary"""
        return symbol in self._symbols

    def get_address(self, symbol):
        """Returns the symbols that are associated with the adress"""
        return self._symbols[symbol]
