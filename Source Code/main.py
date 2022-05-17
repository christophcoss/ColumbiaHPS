from EnvironmentalDischarge import *
from LCOE import *
from Parsers import *

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f1())
    print(f2())
    print(f3())
    print(f6())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = excelParser('Data/FlowData.xlsx', None)
    print(data)


    # this is just a test to make sure that it works
    print(calcLCOE(10000, 500, 500, 0.08, 10))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
