'''A docstring (documentation string) is a special string used to describe what a function, class, or module does.
It's written just after the definition of a function, class, or module using triple quotes (""" """ or ''' ''').
Python uses it to generate documentation automatically (like when you use help()).'''

def sum(a, b):
    '''This will sum two numbers'''
    c = a + b
    return c

print(sum(2,2))
print(sum.__doc__)