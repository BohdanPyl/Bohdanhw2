def print_big(a, b):
    if a > b:
        print(f'a == {a} - bigger')
    elif a == b:
        print('a == b')
    else:
        print(f'b == {b} - bigger')


print_big(15, 11)
print_big(5, 11)
print_big(17, 11)
print_big(15, 101)
print_big(15, 1001)
print_big(125, 11)

# or 

def plus(a, b):
    return a + b

print(plus(9, 13))


