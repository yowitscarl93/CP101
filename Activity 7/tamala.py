def calculate_salary(years, office):
    # Salary conditions based on years of service and office
    salary_conditions = {
        'it': {10: 10000, 0: 5000},
        'acct': {10: 12000, 0: 6000},
        'hr': {10: 15000, 0: 7500}
    }

    # Normalize office input
    office = office.lower()
    
    if office in salary_conditions:
        if years >= 10:
            return salary_conditions[office][10]
        else:
            return salary_conditions[office][0]
    else:
        return None

def main():
    # Get user input
    try:
        years = int(input("Enter the number of years in service: "))
        office = input("Enter the office (it, acct, hr): ")
        
        # Calculate salary
        salary = calculate_salary(years, office)
        
        if salary is not None:
            print(f"The salary for an employee in the {office} office with {years} years of service is: ${salary}")
        else:
            print("Invalid office input. Please enter one of the following: it, acct, hr.")
    except ValueError:
        print("Invalid input. Please enter a valid number for years of service.")

if __name__ == "__main__":
    main()
