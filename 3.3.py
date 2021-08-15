str_list = ['Chile', 'b', 'c']
print('第一种循环取值方式： 直接取值')
for sub_str in str_list:
    print(sub_str)

print('-------------------')

print('第二种循环取值方式：索引取值')
for i in range(len(str_list)):
    print(str_list[i])

print('-------------------')

str_list = ['Chile', 'b', 'c']
i = 0
while i < len(str_list):
    print(str_list[i])
    i += 1

print('-------------------')

str_list = ['Chile', 'b', 'c']
mix_tuple = ('chile', 111, 2.2, 'a', str_list)
print('第一种循环取值方式：直接取值')
for sub_tuple in mix_tuple:
    print(sub_tuple)

print('-------------------')
print('第二种循环取值方式：索引取值')
for i in range(len(mix_tuple)):
    print(mix_tuple[i])
print('-------------------')

str_list = ['Chile', 'b', 'c']
mix_tuple = ('chile', 111, 2.2, 'a', str_list)
i = 0
while i < len(mix_tuple):
    print(mix_tuple[i])
    i += 1

print('-------------------')

str_list = ['Chile', 'b', 'c']
mix_tuple = ('chile', 111, 2.2,  str_list)
num_list = [1, 2, 3, 4]

test_dict = {'name': 'Chile', 'age': '18', 'num_list': num_list, 'mix_tuple': mix_tuple}
for keys in test_dict.keys():
    print('keys:', keys)
    print('value:', test_dict[keys])

print('-------------------')

test_set = {'abc', 1, 1, '1', 'chile'}
for value in test_set:
    print(value,  '', type(value))

print('-------------------')

a = 1
b = '1'
if a == b:
    print('a == b')
else:
    print('a != b')

print('-------------------')

a = 1
b = 2
if a > b:
    print('a>b')
elif a < b:
    print('a<b')
else:
    print('a == b')

print('-------------------')

a = True
b = False
if a and b:
    print('True')
else:
    print('False')

if a or b:
    print('True')
else:
    print('False')

if a and (not b):
    print('True')
else:
    print('False')

print('-------------------')

with open('text.txt', 'w') as fw:
    string = 'I am chile!'
    for i in range(5):
        fw.write(string + '\n')
with open('text.txt', 'r') as fr:
    for line in fr:
        print(line)

print('-------------------')

with open('text.txt', 'a') as fw:
    string = 'You are handsome!'
    for i in range(5):
        fw.write(string + '\n')
with open('text.txt', 'r') as fr:
    for line in fr:
        print(line)

print('-------------------')

try:
    with open('text.txt', 'r') as fr:
        text = fr.read()
except IOError:
    print('The file does not exist!')

else:
    print('Succeed!')

print('-------------------')


import time
print(time.strftime("%Y- %m- %d %H: %M: %S",time.localtime()))


