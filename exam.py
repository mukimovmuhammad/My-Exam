from mukimov import color
from cheker import exam_cheking

ex1 = int(input(color.blue('Enter the score Exam  1: ')))
ex2 = int(input(color.blue('Enter the score Exam  2: ')))
ex3 = int(input(color.blue('Enter the score Exam  3: ')))
ex4 = int(input(color.blue('Enter the score Exam  4: ')))

vp1 = exam_cheking(ex1)
vp2 = exam_cheking(ex2)
vp3 = exam_cheking(ex3)
vp4 = exam_cheking(ex4) 

res = vp1 + vp2 + vp3 + vp4
exmp_result = print(color.lime(f'Result: {res}'))