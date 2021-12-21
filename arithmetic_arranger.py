import re

def arithmetic_arranger(problems, make = False):
    line_1st = ''
    line_2nd = ''
    line_border = ''
    line_ans = ''
    arranged_problems = ''

    if len(problems) > 5:
      return 'Error: Too many problems.'

    for problem in problems:
      if (re.search('[^\s0-9.+-]', problem)):
        if (re.search('[/]', problem) or re.search('[*]', problem)):
          return "Error: Operator must be '+' or '-'."
        return 'Error: Numbers must only contain digits.'
      
      num_1st = problem.split(' ')[0]
      symbol = problem.split(' ')[1]
      num_2nd = problem.split(' ')[2]

      if len(num_1st)>4 or len(num_2nd)>4:
        return 'Error: Numbers cannot be more than four digits.'

      rst = ''
      if (symbol=='+'):
        rst = int(num_1st) + int(num_2nd)
      elif (symbol=='-'):
        rst = int(num_1st) - int(num_2nd)
      
      width = max(len(num_1st), len(num_2nd)) + 2
      dash_line = ''

      for _ in range(width):
        dash_line += '-'

      if problem != problems[-1]:
        line_1st += str(num_1st).rjust(width) + ' '*4
        line_2nd += symbol + str((num_2nd).rjust(width-1)) + ' '*4
        line_border += dash_line + ' '*4
        line_ans += str(rst).rjust(width) + ' '*4
      else:
        line_1st += str(num_1st).rjust(width)
        line_2nd += symbol + str((num_2nd).rjust(width-1))
        line_border += dash_line
        line_ans += str(rst).rjust(width)
      
    if make:
      arranged_problems = line_1st + '\n' + line_2nd + '\n' + line_border + '\n' + line_ans
      return arranged_problems
    else:
      arranged_problems = line_1st + '\n' + line_2nd + '\n' + line_border
      return arranged_problems

    
