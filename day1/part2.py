import re

NUMBERS_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

def main():
    example_lines = read_file("day1/inputs/example2.txt")
    input_lines = read_file("day1/inputs/input2.txt")
    
    print("Case 2 example:", solve_part2(example_lines))
    print("Case 2 input:", solve_part2(input_lines))
    
def solve_part2(lines):
    total_sum = 0
    for line in lines:
        first_number = find_string_number(line, 1)
        last_number = find_string_number(line, 2)
        total_sum += int(first_number + last_number)
    return total_sum

def find_string_number(string, part):
    regex = re.compile('|'.join(re.escape(string) for string in NUMBERS_MAP.keys()))
    matches = regex.findall(string)

    if matches:
        if part == 1:
            return NUMBERS_MAP[matches[0]]
        else:
            return NUMBERS_MAP[matches[-1]]
    else:
        return '0'
        
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
        
if __name__ == "__main__":
    main()