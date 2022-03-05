import re
import json
import os

from isort import file
from quadratic_equations import formulas


def input_by_user():
    a = int(input('Masukan Nilai a : '))
    b = int(input('Masukan Nilai b : '))
    c = int(input('Masukan Nilai c : '))

    if  a != None and b != None and c != None:
        return formulas(a,b,c)
    else:
        raise ValueError('ERROR')


def input_by_file(filename):

    input_txt = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            pattern = r'(\w)=(-?\d*)'
            match = re.search(pattern, line.strip())

            if match != None:
                coefisient = match.group(1)
                value = match.group(2)

                input_txt[coefisient] = value
                

        input_a = int(input_txt['a'])
        input_b = int(input_txt['b'])
        input_c = int(input_txt['c'])
        formulas(input_a, input_b, input_c)

def input_by_json(filename):

    input_json = {}
    with open (filename, 'r') as file:
        load_json = json.load(file)

        chose_data = int(input('Masukan nomor data yang ingin dipilih :'.upper()))


        if chose_data != 0 and chose_data <= len(load_json['list_data']):
            chose_data -= 1
            for keys, items in load_json['list_data'][chose_data].items():
                input_json[keys] = items
            
            chosen_data_json = input_json['data']
            print(f'Data yang dipilih : {chosen_data_json}')

            input_json_a = int(input_json['a'])
            input_json_b = int(input_json['b'])
            input_json_c = int(input_json['c'])
            formulas(input_json_a, input_json_b, input_json_c)
        elif chose_data == 0:
            raise ValueError('Out of range lenght'.upper())
        else:
            raise ValueError('Out of range lenght'.upper())
            
        


# Direktory file
path = os.path.dirname(__file__)

# Output by scripts
a = 1
b = 2
c = 1
print('='*50)

print('OUTPUT FROM SCRIPT\n')
formulas(a,b,c)
print('='*50)


# Output by User
print('='*50)
print('OUTPUT BY USER\n')
input_by_user()
print('='*50)

# Output by file (.txt)]
print('='*50)
print('OUTPUT BY File (.txt)\n')
file_path = 'src/input.txt'
input_by_file(os.path.join(path, file_path))
print('='*50)

# Output by json
print('='*50)
print('OUTPUT BY JSON\n')
json_path = 'src/input_json.json'
input_by_json(os.path.join(path, json_path))
print('='*50)