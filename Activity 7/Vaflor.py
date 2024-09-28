def main():
    offices = ["it", "acct", "hr"]
    salaries = {
        "it": {"less_than_10": 5000, "more_than_10": 10000},
        "acct": {"less_than_10": 6000, "more_than_10": 12000},
        "hr": {"less_than_10": 7500, "more_than_10": 15000}
    }

    print("Enter the number of employees:")
    num_employees = int(input())

    for i in range(num_employees):
        print(f"Enter employee {i+1} information:")
        name = input("Name: ")
        years_in_service = int(input("Years in Service: "))
        office = input("Office (it, acct, hr): ").lower()
        while office not in offices:
            print("Invalid office. Please enter it, acct, or hr.")
            office = input("Office (it, acct, hr): ").lower()

        if years_in_service >= 10:
            salary = salaries[office]["more_than_10"]
        else:
            salary = salaries[office]["less_than_10"]

        print(f"Name: {name}, Years in Service: {years_in_service}, Office: {office}, Salary: {salary}")

if __name__ == "__main__":
    main()
