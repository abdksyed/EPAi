# Assignemt 7 - First Class Functions Part II

## Topics Covered:

* Map, Filter and Zip

* Reducing Functions

* Partial Functions

* The Operator Module

## Link to Class Notebook (along with Notes)

[Class Notebook with extra Notes.](https://github.com/abdksyed/EPAi/blob/master/Session07_First%20Class%20Functions%20Part%20II/notebooks/Session07_Notes.ipynb)

## map()

A map function is a higher order function which take a function and an iterator . It iterates the function over the iterator.

```python
map(func, *iterators)
```
map is lazy operator that is when you initialize a map it will not give direct answer to function but will make a map object only when called it will iterate over and give results. it is also exhaustive i.e. once the iterator is iterated over the map function ends. 


## filter()

A map function is a higher order function which take a function and an iterator. It iterates the function over the iterator and returns Truthy value.

```python
filter(func, iterator)
```
Only one single iterator is accepted. If function is None , it simply returns the elements of Iterable that are truthy.

## zip()

zip is not a higher order function but it zips the elements of multiple iterables .
```python
zip(*iterables)
```
```python
zip([1,2,3],[5,6,7])

gives

(1,5),(2,6),(3,7)
```

## list comprehensions

list comprehension are one liner codes that are used to create lists.  
List comprehension can be used to replace map function and filter function as they are more understandable.

## lambda function

lambda function is used to write one liner function. Usually passed as a function where the input has to change in ever iteration .
```python
lambda x:x+1
```
here x is passed as an input which is written in the left hand side of the : and right hand side we write the function which is to be performed.


## reduce function 

function like max(), min(), avg() are reduce functions. Reduce functions are the once which iterate a function over the input which is given. Like it iterator over a iterator and given the addition of the element within that iterator.

python has it own reduce function in the functools module.


## Partial Function
To reduce the total number of required arguments when calling a fucntion.

In the below example partial function such that 1000/9999 are hardcoded.  
```python
from functools import partial
part_num_plate = partial(variable_num_plate, two_d=47,
                         two_alp='AK', four_d=9999)
```
