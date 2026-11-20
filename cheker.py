from mukimov import color

def exam_cheking(exam_param=None):
    if exam_param:
        print(color.green('Exam-Param: Haved ✓'))
        if exam_param < 0:
            print(color.red('Error: Exam scores cannot be less than '),color.gold('[ 0 ]'))
            if exam_param > 100:
                print(color.red('Error: Exam scores cannot be greater than '),color.gold('[ 100 ]'))
                return False
            else:
                print(color.green('Success ✓'))
                return True
    else:
        print(color.yellow('Exam-Param: None'))
