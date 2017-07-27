def type_of_tents():
    """ str -> str
    tent sizes 
    """
    tent_sizes = ['Tent 1 = 10X10\t\t' 'Tent 7 = 10X10 w/ 6 chairs & 1 table',
    'Tent 2 = 10X20\t\t' 'Tent 8 = 10X20 w/ 15 chairs & 3 tables',
    'Tent 3 = 16X16\t\t' 'Tent 9 = 10X20 w/ 20 chairs & 4 tables',
    'Tent 4 = 20X20\t\t' 'Tent 10 = 10X20 w/ 40 chairs & 6 tables',
    'Tent 5 = 20X30\t\t' 'Tent 11 = 10X20 w/ 55 chairs & 7 tables',
    'Tent 6 = 20X40\t\t' 'Tent 12 = 10X20 w/ 70 chairs & 8 tables']
    return tent_sizes

def cost_of_tents(tent):
    ''' string -> string 
    Prices of the avalible tents
    >>> cost_of_tents(1)
    50
    >>> cost_of_tents(12)
    330    
    '''
    tent1 = 50   
    tent2 = 75
    tent3 = 82
    tent4 = 115
    tent5 = 170
    tent6 = 285
    tent7 = 75
    tent8 = 125
    tent9 = 132
    tent10 = 165
    tent11 = 220
    tent12 = 330

    if tent == '1' or tent.lower() == 'one':
        return tent1 
    elif tent == '2' or tent.lower() == 'two':
        return tent2
    elif tent == '3' or tent.lower() == 'three':
        return tent3
    elif tent == '4' or tent.lower() == 'four':
        return tent4
    elif tent == '5' or tent.lower() == 'five':
        return tent5
    elif tent == '6' or tent.lower() == 'six':
        return tent6
    elif tent == '7' or tent.lower() == 'seven':
        return tent7
    elif tent == '8' or tent.lower() == 'eight':
        return tent8
    elif tent == '9' or tent.lower() == 'nine':
        return tent9
    elif tent == '10' or tent.lower() == 'ten':
        return tent10
    elif tent == '11' or tent.lower() == 'eleven':
        return tent11
    elif tent == '12' or tent.lower() == 'twelve':
        return tent12 

def deposit(tents):
    """deposit for every tent
    >>> deposit(50)
    55.0
    >>> deposit(75)
    82.5
    """
    return (float(tents) * float(.1)) + float(tents)

def total(tents):
    """ returns the total price of a tent, tent price plus
    deposit plus sales tax.
    >>> total(50)
    53.5
    """
    return (float(tents) * float(.07)) + float(tents)
