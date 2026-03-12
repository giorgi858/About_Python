import math

def math_example(*args, **kwargs):
    if kwargs['operation'] == 'sum':
        print(sum(args))
        return sum(args)
    if kwargs['operation'] == 'multiply' and kwargs['message'] == 'success':
        print(math.prod(args))
        return  math.prod(args)
        
    else:
        return print('We have an Error')
    
math_example(2,100, operation='multiply', message='success')

