# this file should include all functions that should do something
# for example, it can fetch a mobile string for other users

def firstfunc(x, y):
    ''' 
    Documentation
    --------------------
    PARAMS: x, y 
        x: first argument, should be integer or float
        y: second argument, should be text or string 

    OUTPUT: object / string
        string containing all only text that should be contained. 

    EXAMPLE:
        >>> firstfunc(3, "hi! I am _ years old")
        out: hi! I am 3 years old 
    '''
    return y.replace('_', str(x))


def secondfunc(first, second, input = '+'):
    '''
    'makes operation based on inputs'
    -----------------
    Documentation
    -----------------
    PARAMS: first, second, input
        first: first argument, should be integer or float
        second: second argument, should be integer or float
        input: operator object: possibilities; +, -, *, :

    OUTPUT: float / integer 
        integer with the value of the operation between the two inputs

    EXAMPLE: 
        >>> secondfunc(4, 3, '-'):
        out: 1
    '''
    if input=='-':
        return first - second
    elif input=='*':
        return first*second
    elif input == ':':
        return first/second
    else:
        return first+second


def thirdfunc(f, s, ip='+'):
    '''
    Documentation
    ---------------------
    DESC:
        this functions applies the operation to two integers / floats and 
        returns the value of gotten from the applied function.

    PARAMS: f, s, ip
        f: integer / float; first argument
        s: integer / float; second argument
        ip: operation symbol; optionsal 

    OUTPUT: integer / float
        the value from the chosen operation

    EXAMPLE:
        >>> secondfunc(4, 3, ip='-')
        out: 1
    '''

    if ip == '-':
        return f - s
    elif ip == ':':
        return f / s
    elif ip == '*':
        return f*s
    else:
        return f + s


# first function

print(firstfunc(25, 'hi! my name is Richard and I am _ years old. This means\
                    that we I have been on this planet _ years.'))

# second function

x = thirdfunc(25, 5, ':')
print(x)

