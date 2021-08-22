import re
print(re.match('Chile', 'ChileWang'). span())
print(re.match('Wang','ChileWang'))
print('-------------------')

import re
print(re.match('Chile', 'ChileWang').span())
print(re.match('Wang', 'ChileWang'))
print('-------------------')

import re

phone =  "1234567@qq.com"
num = re.sub(r'#.*$',"", phone)
print("QQ邮箱是：", num)

num = re.sub(r'\D+', "@163.com",phone)
print("163邮箱是：", num)
print('-------------------')

import re

pattern = re.compile(r'\d+')
result1 = pattern.findall('Chile 111 Wang 222')
result2 = pattern.findall('Chi111le444Wang333', 0, 11)

print(result1)
print(result2)
print('-------------------')



