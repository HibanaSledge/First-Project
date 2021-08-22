a = 1
c = b = 2
print(a)
print(b, c)
print('-------------------')




name = 'Chile'
miles = 1000.0
num = 100
print(type(name))
print(type(miles))
print(type(num))
print('-------------------')

a = 1
b = 1.0
my_name = 'Chile'
print(my_name[0])
print(my_name[1:3])
print(my_name[2:])
print(my_name[-1])
print('-------------------')


num_list = [1, 2, 3, 4]
str_list = ['Chile', 'b', 'c']
mix_list = ['a', 1, 1.0, num_list, str_list]
print(num_list)
print(str_list)
print(mix_list)
print('-------------------')

mix_tuple = ('Chile', 111, 2.2, 'a', num_list)
print(mix_list[1])
print(mix_tuple)


print('-------------------')



test_dict = {'name': 'Chile', 'age': 18, 'num_list': num_list, 'tuple': mix_tuple}
print(test_dict)
print(test_dict.keys())
print(test_dict.values())
print(test_dict['name'])
print(test_dict['num_list'])
print(test_dict['tuple'])
print('-------------------')

test_dict_copy = test_dict
test_dict_copy['name'] = 'alialili'
print(test_dict['name'])
print(test_dict_copy['name'])
print('-------------------')


from copy import deepcopy
test_dict_copy = deepcopy(test_dict)
test_dict_copy['name'] = 'Mary'
print(test_dict['name'])
print(test_dict_copy['name'])
print('-------------------')

test_set = {'abc', 1, 1, '1', 'chile'}
print(test_set)
print('-------------------')

tr_a = '1'
int_b = int(tr_a)
str_c = str(int_b)
float_d = float(str_c)
print(type(tr_a))
print(type(int_b))
print(type(str_c))
print(type(float_d))
print('-------------------')
tr_list = [1, 2, 3]
set_a = set(tr_list)
list_b = list(set_a)
print(type(tr_list))
print(type(set_a))
print(type(list_b))
print('-------------------')

a = 2
b = a+2
c = a-1
d = a*b
e = d/c
f = d%c
g = 3//2
h = 2**3
print('c:', c)
print('d:', d)
print('e:', e)
print('f:', f)
print('g:', g)
print('h:', h)
print('-------------------')

print('abc %d, dhfjdhfhdh, %s, sjdhsjhdhs, skdjskjsk%f, sdjsdhs'%(1, 'Chile', 1.0))
print('abc %d, dhfjdhfhdh, %s, sjdhsjhdhs, skdjskjsk%. 2f, sdjsdhs'%(1, 'Chile', 1.0))
print('-------------------')





