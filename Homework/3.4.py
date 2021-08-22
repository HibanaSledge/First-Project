def print_value():
    return 1
print_value()

print('-------------------')

def print_value():
    print('Chile')
print_value()
print('-------------------')

def print_value(a,b):
    if a > b:
        print('a>b')
    elif a < b:
        print('a<b')
    else:
        print('a==b')

#三种调用方式
print_value(1,2)

a = 1
b = 2
print_value(a,b)

print_value(a=1, b=2)
print('-------------------')

def print_value(a_test, b_test):
    if a > b:
        return'a > b'
    elif a < b:
        return'a < b'
    else:
        return'a==b'

#三种调用方式
print(print_value(1,2))

a = 1
b = 2
print(print_value(a,b))

print(print_value(a_test=1, b_test=2))
print('-------------------')

class Phone(object):
    def __init__(self, name, price):
     self.name = name
     self.price = price

    def print_price(self):
        print(self.price)
    def assistant(self):
        print('I have an assistant!')
    def wifi(self):
        print('I have WIFI!')

iphone = Phone('iphone', 8500)
huawei = Phone(name= 'huawei', price= 5555)
print(iphone.price)
huawei.print_price()
print('-------------------')

class Iphone(Phone):
    def operation_system(self):
        return 'ios'
iphone = Iphone('iphone', 8500)
print(iphone.operation_system())
print('-------------------')

class Iphone(Phone):
    def assistant(self):
        print('I have siri assistant!')

class Huawei(Phone):
    def assistant(self):
        print('I have hormony assistant!')

iphone = Iphone('iphone', 5200)
huawei = Huawei(name= 'huawei', price = 1000)
iphone.assistant()
huawei.assistant()
print('-------------------')

def get_assistant(Phone):
    Phone.assistant()
get_assistant(Phone('phone', 500))
get_assistant(Iphone('iphone', 8888))
get_assistant((Huawei('huawei', 5200)))

