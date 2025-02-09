import time

# EXTRA CREDIT
# time efficiency decorator
def timeEfficiencyDecorator(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        print(f'Start Time: {startTime}')

        lst = func(*args, **kwargs)

        endTime = time.time()
        print(f'End Time: {endTime}')
        duration = endTime - startTime
        print(f'Duration: {duration}')
        print(f'Result: [{lst[0]}, {lst[1]}, {lst[2]}, {lst[3]}, {lst[4]}, ...\
, {lst[-5]}, {lst[-4]}, {lst[-3]}, {lst[-2]}, {lst[-1]}]')
    return wrapper