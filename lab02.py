# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    hrs = 0 
    mins = 0 
    sec = 0
    hrs = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    sec = total_seconds % 60
    formatted_time = f"{hrs}:{mins:02}:{sec:02}"
    return formatted_time


def admission_price(age):
    if age <5: 
        Price = 0.00
    elif age >=5 and age <=12:
        Price = 8.00
    elif age >=13 and age <=64:
        Price = 15.00
    else:
        Price = 10.00
    return Price 


def sum_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
    return total


def total_of_positives(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total = total + num
    return total


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
