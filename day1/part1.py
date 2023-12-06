import re

def main():
    exampleLines = read_file("day1/inputs/example.txt")
    inputLines = read_file("day1/inputs/input1.txt")
    
    print("Case 1 example: " + str(solve1part(exampleLines)))
    print("Case 1 input: " + str(solve1part(inputLines)))
    
def solve1part(lines):
    sum = 0
    for line in lines:
        numbers = ''.join(re.findall(r'\d', line))
        sum += int(numbers[0] + numbers[-1])
    return sum
        
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
        
if __name__ == "__main__":
    main()