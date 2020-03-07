# Use Modern Python
from __future__ import unicode_literals, absolute_import, print_function

# System imports
import csv

# External libraries
import six


def parse_line(value, quotechar=None, **kwargs):
    """
    A simple wrapper to parse a single CSV value
    """

    quotechar = quotechar or '"'

    for row in csv.reader([value], quotechar=quotechar, **kwargs):
        return row

def line_to_string(value, **kwargs):
    """
    A simple wrapper to write one CSV line
    """

    fh = six.StringIO()
    csv.writer(fh, **kwargs).writerow(value)
    return fh.getvalue()
