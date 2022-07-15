def is_vowel(x):
    '''
    is_vowel:
    parameter: x, a string value
    returns: true if x is avowel, false if x is anything else
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel:
        if x.lower() == v:
            return True
    return False


def calculate_tip(x, y):
    '''
    calculate_tip:
    parameters: (x [a numerical value between 0 and 1] , y [the bill total])
    returns: new numerical value representing total tip amount
    '''
    x = x/100
    tip_amount = format(x * y, '.2f')
    return f'${tip_amount}'


def get_letter_grade(x):
    '''
    get_letter_grade:
    parameters: x, a numerical value representing a grade
    returns: x as a string variant of its numerical value
    '''
    if x > 89:
        return 'A'
    elif x > 79:
        return 'B'
    elif x > 69:
        return 'C'
    elif x > 59:
        return 'D'
    else:
        return 'F'

def con_str(x):
    x = x.replace(',', '')
    for i in x:
        if i.isalnum() == False:
            x = x.replace(i,'')
            break
    x = float(x)
    return x

def sum_all(list):
  total = 0
  for x in list:
    total += x
  return total

