
weight = int(input("Enter your current weight (in kg): "))
i_weight = weight
height = int(input("Enter your current height (in cm): "))
age = int(input("Enter your age: "))
gender = str(input("Enter your gender: ")).lower().strip()
daily_calorie_intake = int(input("Enter your daily calorie intake: "))
workout = int(input("Enter your daily workout duration (in mins): "))
daily_calorie_intake -= 5*workout
target_bmi = float(input("Enter your target BMI: "))
target_weight = target_bmi*(height/100)**2
current_bmi = weight/(height/100)**2
month_counter = 0
male_bmr = 10*weight + 6.25*height - 5*(age + int(month_counter/12)) + 5
female_bmr = 10*weight + 6.25*height - 5*(age + int(month_counter/12)) - 161
if gender == "m":
    bmr = male_bmr
else:
    bmr = female_bmr
if daily_calorie_intake >= bmr and target_weight<weight:
    print("It is impossible to reach your goal because your daily calorie intake is greater than your basal metabolism rate ","(",bmr,").",sep="" )
else:
    while weight > target_weight:
        male_bmr = 10 * weight + 6.25 * height - 5 * (age + int(month_counter / 12)) + 5
        female_bmr = 10 * weight + 6.25 * height - 5 * (age + int(month_counter / 12)) - 161

        if gender == "m":
            bmr = male_bmr
        else:
            bmr = female_bmr
        daily_calorie_change = daily_calorie_intake - bmr
        monthly_change = daily_calorie_change * 30
        month_counter += 1
        weight += monthly_change/7700
    daily_calorie_change = daily_calorie_intake - bmr
    monthly_change = daily_calorie_change * 30



    weight -= monthly_change/7700
    month_counter -= 1
    decimal_point = (weight - target_weight)/(((bmr-daily_calorie_intake)*30) / 7700)
    month_counter += decimal_point
    month_counter = round(month_counter, 1)


if month_counter > 0 and target_weight < i_weight:
    print("Number of months:", month_counter)

if target_weight > weight:
    print("Your BMI is already lower than your target BMI.")


