from stack_q4 import Stack
def reverse_file_content(input_file, output_file):
    stack = Stack()

    with open(input_file, "r") as file:
        for line in file:
            stack.push(line)

    with open(output_file, "w") as file:
        while not stack.is_empty():
            file.write(stack.pop())

# Example usage
input_file = "input.txt"
output_file = "output.txt"

reverse_file_content(input_file, output_file)
print("File reversed successfully!")
