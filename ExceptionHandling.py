try:
    year = int(input("Enter year of birth"))
    if year <= 2026:
        print("Your age is", 2026-year)
    else:
        print("Year is invalid")
        
except ValueError:
    print("Enter only numbers")
finally:
    print("Code execution succesfull")