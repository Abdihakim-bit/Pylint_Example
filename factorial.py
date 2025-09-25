"""This module calculates the sum of factorials from 0 to 49."""
import time
final_list = []
def factorial(num):
    """Return the factorial of a given number."""
    time.sleep(.1)
    result = 1
    for i in range (1,num+1):
        result = result * i
    return result
def sum_factorial():
    """Calculate and print the sum of factorials from 0 to 49."""
    for i in range(50):
        final_list.append(factorial(i))
    result=sum(final_list)
    print(f"Final SUM = {result}")
    return result
if __name__ == "__main__":
    sum_factorial()
