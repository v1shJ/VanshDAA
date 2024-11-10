import random
def generate_grade_strings(num_strings=20, string_length_range=(40, 40), common_substrings=None):
    # List of possible grades and corresponding probabilities
    grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'FF']
    probabilities = [0.05, 0.25, 0.25, 0.25, 0.15, 0.1, 0.08, 0.02]
    
    if common_substrings is None:
        common_substrings = ["AB", "BB", "BC"]  # Define some common substrings

    generated_strings = []

    for _ in range(num_strings):
        length = 40
        string = ""

        # Fill the rest of the string with grades chosen based on specified probabilities
        while len(string) < length * 2:  # Multiply by 2 since each grade is 2 characters
            string += random.choices(grades, probabilities)[0]
        print(len(string))

        generated_strings.append(string[:80])  # Ensure the string matches the required length

    print(generated_strings)
    return generated_strings

generate_grade_strings()