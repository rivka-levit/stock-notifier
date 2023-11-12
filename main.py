import sys
from notifiers import CbxNotifier

try:
    direction, value = sys.argv[1], sys.argv[2]
except IndexError as err:
    raise IndexError('You must provide two arguments: trend direction and '
                     'value that you are waiting for. '
                     '(e.g. "python main.py gt 0.15" or '
                     '"python main.py lt -0.17")') from err
ntf = CbxNotifier()
ntf.notify(direction, value)
