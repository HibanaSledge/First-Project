num_list = [1, 2, 4, 5]
str_list = ['Stuart', 'c']
mix_tuple = ('1', 1, 'Car')
test_set = {1, 'stuart', 1.1, '1'}
mix_list = ['a', 1, 11, 1.0, num_list, str_list, mix_tuple, test_set]
print(mix_list)
for sub_str in mix_list:
    print(sub_str)

print('-----------')
for i in range(len(mix_list)):
    print(mix_list[i])

print('-----------')

class School(object):
    def __init__(self, name, ranking):
     self.name = name
     self.ranking = ranking

    def print_name(self):
        print(self.name)
    def school_ranking(self):
        print('My ranking is:', self.ranking)

Polyu = School('Polyu', 50)
TsingHua = School('Tsinghua', 5)
Polyu.school_ranking()
TsingHua.school_ranking()

