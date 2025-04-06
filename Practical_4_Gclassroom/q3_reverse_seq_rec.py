def reverse_seq(seq):
    return seq if len(seq) <= 1 else reverse_seq(seq[1:]) + seq[0]

if __name__ == "__main__":
    result = reverse_seq("hello")
    print(f"Reversed 'hello': {result}")