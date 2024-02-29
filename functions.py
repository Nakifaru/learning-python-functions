# Function 1: Area of a rectangle (lenght * width)

    # function areaFn (length, width) {
    #     const areaVar = lenght * width
    #     return areaVar
    # }
    # areaFn(20, 10)

    # function is our keyword in js for python use def
    # areaFn is the name of the function
    # length and width are parameteres
    # 20 and 10 are our arguemnsta during this invocation of this function

def area_fn (length, width):
    area_var = length * width
    return area_var

print (area_fn(20, 6))

# Function 2: finding if a number is even

def even(number):
    # if(number % 2 == 0):
    #     return True
    # else:
    #     return False
    return True if number % 2 == 0 else False
    
print(even(21))

# Function 3: Find the Maximum of Three Numbers

def maximum(num1, num2, num3):
    maximum_num = num1
    if (num1 > num2):
        return maximum_num
    else:
        if(num3 > num2):
            maximum_num = num3
            return maximum_num
        maximum_num = num2
        return maximum_num
    
# Function 4: Find if a number is divisible by any number
    
def divisibility_test(num, tester):
    return 'divisible' if num % tester == 0 else 'not divisible'


# Function 5: Count Vowels In a string

def count_vowels(str):
    total_vowels = 0
    for letter in str:
        if letter == "a" or "e" or "i" or "o" or "u":
            total_vowels += 1
        else:
            print("not a vowel")
    return total_vowels

# Function 6:  Check if a Year is a Leap Year


# Function 7: Determine type of triangle

def triangle_type(side1, side2, side3):
    if side1 == side2 == side2 == side3:
        return "equilateral triangle"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return 'isoceles triangle'
    else:
        return 'scalene triangle'
    

    
