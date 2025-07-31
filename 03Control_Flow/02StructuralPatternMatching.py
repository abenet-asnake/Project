# =============================================
#           STRUCTURAL PATTERN MATCHING IN PYTHON
# Structural pattern matching allows you to match complex data structures against patterns.
# It was introduced in Python 3.10 and provides a more powerful way to handle conditional logic.
# It handle complex data structures through the match-case syntax, 
# which is more versatile than traditional if-elif-else chains.
# =============================================

# 1. Basic Match-Case Syntax
def match_example(value):
    match value:
        case 1:
            return "Matched 1"
        case 2:
            return "Matched 2"
        case _:
            return "No match"
print(match_example(1))  # Output: Matched 1
print(match_example(3))  # Output: No match
# 2. Matching with Patterns
def match_pattern(value):
    match value:
        case [1, 2, 3]:
            return "Matched list [1, 2, 3]"
        case {"key": "value"}:
            return "Matched dictionary with key 'key'"
        case _:
            return "No match"
print(match_pattern([1, 2, 3]))  # Output: Matched list [1, 2, 3]
print(match_pattern({"key": "value"}))  # Output: Matched dictionary with key 'key'
# 3. Matching with Guards
def match_with_guard(value):
    match value:
        case x if x > 10:
            return "Value is greater than 10"
        case x if x < 5:
            return "Value is less than 5"
        case _:
            return "Value is between 5 and 10"
print(match_with_guard(15))  # Output: Value is greater than 10
print(match_with_guard(3))   # Output: Value is less than 5 
print(match_with_guard(7))   # Output: Value is between 5 and 10

