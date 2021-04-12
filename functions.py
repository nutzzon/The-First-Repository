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


def secondfunc(f, s, ip='+'):
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

x = secondfunc(25, 5, ':')
print(x)