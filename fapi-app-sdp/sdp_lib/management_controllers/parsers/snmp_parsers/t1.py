import functools


def f1(arg, scn=None):
    print('arg: ', arg)
    return arg


fun1 = functools.partial(f1, 'beee', scn='12.12.14')

print(fun1)
print(fun1())