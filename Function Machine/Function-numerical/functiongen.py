# this code will generate the functions that the function generator will use .

#for this task, we need to create the following sets of numerical tasks: (each of them must have at least 4 numbers)

# 1. even numbers from 1-30 (2, 4, 6 ...)
# 2. odd numbers from 1-30 (1, 3, 5 ...)
# 3. multiples of 3 from 1-30 (3, 6, 9 ...)
# 4. multiples of 5 from 1-30 (5, 10, 15 ...)
# 5. prime numbers from 1-30 (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
# 6. Fibonacci numbers from 1-30 (1, 1, 2, 3, 5, 8, 13, 21)
# 7. square numbers from 1-30 (1, 4, 9, 16, 25)
# 8. multiples of 7 from 1-30 (7, 14, 21, 28)
# 9. multiples of 3 from 30-60 (33, 36, 39, 42, 45, 48, 51, 54, 57, 60)
# 10. multiples of 5 from 30-60 (35, 40, 45, 50, 55, 60)
# 11. prime numbers from 30-60 (31, 37, 41, 43, 47, 53, 59)
# 12. multiples of 4 from 30-60 (32, 36, 40, 44, 48, 52, 56, 60)
# 13. multiples of 7 from 30-60 (35, 42, 49, 56)
# 14. multiples of 8 from 30-60 (32, 40, 48, 56)
# 15. multiples of 9 from 30-60 (36, 45, 54)
# 16. even numbers from 30-60 (32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60)
# 17. odd numbers from 30-60 (31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59)
# 19. multiples of 3 from 60-90 (63, 66, 69, 72, 75, 78, 81, 84, 87, 90)
# 20. multiples of 5 from 60-90 (65, 70, 75, 80, 85, 90)
# 21. prime numbers from 60-90 (61, 67, 71, 73, 79, 83, 89)

#then, we are going to label of the previous numbers as IN in their own category. For example, if the ollama system is doing even numbers 1-30, then all even numbers from 1-30 will be labeled as IN, and all other numbers will be labeled as OUT.
#need to create a function that will generate the IN and OUT labels for each of the 21 sets of numbers.
# the function will also vary between tasks so we dont have all of the same, for example having all even numbers and all odd numbers 
# there will be 4-6 tasks, so we should try to vary the types of numbers that are going to be tasked the user.

# the flow should be : 
# 1. generate the numbers for each set. 
# 2. label the numbers as IN or OUT for each set.
# 3. Ollama will ask user to select how many tasks they want to do 
# 3. create a function that will randomly select the amount of tasks from the 21 sets of numbers. (for this code, it will select the amount of tasks the user selects)
# 4. tasks are fed into the ollama and the ollama will give the tasks to the user. the user will get 3 IN numbers at a time. they can request more numbers, in which case the numbers are pulled from the sets. 
# 5. the user can ask if a certain number fits the rule, it will get checked against the set.
# 6. then the system moves on to new tasks until the amount of task the user chose to partake in runs out.


# implementation: first we will create the functin that will generate the numbers for each set.

def generate_number_sets():
    number_sets = {}

    # 1. even numbers from 1-30
    number_sets['even_1_30'] = [x for x in range(1, 31) if x % 2 == 0]

    # 2. odd numbers from 1-30
    number_sets['odd_1_30'] = [x for x in range(1, 31) if x % 2 != 0]

    # 3. multiples of 3 from 1-30
    number_sets['multiples_of_3_1_30'] = [x for x in range(1, 31) if x % 3 == 0]

    # 4. multiples of 5 from 1-30
    number_sets['multiples_of_5_1_30'] = [x for x in range(1, 31) if x % 5 == 0]

    # 5. prime numbers from 1-30
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    number_sets['prime_1_30'] = [x for x in range(1, 31) if is_prime(x)]

    # 6. Fibonacci numbers from 1-30
    fib = [0, 1]
    while fib[-1] < 30:
        fib.append(fib[-1] + fib[-2])
    number_sets['fibonacci_1_30'] = [x for x in fib if x <= 30 and x > 0]

    # 7. square numbers from 1-30
    number_sets['square_numbers_1_30'] = [x**2 for x in range(1, int(30**0.5) + 1)]

    # Continue generating the rest of the sets similarly...

    return number_sets

    # 8. multiples of 7 from 1-30
    number_sets['multiples_of_7_1_30'] = [x for x in range(1, 31) if x % 7 == 0]

    # 9. multiples of 3 from 30-60
    number_sets['multiples_of_3_30_60'] = [x for x in range(30, 61) if x % 3 == 0]

    # 10. multiples of 5 from 30-60
    number_sets['multiples_of_5_30_60'] = [x for x in range(30,61) if x%5==0]

    # 11. prime numbers from 30-60
    number_sets['prime_30_60'] = [x for x in range(30, 61) if is_prime(x)]

    # 12. multiples of 4 from 30-60
    number_sets['multiples_of_4_30_60'] = [x for x in range(30, 61) if x % 4 == 0]

    # 13. multiples of 7 from 30-60
    number_sets['multiples_of_7_30_60'] = [x for x in range(30, 61) if x % 7 == 0]

    # 14. multiples of 8 from 30-60
    number_sets['multiples_of_8_30_60'] = [x for x in range(30, 61) if x % 8 == 0]

    # 15. multiples of 9 from 30-60
    number_sets['multiples_of_9_30_60'] = [x for x in range(30, 61) if x % 9 == 0]

    # 16. even numbers from 30-60
    number_sets['even_30_60'] = [x for x in range(30, 61) if x % 2 == 0]

    # 17. odd numbers from 30-60
    number_sets['odd_30_60'] = [x for x in range(30, 61) if x % 2 != 0]

    # 19. multiples of 3 from 60-90
    number_sets['multiples_of_3_60_90'] = [x for x in range(60, 91) if x % 3 == 0]

    # 20. multiples of 5 from 60-90
    number_sets['multiples_of_5_60_90'] = [x for x in range(60, 91) if x % 5 == 0]

    # 21. prime numbers from 60-90
    number_sets['prime_60_90'] = [x for x in range(60, 91) if is_prime(x)]

# Now that we have generated the number sets, we can create a function to label the numbers as IN or OUT for each set. The IN numbers will be those that belong to the specific set, while the OUT numbers will be all other numbers in the range.

def label_numbers(number_sets):
    labeled_sets = {}
    for key, numbers in number_sets.items():
        labeled_sets[key] = {
            'IN': numbers,
            'OUT': [x for x in range(1, 91) if x not in numbers]
        }
    return labeled_sets

# Now we can create a function that will randomly select the amount of tasks from the 21 sets of numbers based on user input.

def select_tasks(number_sets, num_tasks):
    import random
    selected_tasks = random.sample(list(number_sets.keys()), num_tasks)
    return {task: number_sets[task] for task in selected_tasks}

# now i need to figure out how ollama can communicate with python to pull the tasks
# im gonna do that in a different file

# this file will be just for creating sets, labeling them, randomly generating them. 
# now ill do a function that will randomly select the first 3 numbers the user will get from each set

def get_initial_numbers(labeled_sets, selected_tasks):
    initial_numbers = {}
    for task in selected_tasks:
        initial_numbers[task] = random.sample(labeled_sets[task]['IN'], 3)
    return initial_numbers