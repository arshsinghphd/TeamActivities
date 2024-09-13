# Team Activities: Logic and Control Statements

Well to your first Team Activity (also called  "peer lab"). This is meant to be a time for the team to work through a tutorial like problem, asking questions and seeking better understanding. If you haven't already, make sure to read [The Guide to Quality Team Activities](https://github.com/CS5001-khoury/TeamActivities/blob/main/GuildToGoodTeamsActivities.md)  that was put together by students in past semesters. 

For this Team Activity, you will review two new sets of operators - the conditional operators and the logical operators. You will also learn to use these operators into statements such as if/else statements and general expressions. 

## Grading
Grades for team activities will be based on attendance and notes. You must attend, and as a team you need to generate notes that we can confirm your work. Ideally, you upload the notes as a PDF to the team meeting after you build them out or have a shared document everyone in the team meeting can see (including TAs and the instructor). 

> [!TIP] 
> Good notes become a study guide for you and your team! Make sure they include everything you need to help better understand the weekly material. 

### ⭐ Working in Teams ⭐
When working in teams, remember do not let one person do all the work. Make sure to work together, and ask questions. It is also better if different people program, and you all take turns programming for various team assignments.

### Learning Objectives

* Define and use various conditional operators
* Define an duse various logical operators
* Deal with logic and control flow for programs using if statements
* Have a better understanding of True/False (bool) data types. 


## Conditional Operators

As a quick review of operators, we have covered the 'basic' operators meaning we have looked at `+, -, *, /, %`. We are now adding additional 'conditional' operators, which is something you probably have also done since
elementary school, but not something you have thought about as much. Conditional operators. These operators
look at comparing two values. They are

* `<`
* `>`
* `<=`
* `>=`
* `==`
* `!=`

:memo: Discussion: Reviewing what you learned in the videos, what does each operator do? Is there anything you notice about the operators that isn't normal from what you learned in math years ago (for those who remember!)? Why do you think that it is done in programming this way?

:fire: Task: Now for each each of the conditional operators, come up with example code including what the code would return. For example:

```python
x = 10
y = 5
greater_than = x > y 
print(greater_than) # prints True

less_than = x < y
print(less_than) # prints False
```

> [!NOTE]
> You will see a pattern emerges with the operator whether is a basic
> operator or now the conditional operators:
> `value/variable operator value/variable`. The value can be (and often is) a variable or 
> even a function that returns a value, but the `left operator right` is
> the foundational pattern / grammar.  So breaking down this statement
>
> `less_than = x < y` the pattern shows up twice
> 1. `x < y`  - which when the expression is completed it gives the value of 'False'
> 2. `less_than = False` Since x < y's answer is False, the value gets put in the spot, and the assignment (`=`) operator is applied to the variable `less_than` and the value `False`. 
>
> Note: we realize this is a bit of an abstract way to look at it, and many programmers don't think about that recurring pattern until later. However, knowing the pattern can help you debug as you go through trying to figure out why you may have a syntax error. 

### Conditional Operators and Strings
These operators are not limited to math!  You can apply them to 
other types such as Strings. Try the following in python. 

```python
lone_centurion = "Rory"
girl_who_waited = "Amy"

test = lone_centurion < girl_who_waited
print(test)
```
:memo: What is printed? Why do you think that is? 

:fire: Task: Now, let's make it harder. Take two strings "RORY" and "rory" and apply a couple operators to them. What is printed and why?

## Logical Operators

Now let's expand our operators. For binary conditions of "True" and "False" none of the operators make sense except for `==` and `!=`. As such, we need to have another set of operators to compare binary conditions.

* `and`
* `or`
* `not` 

:memo: Discuss: What does each operator do? Most operators are in the format of `value operator value` is there one in the above three that breaks that rule (and why does it?)

:fire: Task: Complete the following table.

|value|operator|value|result|
| - | :-: | - | - |
| True | and | True |  |
| False | and | False |  |
|  | and | False | False |
| True | or | True |  |
| False | or | False |  |
| True | or |  | True |
| - | not | True | |
| - | not | False | |


> [!NOTE]
> You  may find reference to bitwise operators online. For this
> class we are not covering the bitwise operators, but they are
> ways to do binary math which can help with file security,
> networking, and other types of operations. 


### Logical Operators and Strings?
While logical operators of and/or are meant to work on boolean data
only, you can actually use `not` on strings! However, it doesn't work how 
you think. 


:fire: Task: Try the following code

```python
print(not '')
print(not "aloha")
```

:memo: Deeper Thinking? What happens? Why do you think this is working this way?

## Program Flow
These boolean operations and variables are useful, but the real use is controlling the flow of the program. In order to control the flow of the program, we use various commands the first set you are learning is `if/elif/else`.

The format for the `if/elif/else` statement is as follows:


```python

if bool:
    # do something
elif bool:
    # do something
else:
    # do something
```

> [!WARNING]
> Wait, you just said "bool" but all the examples I saw used condition or logical
> operators. That is true *because* the result of the condition or logical
> operator is a boolean (bool) value! So remember, the operations get processed
> first, and the results is read by the if statement. Why does this matter? 
> Because if doesn't care where the bool comes from, just that it gets one,
> which means for more complex logic, you may have a 
> function returning a bool (example in homework 02). 


Now, let's try writing our own if/else statements. As a group, take the following psuedocode:


1. You are writing a function 'pizza_eater', which takes in the number of slices, the total number of people, and the total number of slices each person wants. It then runs the following conditions
2. If the total slices needed (people * wanted slides) is greater than the total slides, it returns negative -1.
3. If the total slices is bigger than total slides needed it returns the how many slices remain. 

To get you started, here is the function definition:

```python
def pizza_eater(total_slices: int, people: int, slices_wanted: int) -> int:
    """
       Calculates if the pizza has enough slices based on how many
       slices everyone wants per person. 

       Examples:
         >>> pizza_eater(10, 2, 2)
         '6'
         >>> pizza_eater(10, 5, 5)
         '-1'
         >>> pizza_eater(-1, 0, 0)
         '-1'
         >>> pizza_eater(0, 0, 0)
         '0'

       Args:
         total_slices (int): The total slices of pizza
         people (int): the number of people
         slices_wanted (int): the number of wanted slices per person

       Returns:
         (int): -1 if there aren't enough slices, or remaining slices based on need.

    """
```

:fire: TASK:  As a team, discuss the logic and draw a flow chart of the logic. 

:fire: TASK:  As a team, write the code for the problem. 


### Edge Cases
Take a moment to research the term 'edge case', :memo: Discuss what edge case means. Thinking about the tests (Examples) above, do you have every edge case? 

Getting used to edge cases is important! You should always think about them. 
With control flow statements like if/else - every edge case is right on the 'edge' of the condition in addition to extremes. For example, the 0, 0, 0 case is an edge case? Why, because it is checking 0 slices with 0 need. The same would be true with 1, 1, 1, - one slice for one need. (yes, the difference between a `<`, and `<=` operators!)


> [!IMPORTANT]
> Drawing out your flow logic may be tedious now, but it saves you
> time in the future! Right now, practice looking and recognizing the flow
> of programs, and also thinking through your logic. Have a good understanding
> of program flow will help you find errors much easier. 


## Last Task: Work on Coding-Practice
Make sure to work on the [Coding Practice Problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md). Have each member of your group pick a different problem, and you will all work on your problems. Make sure to discuss your solution with the team, and paste your code to your *teams* meeting channel / upload the python .py file! 

At the end of every Team Activity, you will be encouraged to work on coding practice problems as a team. It is important you take this time to talk about solutions, approaches, and make suggestions to each other! You are building a skill needed for technical interviews, and like all new skills it is important to practice.  Some times do the practice problems after the meeting, but then use the chat to comment. Either is fine, but it is important to get feedback and ask questions. 


## Submission
There is no "submission" for the Team Activity. Make sure you have your notes for the meeting (can be a doc in the files section) in your team's meeting channel. The TAs will check the attendance logs and award points based on attendance and completed notes. 