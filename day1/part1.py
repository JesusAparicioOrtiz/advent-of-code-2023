import re

def main():
    example_lines = read_file("day1/inputs/example.txt")
    input_lines = read_file("day1/inputs/input1.txt")
    
    print("Case 1 example: " + str(solve_1_part(example_lines)))
    print("Case 1 input: " + str(solve_1_part(input_lines)))
    
def solve_1_part(lines):
    total_sum = 0
    for line in lines:
        numbers = ''.join(re.findall(r'\d', line))
        total_sum += int(numbers[0] + numbers[-1])
    return total_sum
        
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
        
if __name__ == "__main__":
    main()