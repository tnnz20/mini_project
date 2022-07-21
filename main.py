import re
import json
import os

# Import formula Quadratic Equations
from quadratic_equations import formulas

def line():
    """
    Functions for create line
    """
    return print('='*50)

def input_from_script(a, b, c):
    """
    Functions for input from script
    """

    print('Ouput from script\n'.upper())
    return formulas(a, b, c)

def input_by_user(a, b, c):
    """
    Functions for add input by user
    """

    # Check input
    check_input_none = a.strip() == '' or b.strip() == '' or c.strip() == ''
    check_input_str = a.isalpha() or b.isalpha() or c.isalpha()
    if check_input_none or check_input_str:
        raise ValueError('Please enter a number')
    else:
        print('Ouput from user\n'.upper())
        return formulas(a, b, c)


def input_by_file(filename):
    """
    Functions for add input by file (.txt)
    """

    input_txt = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            pattern = r'(\w)=(-?\d*)'
            # Find exist data
            match = re.search(pattern, line.strip())

            # Input match data to new dictionary
            if match != None:
                coefisient = match.group(1)
                value = match.group(2)

                input_txt[coefisient] = value
                

        input_a = input_txt['a']
        input_b = input_txt['b']
        input_c = input_txt['c']

    print('Ouput from file (.txt)\n'.upper())
    return formulas(input_a, input_b, input_c)

def input_by_json(filename, chosen_data):
    """
    Functions for add input by file (.json)
    """

    input_json = {}
    with open (filename, 'r') as file:
        load_json = json.load(file)
        length_data = len(load_json['list_data'])

        # Check chosen input
        if chosen_data != 0 and chosen_data <= length_data:
            chosen_data -= 1

            # Input Data JSON to new Dictionary
            for keys, items in load_json['list_data'][chosen_data].items():
                input_json[keys] = items
            
            chosen_data_json = input_json['data']
            

            # Load Data JSON 
            input_json_a = input_json['a']
            input_json_b = input_json['b']
            input_json_c = input_json['c']

            print('Ouput from JSON\n'.upper())
            print(f'Chosen data : {chosen_data_json}')
            return formulas(input_json_a, input_json_b, input_json_c)
        else:
            raise ValueError('Out of range lenght'.upper())
            
        

def main():
    # Set up Path
    path = os.path.dirname(__file__)        # File dir
    file_path = 'src/input.txt'             # .txt dir
    json_path = 'src/input_json.json'       # JSON dir

    # Input value
    print('Input value from users')
    a = input('Enter value a: ')
    b = input('Enter value b: ')
    c = input('Enter value c: ')

    print('\nChose data from JSON data (1-3)')
    chosen_data = int(input('Enter chosen data: '))

    # Clear screen
    os.system('cls')

    line()
    input_from_script(1, 2, 1)
    line()
    input_by_user(a, b, c)
    line()
    input_by_file(os.path.join(path, file_path))
    line()
    input_by_json(os.path.join(path, json_path), chosen_data)
    line()

if __name__ == '__main__':
    os.system('cls')
    main()