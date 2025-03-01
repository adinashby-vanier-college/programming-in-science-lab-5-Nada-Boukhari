# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    s = ""
    s += "*" * n + "\n"
    for i in range(2, n - 2):
        s += "*" + " " * (n - 2) + "*" + "\n"
    s += "*" * n
    return s

# 1
# 12
# 123
# 1234
def number_pattern(n):
    pattern = ""
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j) + " "
        pattern += line.rstrip() + "\n"
    return pattern

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum = 0
    while n <= 5:
        sum += 1
    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    pattern = ""
    for i in range(1, n + 1):
      spaces = " " * (n - i)
      stars = "*" * (2 * i - 1)
      pattern += spaces + stars + "\n"
    return pattern