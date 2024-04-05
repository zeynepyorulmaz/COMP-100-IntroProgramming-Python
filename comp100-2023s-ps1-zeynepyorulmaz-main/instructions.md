# PS1 - Getting Healthier
### Deadline: April 9 at 23:00
## Introduction

In this problem set, you will use Python control flow to solve a computational problem by using *Bisection Search*. In total, you will solve **four** different problems. For each part, you should write your code in the corresponding file. For example, for part A, it should be "a.py".

Suppose that you are trying to live a healthier life and be more active. You know that there are many things you can incorporate into your daily life to be a healthier person. In each part of this problem set, we will explore different kinds of mini-problems with the same goal in mind: reaching a target body-mass-index (BMI). 

We provide some example test cases whose results will appear on GitHub actions after you commit your work. You can do multiple commits, only the latest one before the deadline will be graded. Note that **there will be additional test cases** that we will use when grading your solutions, so the points you see when you commit will not be your final grade.

**Disclaimer:** Please keep in mind that this exercise is only intended to practice programming concepts. It's important to approach health and fitness goals in a balanced and healthy way without promoting unhealthy body standards or harmful behaviors. 


## Parts
1. Naive approach
2. Realistic approach
3. Adding sports to your daily routine
4. The ideal way to achieve your BMI goal
---



## PART A. Naive approach (25 pts)

In this part, you will calculate how many months it takes to reach your BMI goal with the given inputs, such as your current weight, current height, gender, age, the BMI value you would like to reach, and a daily calorie intake. 

In this part, we will assume that the basal metabolic rate (BMR) of the individual is fixed, that is, the calories one's body burns at rest won't change over time. In reality, your daily minimum calorie need depends on your current weight, so keeping the same calorie deficit won't result in significant changes over time. But, for this part, we will assume that to be fixed. 

**Throughout the entire PS, assume that each month is 30 days and 1 kg equals 7700 calories.  
For BMI and BMR calculations, use the formulas below.**

```
BMI = weight(kg) / [height(m)]^2
Male BMR = (10 × weight(kg)) + (6.25 × height(cm)) - (5 × age) + 5  
Female BMR = (10 × weight(kg)) + (6.25 × height(cm)) - (5 × age) - 161
```

Write a program that calculates how many months it will take to reach to goal BMI value. Your program should ask the user to enter the following variables. 

* Current weight -> int
* Current height -> int
* Gender -> string
* Age -> int
* Daily calorie intake -> int
* Target BMI -> float

After your calculation, print out the number of months, **rounded to have 1 decimal point**.

### Example Case
```
Enter your current weight (in kg): 100
Enter your current height (in cm): 180
Enter your age: 29
Enter your gender: M
Enter your daily calorie intake: 1600
Enter your target BMI: 25.0
Number of months: 12.7
```

### Edge Cases 

For all parts of the assignment, take care of the edge cases using the strategies described below. 

1 - If the daily calorie intake is greater or equal to the BMR, inform the user that it is not possible to lose weight when there is no calorie deficit. Round the BMR value to have 1 decimal point.

### Example
```
Enter your current weight (in kg): 100
Enter your current height (in cm): 180
Enter your age: 29
Enter your gender: M
Enter your daily calorie intake: 2500
Enter your target BMI: 25.0
It is impossible to reach your goal because your daily calorie intake is greater than your basal metabolism rate (1985.0).
```

2 - If the target weight is already higher than the input weight, inform the user that they've already reached the goal. 

### Example
```
Enter your current weight (in kg): 60
Enter your current height (in cm): 160
Enter your age: 30
Enter your gender: F
Enter your daily calorie intake: 1800
Enter your target BMI: 26.0
Your BMI is already lower than your target BMI.
```


---

## PART B. Realistic approach (25 pts)

In this part, we will take into account the fact that the basal metabolic rate (BMR) of an individual depends on a few factors and it changes over time. Your task is to find the current BMR at each month and continue calculating how many months it would take to reach the BMI goal. Note that we expect the result to be higher than  Part-A because as one loses weight, the daily calorie need (BMR) also decreases. Then, with the same calorie intake, the deficit will become smaller. Also, take into account that every 12 months, the age increases by 1. 

Input and output formats are the same as in Part-A. Do not forget to account for the edge case mentioned before. Notice that even if the daily intake at first is not greater than BMR, over time, it can become so. In that case, print the same output as Part-A. 


### Example Case
```
Enter your current weight (in kg): 100
Enter your current height (in cm): 180
Enter your age: 29
Enter your gender: M
Enter your daily calorie intake: 1600
Enter your target BMI: 25.0
Number of months: 17.2
```

---

## PART C. Adding sports to your daily routine (20 pts)

You are becoming more experienced as time goes by, and after seeing that only adjusting your daily calorie intake is not the ideal approach, you decide to add sports to your daily routine. **We will assume that 1 min of exercise burns 5 calories on average**. Base your solution on your code for Part B, but in addition to the inputs you get, ask for the daily workout time of the user (integer). Include the calories burned in your calculation of the calorie deficit. Output format and edge case treatment are the same. 

### Example Case
```
Enter your current weight (in kg): 100
Enter your current height (in cm): 180
Enter your age: 29
Enter your gender: M
Enter your daily calorie intake: 1600
Enter your daily workout duration (in mins): 40
Enter your target BMI: 25.0
Number of months: 9.9
```

---

## PART D. The ideal way to achieve your BMI goal (30 pts)

In this part, we will explore the bisection search we learned in class. In the first three parts, you explored the effects of the calorie deficit based on BMR and workouts. Now, you need to find how much calorie deficit you need to have to reach the BMI goal within a given time period.

You will write a program that calculates the amount of calorie deficit you need each day to reach your target BMI goal in the given number of months. You **must** use the bisection search for this. Start with the `[0, 4000]` search range. 

Since hitting the exact target BMI might be difficult, stop the search when the difference between your timeframe and the input timeframe is smaller than 0.01. 

Your program should ask the user for the following inputs:   

* Current weight (in kg) -> int
* Current height (in cm) -> int
* Target BMI -> float
* Timeframe (in months) -> int

And your output should be:

* Ideal calorie deficit (rounded to the nearest integer)
* Steps in bisection search
* Suggestion

Note that, in this part, you are calculating the daily calorie deficit needed. Therefore, you don't need to account for varying BMR values or workouts, which were previously used to calculate the calorie deficit. 

However, after you find the ideal calorie deficit value, prompt the user with a suggestion. Suggest the user that 60% of the deficit comes from reducing daily calorie intake and 40% of it comes from a daily workout routine. Apply the percentages based on the rounded deficit value, and print out the values after rounding to the nearest integer. 

### Example Case

```
Enter your current weight (in kg): 100
Enter your current height (in cm): 180
Enter your target BMI: 25.0
Enter your target timeframe (in months): 10
Ideal calorie deficit: 487
Steps in bisection search: 11
I recommend consuming 292 fewer calories and exercising for 39 minutes on a daily basis.
```


In cases where it is not possible to reach the target BMI within given timeframe (i.e. you can not find the result within 1000 search steps), you should notify the user. 

### Example Case
```
Enter your current weight (in kg): 100
Enter your current height (in cm): 180
Enter your target BMI: 20.0
Enter your target timeframe (in months): 2
It is not possible to reach your goal within 2 months.
```
