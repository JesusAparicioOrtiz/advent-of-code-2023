import re

CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    example_lines = read_file("day2/inputs/example.txt")
    input_lines = read_file("day2/inputs/input1.txt")
    
    print("Case 1 example: " + str(solve_1_part(example_lines)))
    print("Case 1 input: " + str(solve_1_part(input_lines)))
    
def solve_1_part(lines):
    total_sum = 0
    for line in lines:
        game = line.split(':')
        if is_possible(line):
            game_id = game[0].split(' ')[1]
            total_sum += int(game_id)
    return total_sum

def is_possible(line):
    game = line.split(':')
    reveals = game[1].split('; ')
    for reveal in reveals:
        subsets = reveal.strip().split(', ')
        for subset in subsets:
            subset_parts = subset.split(' ')
            if int(subset_parts[0]) > CUBES[subset_parts[1]]:
                return False
    return True

def is_subset_possible(subset):
    subset_parts = subset.split(' ')
    if int(subset_parts[0]) > CUBES[subset_parts[1]]:
        return False
    return True
        
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
        
if __name__ == "__main__":
    main()