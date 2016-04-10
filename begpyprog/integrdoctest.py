"""
This is an explanation of integr

Cheating slightly - book called for:
    BadInput: 'abcd' not valid
For convenience, I did:
    BadInput: ['abcd'] not valid

>>> import integr
>>> integr.parse('1,3,4')
[1, 3, 4]

Includes whitespace handling!
>>> integr.parse('1, 3, 4 ')
[1, 3, 4]

Gracefully fails!
>>> integr.parse('abcd')
Traceback (most recent call last):
  ...
BadInput: ['abcd'] not valid
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

