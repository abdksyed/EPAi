import time
import math


def time_it(fn, *args, repetitions=1, **kwargs):
    '''The functions calculates the average and total time took
    for running the given funvtion 'fn' for 'repetitions' number of times
    Arguments to be Passed:
    fn: The function whose timing is to be calculated.
    *arg: any extra arguments if required
    repetiotions: Mandatory named argument, the number of times the given
                    function must be performed.
    **kwargs: Any key word arguments which needs to be passed to the function.
    '''
    if fn not in [print, squared_power_list, polygon_area, temp_converter, speed_converter]:
        raise ValueError('Invalid Value Given for fn.')
    start1 = time.perf_counter()
    for _ in range(repetitions):
        res = fn(*args, **kwargs)
    end1 = time.perf_counter()

    return res, (end1 - start1)/repetitions, f'Avg Time: {(end1 - start1)/repetitions} seconds', f'Total Time: {(end1 - start1)} seconds'


def squared_power_list(number, *, start, end):
    sq_list = []
    for i in range(start, end+1):
        sq_list.append(number**i)


def polygon_area(length, *, sides):
    area = {3: (math.sqrt(3)/4)*(length**2), 4: length**2,
            5: 1/4*(math.sqrt(5*(5+2*math.sqrt(5))))*(length**2),
            6: (3*math.sqrt(3)/2)*(length**2)}
    return area.get(sides, 'Invalid Value for Sides, allowed Sides are 3/4/5/6')


def temp_converter(temp, *, temp_given_in):
    if temp_given_in in ['f', 'F', 'Fahrenheit', 'fahrenheit']:
        return (temp - 32)*(5/9)
    elif temp_given_in in ['c', 'C', 'Celsius', 'celsius']:
        return (temp * (9/5)) + 32
    else:
        raise ValueError(
            "Invalid Temperature type. Please provide either 'f' or 'c'")


def speed_converter(speed, *, dist, time):
    km_to = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yard': 1093.61}
    hr_to = {'hr': 1, 'day': 1/24, 'min': 60, 'sec': 3600, 'ms': 3600000}
    if (not km_to.get(dist, 0)) or (not hr_to.get(time, 0)):
        raise ValueError('Invalid Input')
    return speed*(km_to[dist]/hr_to[time])


#print(time_it(polygon_area, repetitions=1, sides=3))
