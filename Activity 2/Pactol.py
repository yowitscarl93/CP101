def compute_average(scores):
    return sum(scores) / len(scores)

def main():
    #scores for each subject
    print("Enter your scores:")
    math_score = float(input("Math: "))
    science_score = float(input("Science: "))
    english_score = float(input("English: "))
 
    scores = [math_score, science_score, english_score]

    #to calculate the ave
    average = compute_average(scores)
    
    print("Your average score is:", average)

main()
