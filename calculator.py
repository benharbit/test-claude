def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def calculate_average(numbers):
    print("Calculating average...")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

if __name__ == "__main__":
    result = divide(10, 0)
    print(result)

    nums = []
    avg = calculate_average(nums)
    print(f"Average: {avg}")
