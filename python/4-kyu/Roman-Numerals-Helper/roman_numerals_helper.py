class RomanNumerals:

    ROMAN_NUMERALS = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD':  400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    @classmethod
    def to_roman(self, n):
        number = ''
        for roman_numeral, integer in self.ROMAN_NUMERALS.items():
            while n >= integer:
                n -= integer
                number += roman_numeral
        return number

    @classmethod
    def from_roman(self, roman):
        number, index = 0, 0
        for roman_numeral, integer in self.ROMAN_NUMERALS.items():
            while roman[index:index+len(roman_numeral)] == roman_numeral:
                index += len(roman_numeral)
                number += integer
        return number
