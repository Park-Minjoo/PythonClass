# |Good part:
# |- The function takes a list of numbers as input and returns the reversed list.
# |
# |Bad part:
# |- The variable name "list" is not a good choice as it is a built-in function in Python. It is better to use a different name for the variable.
# |- The function modifies the original list in place by using the `reverse()` method. This may cause unexpected behavior if the original list is needed later in the program. It is better to create a copy of the list and reverse the copy instead.
def solution(num_list):
    num_list.reverse()
    return num_list


list = [1, 2, 3, 4, 5]
print(solution(list))
