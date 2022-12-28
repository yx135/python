def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print('0!')
except:
    print('other')