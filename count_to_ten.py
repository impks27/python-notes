# Python 3

count = 1
# Code block 1
while count < 11:
    print(count)
    count = count + 1
# Code block 2
if count == 11:
    print('Counting complete.')
# Code block 3
print('for loop')
list = ['a','b','c','d']
for x in list:
   if x == 'c':
    continue
   print(x)

print('for loop range(6)')
for x in range(6):
    print(x)

print('for loop range(2,8)')
for x in range(2,8):
    print(x)

print('for loop range(2,30,3)')
for x in range(2,30,3):
    print(x)
