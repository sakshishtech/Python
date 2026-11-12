try:
    num = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", num)

finally:
    print("Execution completed")

# - try – code that might fail.
# - except – handles the error.
# - else – executes if no exception occurred.
# - finally – executes whether an exception occurred or not.
