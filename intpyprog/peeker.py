class PeekDone(Exception):
    pass

class Peeker(object):
    def __init__(self, seq):
        self.seq = iter(seq)
        self.buffer = []

    def pop(self):
        if self.buffer:
            return self.buffer.pop(0)

    def peek(self, n=0):
        """ This can raise an exception if peeking off the end.
            Be aware and handle PeekDone appropriately.
        """
        try:
            if n == len(self.buffer):
                self.buffer.append(self.seq.next())
        except StopIteration as e:
            raise PeekDone('Exhausted')
        return self.buffer[n]

    def __iter__(self):
        return self

    def next(self):
        if self.buffer:
            return self.buffer.pop(0)
        else:
            return self.seq.next()

