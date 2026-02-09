# Below is the program to store Gross Salary in variable using if Else  ststement of monthly contribution

def calculate_nhif(gross_salary):
    if gross_salary<=5999:
        return 150.00
    elif 6000<=gross_salary<=7999:
        return 300.00
    elif 8000<=gross_salary<=11999:
        return 400.00
    elif 12000<=gross_salary<=14999:
        return 500.00
    elif 15000<=gross_salary<=19999:
        return 600.00
    elif 20000<=gross_salary:
        return 750.00
    elif 25000<=gross_salary:
        return 850.00
    elif 30000<=gross_salary:
        return 1000.00
    elif 50000<=gross_salary:
        return 1500.00
    else:
        return 2000.00
    print("yourmonthly nhifcontribution")