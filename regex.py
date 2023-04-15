import sys

sys.setrecursionlimit(10000)


def compare_regex_to_input(regex_pattern, input_string):
    """Compare a single character regex to a single character input string"""
    return regex_pattern == input_string or regex_pattern == '.' or not regex_pattern


def compare_patterns(regex_pattern, input_string):
    """Compare two equal length strings.
    Regex can contain different operators ('?', '*', '+') that control
    repetition of a character within a string"""

    if regex_pattern and regex_pattern[0] == "\\":
        regex_pattern = regex_pattern[1:]
    if not regex_pattern or regex_pattern == '$' and not input_string:
        return True
    elif len(regex_pattern) > 1 and regex_pattern[1] == "?" and input_string:
        return compare_patterns(regex_pattern[2:], input_string) or compare_patterns(
            regex_pattern[0] + regex_pattern[2:], input_string)
    elif len(regex_pattern) > 1 and regex_pattern[1] == "*" and input_string:
        return compare_patterns(regex_pattern[2:], input_string) or compare_patterns(regex_pattern, input_string[1:])
    elif len(regex_pattern) > 1 and regex_pattern[1] == "+" and input_string:
        return compare_patterns(regex_pattern[0] + regex_pattern[2:], input_string) or compare_patterns(regex_pattern,
                                                                                                        input_string[
                                                                                                        1:])
    elif not input_string or not compare_regex_to_input(regex_pattern[0], input_string[0]):
        return False
    else:
        return compare_patterns(regex_pattern[1:], input_string[1:])


def compare_str(regex_pattern, string):
    """Compare two strings using a recursion"""

    if not string and regex_pattern:
        return False
    elif compare_patterns(regex_pattern, string):
        return True
    elif regex_pattern[0] == "^":
        return compare_patterns(regex_pattern[1:], string)
    else:
        return compare_str(regex_pattern, string[1:])


print(compare_str(*input().split('|')))
