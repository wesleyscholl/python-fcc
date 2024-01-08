def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
      return "Error: Too many problems."

  top_line = ""
  bottom_line = ""
  dashed_line = ""
  answer_line = ""

  for problem in problems:
      num1, operator, num2 = problem.split()

      if operator != '+' and operator != '-':
          return "Error: Operator must be '+' or '-'."

      if not (num1.isdigit() and num2.isdigit()):
          return "Error: Numbers must only contain digits."

      if len(num1) > 4 or len(num2) > 4:
          return "Error: Numbers cannot be more than four digits."

      length = max(len(num1), len(num2)) + 2
      top_line += num1.rjust(length) + '    '
      bottom_line += operator + num2.rjust(length - 1) + '    '
      dashed_line += '-' * length + '    '

      if show_answers:
          if operator == '+':
              result = str(int(num1) + int(num2))
          else:
              result = str(int(num1) - int(num2))

          answer_line += result.rjust(length) + '    '

  arranged_problems = top_line.rstrip() + '\n' + bottom_line.rstrip() + '\n' + dashed_line.rstrip()

  if show_answers:
      arranged_problems += '\n' + answer_line.rstrip()

  return arranged_problems
