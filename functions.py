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


print(firstfunc(25, 'hi! my name is Richard and I am _ years old. This means\
                    that we I have been on this planet _ years.'))

