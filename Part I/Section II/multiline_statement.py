
# certain physical newlines are ignored in order to form a complete logical line of code.


# Implicit Examples
x = [
    'priya',   # 1st child << inline comment
    'muthu',
    'paul'
]


# Multi-Line String used as docstring though it's just regular string
def calc_age(
        birth_year:int           # birth_year e.g) 1998
    )->int:
    '''
        functions helps to calculate age
    '''
    # Explicit use `\` character to explicitly create multi-line statements.
    if birth_year>2024  and \
        isinstance(birth_year,int):
        return(0)
    return(2024-birth_year)



if __name__=='__main__':
    pass