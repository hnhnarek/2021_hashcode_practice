import numpy as np
import matplotlib.pyplot as plt
import os

def process_input(file_path):
    """
    process_input('../dir/a_example.txt')
    """
    mapping = {  
        'a': 'input_files/a_example.in',
        'b': 'input_files/b_little_bit_of_everything.in',
        'c': 'input_files/c_many_ingredients.in',
        'd': 'input_files/d_many_pizzas.in',
        'e': 'input_files/e_many_teams.in'
    }
    if file_path in mapping:
        file_path = mapping[file_path]
    file = {'data': open(file_path).readlines(), 'name': file_path.split('/')[-1]} 
    
    first_line = file['data'][0].split(' ')
    
    objs_count = int(first_line[0])
    M = objs_count
    T2 = int(first_line[1])
    T3 = int(first_line[2])
    T4 = int(first_line[3])
    # similar general info
    
    objs = []
    for i, value in enumerate(file['data'][1:]):
        tokens = value.strip().split(' ')
        temp = {
            'id': i,
            'count': int(tokens[0]),
            'ingredients': sorted(tokens[1:]),
        }
        objs.append(temp)
    if len(objs) == objs_count:
        file['data'] = objs
        file['N'] = objs_count
        file['T2'] = T2
        file['T3'] = T3
        file['T4'] = T4
        file['M'] = M
        return file


def score(input_file_name, filename):
    mapping = {  
        'a': 'input_files/a_example.in',
        'b': 'input_files/b_little_bit_of_everything.in',
        'c': 'input_files/c_many_ingredients.in',
        'd': 'input_files/d_many_pizzas.in',
        'e': 'input_files/e_many_teams.in'
    }
    if input_file_name in mapping:
        input_file_name = mapping[input_file_name]
    data = process_input(input_file_name)
    f = open(filename).readlines()
    D = int(f[0].strip())
    deliveries = [(int(i.split()[0]),list(map(int,i.split()[1:]))) for i in f[1:]]
    if len(deliveries) != D:
        raise Exception("Wrong number of deliveries")
    score = 0
    for d in deliveries:
        if d[0]!= len(d[1]):
            raise Exception("Wrong number of pizzas")
        ings = [data['data'][i]['ingredients'] for i in d[1]]
        ings_list = []
        for p in ings:
            ings_list.extend(p)
        ings_set = list(set(ings_list))
        score += (len(ings_set)**2)
    return score