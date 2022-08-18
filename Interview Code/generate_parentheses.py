# @author   Lucas Cardoso de Medeiros
# @since    07/06/2022
# @version  1.0

# GENERATE PARENTHESES ()

# Rules: Given an integer n generate all valid combinations of n pairs of parentheses
# Is valid if: every opening has its closing parenthesis
# And doesn't have a closing without having an unused opening parenthesis before it

# Example:
# n = 3
# output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Solution 1: stack
def is_valid_stack(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        elif par == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            return False
    return len(stack) == 0


# Solution 2: number sum
def is_valid_sum(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1
        elif par == ')':
            if diff == 0:
                return False
            else:
                diff -= 1
        else:
            return False
    return diff == 0


# Solution 3: backtrack tree
# T(n) = 2^k T(n - k) + (2^k - 1)
# T(n) = 2^n * n + 2^n - 1
# T(n) = O(n * 2^n) complexity
def generate(n):
    def rec(n, diff, comb, comb_arr):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                comb_arr.append(''.join(comb))
                print(comb_arr)
        else:
            comb.append('(')
            rec(n - 1, diff + 1, comb, comb_arr)
            comb.pop()
            comb.append(')')
            rec(n - 1, diff + 1, comb, comb_arr)
            comb.pop()

    comb_arr = []
    rec(2 * n, 0, [], comb_arr)


if __name__ == '__main__':
    generate(int(input("Input n: ")))
