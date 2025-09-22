# will review

def calculate_average(scores):
    return sum(scores) / len(scores)        
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
    count = 0
    while count < num_scores:
        score = float(input(f"Enter score {count + 1}: "))
        scores.append(score)
        count += 1
    average = calculate_average(scores)
    letter_grade = get_letter_grade(average)
    print("\n=== GRADE REPORT ===")
    print(f"Test Scores: {scores}")
    print(f"Average Score: {average}")
    print(f"Letter Grade: {letter_grade}")
if __name__ == "__main__":
    main()

