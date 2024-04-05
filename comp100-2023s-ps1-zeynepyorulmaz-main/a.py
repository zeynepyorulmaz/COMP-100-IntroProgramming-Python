weight = int(input("Enter your current weight (in kg): "))
height = int(input("Enter your current height (in cm): "))
age = int(input("Enter your age: "))
gender = str(input("Enter your gender: ")).lower().strip()
daily_calorie_intake = int(input("Enter your daily calorie intake: "))
target_bmi = float(input("Enter your target BMI: "))
target_weight = target_bmi*(height/100)**2

current_bmi = weight/(height/100)**2
male_bmr = 10*weight + 6.25*height - 5*age + 5
female_bmr = 10*weight + 6.25*height - 5*age - 161



if gender == "m":
    bmr = male_bmr
else:
    bmr = female_bmr

months = 7700*(weight-target_weight)/(bmr-daily_calorie_intake)/30
months = round(months, 1)
if months > 0 and target_weight < weight:
    print("Number of months:", months)

if target_weight > weight:
    print("Your BMI is already lower than your target BMI.")

if daily_calorie_intake >= bmr and target_weight<weight:
    print("It is impossible to reach your goal because your daily calorie intake is greater than your basal metabolism rate ","(",bmr,").",sep="" )
