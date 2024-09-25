# Prompt the user/employee to enter years of service in each category.
years_in_IT = float(input("Years of service rendered in IT Department: "))
years_in_ACCT = float(input("Years of service rendered in ACCT Department: "))
years_in_HR =float(input("Years of service rendered in HR: "))

# Will check for the amount of bonuses to be given.
if years_in_IT >= 10:
    bonus_IT = 10000
    print ("IT Department Bonus: 10000")
elif years_in_IT < 10 and years_in_IT > 0:
    bonus_IT = 5000
    print ("IT Department Bonus: 5000")
else:
    bonus_IT = 0
    print ("No Bonus in IT!")

if years_in_ACCT >= 10:
    bonus_ACCT = 12000
    print("ACCT Department Bonus: 12000")
elif years_in_ACCT < 10 and years_in_ACCT > 0:
    bonus_ACCT = 6000
    print("ACCT Department Bonus: 6000")
else:
    bonus_ACCT = 0
    print ("No Bonus in ACCT!")

if years_in_HR >= 10:
    bonus_HR = 15000
    print ("HR Department Bonus: 15000")
elif years_in_HR < 10 and years_in_HR > 0:
    bonus_HR = 7500
    print ("HR Department Bonus: 7500")
else:
    bonus_HR = 0
    print ("No Bonus in HR!")

# Computation of all Bonuses receive.
total_bonusses = bonus_IT + bonus_ACCT + bonus_HR
print (f"The total computed bonuses from each department: {total_bonusses}")



#Other way of coding uding  def function.
#Input years of service.
years_in_IT = float(input("Years of service rendered in IT Department: "))
years_in_ACCT = float(input("Years of service rendered in ACCT Department: "))
years_in_HR =float(input("Years of service rendered in HR: "))

#Using def function
def bonus_calculation(years_of_service, department, bonus_above10, bonus_below10):
    if years_of_service >= 10:
        bonus = bonus_above10
        print (f"{department} Department Bonus: {bonus_above10}")
    elif years_of_service > 0:
        bonus = bonus_below10
        print (f"{department} Department Bonus: {bonus_below10}")
    else:
        bonus = 0
        print (f"Sorry No BONUS In {department}!")

    return bonus

# Each department calculation.
bonus_IT = bonus_calculation(years_in_IT, "IT", 10000, 5000)
bonus_ACCT = bonus_calculation(years_in_ACCT, "ACCT", 12000, 6000)
bonus_HR = bonus_calculation(years_in_HR, "HR", 15000, 7500)

# Total bonuses.
total_bonuses = bonus_IT + bonus_ACCT + bonus_HR
print (f"Total of all bonuses in each department: {total_bonuses}")
