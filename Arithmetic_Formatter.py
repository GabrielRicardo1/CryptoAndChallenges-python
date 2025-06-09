def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        left, operator, right = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_line = []
    second_line = []
    hash_line = []
    result_line = []

    for problem in problems:
        left, operator, right = problem.split()
        width = max(len(left), len(right)) + 2

        first_line.append(left.rjust(width))
        second_line.append(operator + right.rjust(width - 1))
        hash_line.append('-' * width)

        if show_answers:
            answer = str(eval(left + operator + right))
            result_line.append(answer.rjust(width))

    arranged = '    '.join(first_line) + '\n' + \
               '    '.join(second_line) + '\n' + \
               '    '.join(hash_line)

    if show_answers:
        arranged += '\n' + '    '.join(result_line)

    return arranged

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')


