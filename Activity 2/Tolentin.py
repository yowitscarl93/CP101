def compute_average(scores):
    return sum(scores) / len(scores)

def main():
   
    print("Enter your scores:")
    philosophy_score = float(input("philosophy: "))
    MIL_score = float(input("MIL: "))
    english_score = float(input("English: "))

    scores = [philosophy_score, MIL_score, english_score]

   
    average = compute_average(scores)

    print("Your average score is:", average)

main()
