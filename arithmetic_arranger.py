def arithmetic_arranger(problems, *args):
    """
    This is the arithmetic formatter assessment on freeCodeCamp
    https://replit.com/@sliu21/boilerplate-arithmetic-formatter#arithmetic_arranger.py
    """
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []

    for index, value in enumerate(problems):
        operation = value.split(" ")

        if operation[1] not in "-+":
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            isinstance(int(operation[0]), int) and isinstance(int(operation[2]), int)
        except ValueError:
            return "Error: Numbers must only contain digits."

        # Calculate the length of each line
        longest_val = max(len(operation[0]), len(operation[2]))
        width = longest_val + 2
        L1 = f"{operation[0]:>{width}}"
        L2 = operation[1] + f"{operation[2]:>{width - 1}}"
        dash = "-" * width

        try:
            arranged_problems[0] += (" " * 4) + L1
        except:
            arranged_problems.append(L1)

        try:
            arranged_problems[1] += (" " * 4) + L2
        except:
            arranged_problems.append(L2)

        try:
            arranged_problems[2] += (" " * 4) + dash
        except:
            arranged_problems.append(dash)

        if args:
            """
            This is to calculate the answers when args is parsed in as a parameter.
            """
            if operation[1] == "+":
                answer = int(operation[0]) + int(operation[2])
            else:
                answer = int(operation[0]) - int(operation[2])

            answers = f"{answer:>{width}}"

            try:
                arranged_problems[3] += (" " * 4) + answers
            except:
                arranged_problems.append(answers)

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    output = output + f"\n{arranged_problems[3]}" if args else output
    return output
