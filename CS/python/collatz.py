def collatz_sequence(n):
    """
    Function to calculate and print the Collatz sequence starting from n.
    """
    steps = 0
    if n <= 0:
        raise ValueError("The starting number must be a positive integer.")
    
    sequence = []  # List to store the sequence
    while n != 1:
        sequence.append(n)  # Append the current value of n to the sequence
        if n % 2 == 0:
            n = n // 2  # Apply the rule for even numbers
            steps + 1
        else:
            n = 3 * n + 1  # Apply the rule for odd numbers
            steps + 1
    sequence.append(1)  # Add the final 1 to the sequence
    return sequence

# Example usage
start_number = int(input("Enter a positive integer to start the Collatz sequence: "))
collatz_seq = collatz_sequence(start_number)
print("Collatz sequence:", collatz_seq)
print("It took", len(collatz_seq) - 1, "steps to reach 1.")
