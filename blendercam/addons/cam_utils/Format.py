'''
Format Numbers
'''

import math

class Format:
    '''Format numbers'''

    def __init__(self, scale=1, number_of_decimal_places = 3):
        self.__number_of_decimal_places = number_of_decimal_places
        self.__scale = scale

    def string(self, number):
        if number == None:
            return 'None'
        if isinstance(number, str):
            number = float(number)
        if not isinstance(number, float):
            print("TTTTTTTTTTTTTTTTTT ", type(number), number)
        assert isinstance(number, float) or isinstance(number, int)
        return ("%%.%df" % self.__number_of_decimal_places) % (number * self.__scale)


class OrigFormat:
    def __init__(self, number_of_decimal_places = 3, add_leading_zeros = 1, add_trailing_zeros = False, dp_wanted = True, add_plus = False, no_minus = False, round_down = False):
        self.number_of_decimal_places = number_of_decimal_places
        self.add_leading_zeros = add_leading_zeros # fill the start of the number with zeros, so there are at least this number of digits before the decimal point
        self.add_trailing_zeros = add_trailing_zeros # fill the end of the number with zeros, as defined by "number_of_decimal_places"
        self.dp_wanted = dp_wanted
        self.add_plus = add_plus
        self.no_minus = no_minus
        self.round_down = round_down

    def string(self, number):
        '''Convert a floating point number into a string

        Using the format configuration as passed in during
        construction.
        '''
        # Handle the 'None' case
        if number == None:
            return 'None'

        # Convert to expotent float and string
        f = float(number) * math.pow(10, self.number_of_decimal_places)
        s = str(f)
        print("SSSSSSSSSSSSSSSSSSSSS 0", s)
        
        if self.round_down == False:
            if f < 0:
                f = f - .5
            else:
                f = f + .5
            s = str(number)
            print("SSSSSSSSSSSSSSSSSSSSS 1", s)
            
        if math.fabs(f) < 1.0:
            s = '0'
            
        minus = False
        if s[0] == '-':
            minus = True
            if self.no_minus:
                s = s[1:]
        
        dot = s.find('.')
        if dot == -1:
            before_dp = s
            after_dp = ''
        else:
            before_dp = s[0:dot]
            after_dp = s[dot + 1: dot + 1 + self.number_of_decimal_places]
        
        before_dp = before_dp.zfill(self.add_leading_zeros)
        if self.add_trailing_zeros:
            for i in range(0, self.number_of_decimal_places - len(after_dp)):
                after_dp += '0'
        else:
            after_dp = after_dp.rstrip('0')
                 
        s = ''

        if minus == False:
            if self.add_plus == True:
                s += '+'
        s += before_dp
        if len(after_dp):
            if self.dp_wanted: s += '.'
            s += after_dp
            
        return s
