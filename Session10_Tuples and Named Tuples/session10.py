from faker import Faker
from collections import namedtuple
from time import perf_counter
from datetime import date
from dateutil.relativedelta import relativedelta
from collections import Counter
import statistics
from operator import attrgetter
import random
import re
import string
from matplotlib import pyplot as plt
import pandas as pd

# Decorator to Check Performance


def timed(n: 'Number of Iterations') -> 'Decorator':
    '''
    function acts as a decorator factory which takes function repetation count
    as argument.
    returns the decorator
    '''
    def timed_inner(fn: 'Funciton') -> 'closure':
        '''
        function acts as a decorator which runs the given function for
        specified number of times using closure.
        returns the closure
        '''
        def inner(*args: 'arguments', **kwargs: 'keyword arguments') -> 'Result, Time':
            '''
            Calculates the Average Time and Run the Funciton
            '''
            start = perf_counter()
            for _ in range(n):
                result = fn(*args, **kwargs)
            end = perf_counter()

            return result, f'Average Time to Run the Function is: {(end-start)/n :.3f}'

        return inner

    return timed_inner

# Named Tuple Approach
@timed(1)
def nt_approach(n: 'Number of Profiles') -> 'Named Tuple of Statstics':
    '''
    function generates a profile of a person using faker library and
    using namedtuple, calculates the largest blood type, mean_location,
    oldest_person_age and average age using the namedtuple.
    returns namedtuple of the above data.
    '''
    Data = namedtuple('Data', Faker().profile().keys())
    Data.__doc__ = 'Fake personnel profile using faker library'

    nt_list = []
    '''Reason for using List - Using another Named Tuple to stroe 10000 tuples, will be not feasible,
    as NamedTuple allows maximum 255 variables, and all if we need to add one more,
    we need to create an entire new NamedTuple with 10,001 variables, hihgly Ineffecient.'''
    for _ in range(n):
        prof = Faker().profile()
        prof = Data(**prof)
        nt_list.append(prof)

    ages, blood, location = [], [], []
    for tup in nt_list:
        ages.append(relativedelta(date.today(), tup.birthdate).years)
        blood.append(tup.blood_group)
        location.append(tup.current_location)
    oldest_person = max(ages)
    highest_blood = max(Counter(blood).items(), key=lambda item: item[1])
    mean_location = tuple(map(lambda x: sum(x)/len(x), zip(*location)))
    average_age = statistics.mean(ages)
    Stat = namedtuple(
        'Stat', 'oldest_person, highest_blood, mean_location, average_age')
    Stat.__doc__ = '''Statistics of profile data showing the largest present 
    blood type, mean current location, oldest person age and average age using the namedtuple'''
    result = Stat(oldest_person, highest_blood, mean_location, average_age)

    return result

# Dictionary Approach
@timed(1)
def dict_approach(n: 'Number of Profiles') -> 'Dictionary of Statstics':
    '''
    function generates a profile of a person using faker library and
    using dictionary, calculates the largest blood type, mean-current_location,
    oldest_person_age and average age.
    returns dictionary of the above data.
    '''
    dict_list = []
    for _ in range(n):
        prof = Faker().profile()
        dict_list.append(prof)

    ages, blood, location = [], [], []
    for prof in dict_list:
        ages.append(relativedelta(date.today(), prof['birthdate']).years)
        blood.append(prof['blood_group'])
        location.append(prof['current_location'])
    oldest_person = max(ages)
    highest_blood = max(Counter(blood).items(), key=lambda item: item[1])
    mean_location = tuple(map(lambda x: sum(x)/len(x), zip(*location)))
    average_age = mean(ages)

    return {'oldest_person': oldest_person, 'highest_blood': highest_blood, 'mean_location': mean_location, 'average_age': average_age}

# TSAI Stock Exchange


def simulate_stock(days: 'Number of Days to Run Simulation') -> 'Decorator':
    '''
    function acts as a decorator factory which takes number of days to
    simulate the stock exchange.
    returns the decorator
    '''
    def simulate_inner(fn: 'Funciton') -> 'closure':
        '''
        function acts as a decorator which runs the given function for
        specified number of days using closure.
        returns the closure
        '''
        def inner(*args: 'arguments', **kwargs: 'keyword arguments') -> 'History':
            '''
            Simulates the Index Fund for given days, and append to
            corresponding lists
            '''
            open, close, high, low = [], [], [], []
            for _ in range(days):
                index = fn(*args, **kwargs)
                open.append(index.open)
                close.append(index.close)
                high.append(index.high)
                low.append(index.low)
            History = namedtuple('History', 'open high low close')
            history = History(open, high, low, close)

            return history

        return inner

    return simulate_inner


@timed(1)
def stock(count: 'number of comapanies') -> 'tuple':
    '''
    function generates a company stock profile for market value using faker
    library and simulates instantaneous market trend.
    returns list of comapanies stock profiles and contribution to stock_market.
    '''
    exc = []  # Parent Stock Exchange List which will contain all the Companies Named Tuples.
    Stock = namedtuple(
        'Stock', 'index, name, open, high, low, close, contribution')
    Stock.__doc__ = "Company stock profile with current market trend values"
    weights = [random.uniform(0.2, 0.8) for _ in range(100)]
    norm_wts = [x/sum(weights) for x in weights]
    index_l = []  # List to store index and maintain all unique indexes.
    for i in range(count):
        comp_name = Faker().company()
        comp_index = ''.join(i[:3] for i in re.split(
            '[ -]+', comp_name.replace('and', ' ').upper(), 1))[:5]
        while True:
            if comp_index not in index_l:
                index_l.append(comp_index)
                break
            comp_index = comp_index[:4] + random.choice(string.ascii_uppercase)
        open = random.randint(80, 950)
        close = round(open * random.uniform(0.8, 1.2))
        high = round(open * random.uniform(1, 1.6))
        high = close if close > high else high
        low = round(open * random.uniform(0.6, 1))
        low = close if close < low else low
        comp = Stock(comp_index, comp_name, open,
                    high, low, close, norm_wts[i])
        exc.append(comp)

    return exc


df = pd.DataFrame(stock(100)[0], columns=[
    'Index', 'Name', 'Open', 'High', 'Low', "Close", "Contribution to Index"])


@timed(1)
@simulate_stock(10)
def tsai_index(num_comp: 'Number of Companies') -> 'The Index Fund':
    """
    Generates and gives the Index open, high and close of a 
    small stock exchange simulation of listed stocks.
    input: num_comp, number of companies in the exchange
    output: namedtuple('TSAIEX', 'Open High Low Close')
    """
    TSAI = namedtuple('TSAI', 'open high low close')
    TSAI.__doc__ = 'Shows the market trend as whole.'
    open, high, low, close = 0, 0, 0, 0
    companies, comapnies_avg_time = stock(num_comp)
    for i in companies:
        open += round(i.open * i.contribution)
        high += round(i.high * i.contribution)
        low += round(i.low * i.contribution)
        close += round(i.close * i.contribution)
    # Index Checks:
    high = close if close > high else high
    low = close if close < low else low
    tsai_index = TSAI(open, high, low, close)

    return tsai_index
