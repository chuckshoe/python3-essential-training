#!/usr/bin/python3

a, b = 0, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

''' 
for ternary operator : a<b ? "foo":"bar"
Equivalent python : "foo" if a<b else "bar"
'''
print("foo" if a<b else "bar")
