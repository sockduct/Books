from peeker import Peeker, PeekDone

def blank(line):
    """This assumes a line which is all whitespace is `blank'.
       Could also do:  if line in ['\n', '\r\n', '\r']:
    """
    if not line.strip():
        return True
    else:
        return False

def fix_space_in_paragraph(lines):
    """ If paragraphs span pages (often) then there
        could be extra returns in the paragraphs....

        This removes multiple blank lines between
        paragraphs.
    """
    lines = Peeker(lines)
    for line in lines:
        try:
            line2 = lines.peek()
        except PeekDone as e:
            yield line
            return
        try:
            line3 = lines.peek(1)
        except PeekDone as e:
            yield line
            yield line2
            return
        # Not clear what "ends_sentence" should do so changed:
        #if blank(line2) and not ends_sentence(line):
        if blank(line2) and not blank(line):
            # don't use line2 so pop it
            lines.pop()
        yield line

