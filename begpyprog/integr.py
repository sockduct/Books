####################################################################################################
'''
Simple program to convert a string of integers separated by commas into an integer list
'''

# Imports
import sys
from BadInput import BadInput

__version__ = '0.0.1'

def parse(input):
    curlst = input.replace(' ', '')
    curlst = curlst.split(',')
    try:
        newlst = [int(i) for i in curlst]
    except ValueError as e:
        raise BadInput(curlst)
    #except ValueError as e:
    #    newlst = None
    #    print 'Skipping invalid input - {}'.format(str(curlst))
    #except Exception as e:
    #    print 'Unhandled except - {}, aborting...'.format(str(e))
    #    sys.exit(-2)
    return newlst

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage:  {} <string of integers separated by commas> [<str2> ...]'.format(
                sys.argv[0])
        sys.exit(-1)
    for elmt in sys.argv[1:]:
        print parse(elmt)

