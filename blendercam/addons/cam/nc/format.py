import math

from cam_utils.Format import Format
    
class Address:
    def __init__(self, text, fmt = Format(), modal = True):
        self.text = text
        self.fmt = fmt
        self.modal = modal
        self.str = None
        self.previous = None
        
    def set(self, number):
        self.str = self.text + self.fmt.string(number)
        
    def write(self, writer):
        if self.str == None: return ''
        if self.modal:
            if self.str != self.previous:
                writer.write(writer.SPACE() + self.str)
                self.previous = self.str            
        else:
            writer.write(writer.SPACE() + self.str)
        self.str = None
    
class AddressPlusMinus(Address):
    def __init__(self, text, fmt = Format(), modal = True):
        Address.__init__(self, text, fmt, modal)
        self.str2 = None
        self.previous2 = None
        
    def set(self, number, text_plus, text_minus):
        Address.set(self, number)
        if float(number) > 0.0:
            self.str2 = text_plus
        else:
            self.str2 = text_minus

    def write(self, writer):
        Address.write(self, writer)
        if self.str2 == None: return ''
        if self.modal:
            if self.str2 != self.previous2:
                writer.write(writer.SPACE() + self.str2)
                self.previous2 = self.str2            
        else:
            writer.write(writer.SPACE() + self.str2)
        self.str2 = None
