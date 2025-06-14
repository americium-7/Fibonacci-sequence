def generate_fibonacci_sequence():

    print("Fibonacci Sequence Generator")
    print("---------------------------")
    
    while True:
        try:
            num_terms = int(input("Enter the number of terms (≥1): "))
            
            if num_terms < 1:
                print("Please enter a positive integer.")
                continue
                
            if num_terms == 1:
                print("\nFibonacci sequence (1 term):")
                print("[0]")
                break
                
            sequence = [0, 1]
            for i in range(2, num_terms):
                next_term = sequence[-1] + sequence[-2]
                sequence.append(next_term)
            
            print(f"\nFibonacci sequence ({num_terms} terms):")
            print(sequence)
            break
            
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

generate_fibonacci_sequence()