def convert_list(array_list):
    dict_root = {}
    dict_child1 = {}
    dict_child2 = {}
    dict_child2[array_list[2]] = array_list[3]
    dict_child1[array_list[1]] = dict_child2
    dict_root[array_list[0]] = dict(dict_child1)
    return dict_root


data = ['2018-01-01', 'yandex', 'cpc', 100]
print(convert_list(data))
