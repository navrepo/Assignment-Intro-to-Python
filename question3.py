# Question 3: Grade Average Calculator (Lessons 1-4 Combined)
# Build a grade calculator that uses loops and functions to process student scores.
# Requirements:
# Create a function calculate_average(scores) that:
# Takes a list of scores as a parameter
# Calculates and returns the average
# Create a function get_letter_grade(average) that:
# Takes an average score as a parameter
# Returns letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (below 60)
# Use a while loop to:
# Ask how many test scores to enter
# Collect each score from the user
# Store scores in a list
# Display the average and letter grade using your functions

 
def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0       
def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def main():
    scores = []
    num_scores = int(input("How many test scores do you want to enter? "))
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)
    average = calculate_average(scores)
    letter_grade = get_letter_grade(average)
    print("\n=== GRADE REPORT ===")
    print(f"Test Scores: {scores}")
    print(f"Average Score: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
if __name__ == "__main__":
    main()      






# Example Output:
# How many test scores do you want to enter? 4
# Enter score 1: 85
# Enter score 2: 92
# Enter score 3: 78
# Enter score 4: 88

# === GRADE REPORT ===
# Test Scores: [85, 92, 78, 88]
# Average Score: 85.75
# Letter Grade: B

# Enter score 1: 95
# Enter score 2: 87
# Enter score 3: 91

# === GRADE REPORT ===
# Test Scores: [95, 87, 91]
# Average Score: 91.0
# Letter Grade: A
