import sys

from .spreadsheet import Spreadsheet
from .viewport import Viewport


def cli():
    filename = sys.argv[1]

    spreadsheet = Spreadsheet.from_xls(filename, Viewport('B3:E13'))

    print(str(spreadsheet))
