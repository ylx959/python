# recursion = a function that calls itself from within
#                      helps to visualize a complex problem into basic steps
#                      problems can be solved more easily iteratively or recursively
#                      iterative = faster, complex
#                      recursive = slower, simple


# ITERATIVE
def walk_iterative(steps):
    for step in range(1, steps+1):
        print(f"You take step #{step}")

# RECURSIVE
def walk_recursive(steps):
    if steps == 0: #終止條件，沒有它就會無限呼叫
        return
    walk_recursive(steps - 1)
    print(f"You take step #{steps}")

walk_iterative(5)
walk_recursive(5)

# ----- EXAMPLE 2 -----

# ITERATIVE
def factorial_iterative(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

# RECURSIVE
def factorial_recursive(x):
    if x <= 1: #0和1的階乘都是1
        return 1
    else:
        return x * factorial_recursive(x - 1)

print(factorial_iterative(10))
print(factorial_recursive(10))
