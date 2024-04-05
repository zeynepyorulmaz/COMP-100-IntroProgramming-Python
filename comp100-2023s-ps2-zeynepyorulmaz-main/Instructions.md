# PS2 - Movie Theater 
### Deadline: April 30 at 23:59
## Introduction

In this problem set, you will use *conditional statements*, *string operations*, and *functions* to help Tom, Jerry, and their group of cartoon friends find cinema seats in a movie theater.

Tom, Jerry, and their friends are going to watch a movie in the only cinema in the city. The cinema has seats arranged in a single row with small corridors separating the slots of seats. Each slot of seats is separated by a corridor and contains the same number of seats.

## String Representation of the Movie Theater 
Cinema seats and corridors will be denoted by different characters: 
- ```'O'``` denotes an empty seat,
- ```'X'``` denotes an occupied seat,
- ```'|'``` denotes a corridor.
- ```'S'``` denotes seats that are allocated for cartoon characters from Tom and Jerry's group.

#### Examples:
- 6 empty seats separated by 2 corridors:
```
 OO|OO|OO
```
- 6 seats, first two and the last two are occupied, separated by a corridor:
```
 XXO|OXX
```
Notice that each seat slot has equal number of seats.


## PART 1: Find Seats for the Group (25 pts)

In Part 1, there are no special conditions when allocating seats for the members of the cartoon group. Whenever an empty seat ```'O'``` is encountered, it should be immediately allocated to one of the group members.



### A) Return YES or NO

For Part A, given the number of cartoon characters in the group and the current seat configuration of the movie theater, you need to check if there is an available seat configuration for the group.

To achieve this, you should implement a function called ```is_there_a_solution(num_of_chars, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```seat_config``` : current seat configuration of the movie theater (string)

If it is possible to find enough seats for the whole group, your function should return 'YES'. Otherwise, it should return 'NO'.



Some examples:
```
>> is_there_a_solution(7, 'OO|OX|OO|XX|XO|OO')
'YES'                                              # The solution is 'SS|SX|SS|XX|XS|SO'
```
```
>> is_there_a_solution(8, 'OOOO|OXXO|XOXO|OOXX')
'YES'                                              # The solution is 'SSSS|SXXS|XSXS|OOXX'
```
```
>> is_there_a_solution(3, 'O|X|X|O')
'NO'                                               # There are no enough available seats.
```

### B) Return Seat Configuration

In Part B, in addition to what you implemented in Part A, you need to return the new seat configuration after allocating seats for the whole group if possible. If it is not possible to allocate enough seats for the entire group, you should return 'X'.

**Important Note:** Starting from the leftmost seat, please allocate the first empty seats and do not skip any empty seats. You will be graded based on these solutions. For example, if you want to allocate seats for 3 characters in the seat configuration ```OO|OX|OX```, you should allocate the first three empty seats from the left. The correct solution would be ```SS|SX|OX```. ```SS|OX|SX``` will not be accepted as an answer.

You should implement a function called ```get_the_solution(num_of_chars, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```seat_config``` : current seat configuration of the movie theater (string)

If it is possible to find enough seats for the entire group, your function should return the solution. To denote that you have allocated a seat for a cartoon character, put 'S' in that index. If there is no solution, just return 'X'.

Some examples:
```
>> get_the_solution(7, 'OO|OX|OO|XX|XO|OO')
'SS|SX|SS|XX|XS|SO'
```
```
>> get_the_solution(8, 'OOOO|OXXO|XOXO|OOXX')
'SSSS|SXXS|XSXS|OOXX'
```
```
>> get_the_solution(3, 'O|X|X|O')
'X'                                               # There are no enough available seats.
```

**Hint**: You can use the ```replace(old, new, count)``` function to replace occurrences of a character in a string. After you have determined that there is a solution, you can replace the 'O's with 'S's using this function.

For further information about the replace() function, you can refer to the Python documentation or other relevant resources such as: https://www.geeksforgeeks.org/python-string-replace/

## PART 2: Find Seats for the Subgroups (75 pts)

In Part 2, the cartoon group wants to sit together but they are aware of the fact that finding adjacent seats for the whole group is a bit challenging. That is why they decide to split into k subgroups, with each subgroup having an equal number of cartoon characters, and they will look for adjacent seats for these subgroups separately. You can assume that they will split equally.

Assuming they are split into k equal subgroups, each subgroup wants to find seats for themselves while considering some conditions. We define two conditions as following:

- **Condition 1**: The members of **each subgroup should sit in the same seat slot** *without separated by a corridor*. Different subgroups can also sit in the same seat slot if there are enough seats available.
  
  Some example cases:
  - There are 6 cartoon characters in the group. They are split into 2-2-2 subgroups, and the seat configuration is ```OOOO|XOXO```.  The solution is ```SSSS|XXSS```.
  - There are 6 cartoon characters in the group. They are split into 2-2-2 subgroups, and the seat configuration is ```OOO|XXO|OOX```. The first subgroup can sit in the first seat slot (the leftmost one), and the second subgroup can sit in the last seat slot (the rightmost one). However, there are no available seats for the last subgroup. In this case, there is no solution.

- **Condition 2**: The members of **each subgroup should sit next to each other** *without separated by a corridor or other people*.
  Some example cases:
  - There are 6 cartoon characters in the group. They are split into 2-2 subgroups, and the seat configuration is ```OOOO|XXOO```. The solution is ```SSSS|XXSS```.
  - There are 6 cartoon characters in the group. They are split into 2-2-2 subgroups, and the seat configuration is ```OOOO|XOXO```. Although two subgroups can sit in the first slot, the third subgroup can't since they cannot sit adjacently in the second seat slot. There is no solution.



### A) Consider Condition 1, Return YES or NO.

For Part A, given the number of cartoon characters in the group, subgroups and seats in one slot and the current seat configuration of the cinema, you will check if you can allocate seats for every subgroup considering **Condition 1**. 

To achieve this, you should implement a function called ```is_there_a_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```num_of_subgroups``` : number of groups that they want to split into (int)
- ```num_seats_in_a_slot``` : number of seats in one slot (int)
- ```seat_config``` : current seat configuration of the cinema (string)

If it is possible to find place for every subgroup, your function should return 'YES'. Otherwise, return 'NO'.

Some examples:
```
>> is_there_a_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO')
'YES'                                                    # The solution is 'SS|OX|SS|XX|XO|SS'
```
```
>> is_there_a_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO')
'YES'                                                    # The solution is 'SSSS|SXXS|XSXS'
```
```
>> is_there_a_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO')
'NO'                                                    # Only one subgroup can sit in the first seat slot
```


### B) Consider Condition 1, Print Seat Configuration.

In Part B, in addition to what you have implemented in Part A, you will return the new seat configuration after you allocated seats for the whole group if possible. If it is not, you will return 'X'.


To achieve this, you should implement a function called ```get_the_solution_C1(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```num_of_subgroups``` : number of groups that they want to split into (int)
- ```num_seats_in_a_slot``` : number of seats in one slot (int)
- ```seat_config``` : current seat configuration of the cinema (string)

  
If it is possible to find place for the whole group, your function should return the solution. To denote that you have allocated a seat for a cartoon character, put 'S' in that index. If there is no solution, just return 'X'.


Some examples:
```
>> get_the_solution_C1(6, 3, 2, 'OO|OX|OO|XX|XO|OO')
'SS|OX|SS|XX|XO|SS'
```
```
>> get_the_solution_C1(8, 4, 4, 'OOOO|OXXO|XOXO')
'SSSS|SXXS|XSXS'
```
```
>> get_the_solution_C1(10, 2, 6, 'OOOOOO|OOOXXO|XXOOXO')
'X'                                                    # Only one subgroup can sit in the first seat slot
```

**Hint**: You can use ```replace(old,new,count)``` function for this part. After you find out how many subgroups can seat in the current seat slot, you can replace ```O```'s with ```S```'s for that seat slot. Think about handling seat slots separately, and concatenate their results.

For further information about ```replace``` function: https://www.geeksforgeeks.org/python-string-replace/


### C) Consider Condition 2, Return YES or NO.

For Part C, given the number of cartoon characters in the group, subgroups and seats in one slot and the current seat configuration of the cinema, you will check if you can allocate seats for every subgroup considering **Condition 2**. 

To achieve this, you should implement a function called ```is_there_a_solution_C2(num_of_chars, num_of_subgroups, num_seats_in_a_slot, seat_config)``` that takes two arguments as follows:
- ```num_of_chars``` : number of characters in the group (int)
- ```num_of_subgroups``` : number of groups that they want to split into (int)
- ```num_seats_in_a_slot``` : number of seats in one slot (int)
- ```seat_config``` : current seat configuration of the cinema (string)

If it is possible to find place for every subgroup, your function should return 'YES'. Otherwise, return 'NO'.

Some examples:
```
>> is_there_a_solution_C2(6, 3, 2, 'OO|OX|OO|XX|XO|OO')
'YES'                                                    # The solution is 'SS|OX|SS|XX|XO|SS'.
```
```
>> is_there_a_solution_C2(8, 4, 4, 'OXXO|OXXO|OOOO')
'NO'                                                    # Only two subgroups can sit in the 3rd seat slot.
```
```
>> is_there_a_solution_C2(12, 3, 6, 'OOOOOO|OOXXO|XOOOOX')
'NO'                                                    # Only two subgroup can sit at the 1st and 3rd slot.
```

