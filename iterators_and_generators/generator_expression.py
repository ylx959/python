# Generator Expression = Similar to a list comprehension but uses () instead of []
#                                           Creates a generator (iterator) that yields values one at a time
#                                           No need to define a function or use yield
#                                           Less flexible than a gen func and not reusable
#                                           gen object = (expression for value in iterable if condition)

file_path="lord_of_the_rings.txt"

with open(file_path) as file:
    lines=(line.strip() for line in file)
    for line in lines:
        print(line)