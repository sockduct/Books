from peeker import Peeker, PeekDone

def blank(line):
    """This assumes a line which is all whitespace is `blank'.
       Could also do:  if line in ['\n', '\r\n', '\r']:
    """
    if not line.strip():
        return True
    else:
        return False

def remove_double_returns(lines, verbose=False):
    lines = Peeker(lines)
    for line in lines:
        if verbose:
            print('>line:  {}'.format(line.rstrip()))
        try:
            next_line = lines.peek()
            if verbose:
                print('>next_line:  {}'.format(next_line.rstrip()))
        except PeekDone as e:
            yield line
            return

        if blank(next_line):
            if verbose:
                print('>--Next line blank, removing...')
            yield line
            lines.pop()
        else:
            yield line

