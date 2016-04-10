####################################################################################################
'''
Simple Exception case to handle bad input
'''

# Imports

__version__ = '0.0.1'

class BadInput(Exception):
    def __init__(self, bad_input):
        Exception.__init__(self, '{} not valid'.format(bad_input))
        self.bad_input = bad_input

