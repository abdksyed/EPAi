import random
import time
from decimal import Decimal


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

    start1 = time.perf_counter()

    end1 = time.perf_counter()
