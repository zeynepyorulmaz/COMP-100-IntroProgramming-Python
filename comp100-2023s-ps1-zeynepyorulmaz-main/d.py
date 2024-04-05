weight = int(input("Enter your current weight (in kg): "))
height = int(input("Enter your current height (in cm): "))
target_bmi = float(input("Enter your target BMI: "))
target_time = int(input("Enter your target timeframe (in months): "))
target_weight = target_bmi*(height/100)**2
total_calorie_change = (weight-target_weight)*7700
num_guesses = 0
low = 0
high = 4000
guess = (high + low) / 2
num_months = 0
deficit_daily = total_calorie_change/30/target_time
while abs(num_months-target_time) >= 0.01:
    deficit_per_month = guess*30
    num_months = total_calorie_change / deficit_per_month
    if abs(num_months-target_time) >= 0.01:
        if guess < deficit_daily:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2
        num_guesses += 1

    if num_guesses  >= 1000:
        break

if num_guesses >= 1000:
    print("It is not possible to reach your goal within", target_time, "months.")
if num_guesses < 1000:
    print("Ideal calorie deficit:", round(guess))
    print ("Steps in bisection search:", num_guesses)
    fewer = guess*6/10
    sports = guess*4/10/5
    print("I recommend consuming",round(fewer),"fewer calories and exercising for",round(sports),"minutes on a daily basis.")
# guess = daily deficit gibi düşün sonra deficit per month hesapla ondan sonra number of months bul sonra number of monthsa göre condition yaz number of months - timeframe