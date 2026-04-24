from enum import Enum

class Operators(Enum):
    MORETHAN = '>'
    MORETHANEQUALS = '>='
    LASTTHAN = '<'
    LASTTHANEQUALS = '<='
    EQUALS = '='
    LIKE = 'L'
    IN = 'IN'
    DIFFERENT = '!='
    