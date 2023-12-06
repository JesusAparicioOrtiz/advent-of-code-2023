import re
from math import prod
CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    example_lines = read_file("day2/inputs/example.txt")
    input_lines = read_file("day2/inputs/input2.txt")
    
    print("Case 1 example: " + str(solve_1_part(example_lines)))
    print("Case 1 input: " + str(solve_1_part(input_lines)))
    
def solve_1_part(lines):
    total_sum = 0
    for line in lines:
        total_sum += int(calculate_power(line))
    return total_sum

def calculate_power(line):
    reveals = line.split(': ')[1]
    color_max_numbers = {}
    subsets = re.findall(r'\d+\s\w+', reveals)
    
    for subset in subsets:
        subset_parts = subset.split(' ')
        number, color = int(subset_parts[0]), subset_parts[1]
        if color not in color_max_numbers or number > color_max_numbers[color]:
            color_max_numbers[color] = number    
            
    return prod(color_max_numbers.values())
        
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
        
if __name__ == "__main__":
    main()