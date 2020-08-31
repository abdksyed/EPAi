# Functional parameters and arguments

We have some functions that make use of positional and keyword arguments as described below. We also make use of `*args `and `*kwargs`.

## time_it

It takes a function, the positional and keyword arguments for that function, and gives an average figure of time taken per call to that function over a number of repetitions, which is also specified by the user.

```python
def time_it(fn, *args, repetitions= 1, **kwargs):
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

    return res, f'Avg Time: {(end1 - start1)/repetitions} seconds', f'Total Time: {(end1 - start1)} seconds'
```


## squared_power_list

This function takes a number, as positional argument and two keyword arguments namely, start and end. It returns a list holding the power of that number from start to end. So if we give 2 as the number and start and end as 0 and 3 respectively, it will return [1, 2, 4, 8].

```python
def squared_power_list(number=2, *, start, end):
    sq_list = []
    for i in range(start, end+1):
        sq_list.append(number**i)
```

## polygon_area

This function calculates area for a regular polygon with `sides` ranging from 3 to 6. It takes the length of the side  to calculate the area of the polygon and returns the area in float.

```python
def polygon_area(length=1, *, sides):
    area = {3: (math.sqrt(3)/4)*(length**2), 4: length**2,
            5: 1/4*(math.sqrt(5*(5+2*math.sqrt(5))))*(length**2),
            6: (3*math.sqrt(3)/2)*(length**2)}
    return area.get(sides, 'Invalid Value for Sides, allowed Sides are 3/4/5/6')
```

##  temp_converter

The function takes in temperature as a positional argument and the unit of given argument as a keyword argument and converts it into the other unit of temperature. If the given temperature is in Celsius, the returned is in Fahrenheit an vice versa. Internally, two lambda functions take care of the calculations.

```python
def temp_converter(temp, *, temp_given_in):
    if temp_given_in in ['f', 'F', 'Fahrenheit', 'fahrenheit']:
        return (temp - 32)*(5/9)
    elif temp_given_in in ['c', 'C', 'Celsius', 'celsius']:
        return (temp * (9/5)) + 32
    else:
        return ValueError("Invalid Temperature type. Please provide either 'f' or 'c'")
```


## speed_converter

This function converts the given speed (given in kmph by default) to preferred units of distance and time. It takes input speed in `kmph` and converts into the specified units of speed according to dist and time parameters. `dist` parameter can take values (km/m/ft/yard) and `time` parameter can take values unit (ms/sec/min/hr/day).

```python
def speed_converter(speed, *, dist, time):
    km_to = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yard': 1093.61}
    hr_to = {'hr': 1, 'day': 1/24, 'min': 60, 'sec': 3600, 'ms': 3600000}
    if (not km_to.get(dist, 0)) or (not hr_to.get(time, 0)):
        raise ValueError('Invalid Input')
    return speed*(km_to[dist]/hr_to[time])
```