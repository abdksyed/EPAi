# Assignemt 2 - Object Mutability and Interning

## Topics Covered:

* Variables & Memory References

* Reference Counting

* Garbage Collection

* Dynamic and Static Typing

* Variable Re-Assignment

* Object Mutability

* Function Arguments and Mutability

* Shared References and Mutability

* Variable Equality

* Everything is an Object

* Python Optimizations - Integer Interning

* Python Optimizations - String Interning

* Python Optimizations - Peephole

## Link to Class Notebook (along with Notes)

**TO-DO**


## Classes and Functions Used:

  
### Something -> Class inherited from **object**

    class Something(object):
	    '''A dummy Class which is used to create Cyclic References'''
	    
	    def __init__(self):
		    super().__init__()
		    self.something_new = None    
		    
	    def __repr__(self):
	    return f'Hey You Found Something'
The class has only one variable 'something_new', which is used later by directly calling using the instance of the class.

### SomethingNew -> Class inherited from **object**

    class  SomethingNew(object):
		'''Anothe Dummy Class which is used to create Cyclic Reference.
			Arguments:
			i -> int -> default= 0. Just a variable.
			Something -> Class Object -> default= None'''
		
		def  __init__(self, i: int = 0, something: Something = None):
			super().__init__()
			self.i = i
			self.something = something
		
		def  __repr__(self):
			return  f'Hey You Again Found Something New'
The class have two inputs, *i* which is an integer and another variable *something*, which is use to assign another class object to this variable.

### add_something -> Function

    def  add_something(collection: List[Something], i: int):
		'''A Function which takes a list and int as input.
		Creates Cyclic References using Two Class Objects and append
		it to the main list.'''
		
		something = Something()
		something.something_new = SomethingNew(i, something)
		collection.append(something)

### reserved_function -> Function

     def  reserved_function():
		'''To be used in future if required'''
		pass
### clear_memory -> Function

    def  clear_memory(collection: List[Something]):

		'''A function which take a list as input and performs clearing
		the list and clearing all cyclic references using garbage collector.'''
		
		collection.clear() #Empties the Entire List
		gc.collect() #Run Garbage Collector and removes all Cyclic References
		
### critical_funciton -> Function

    def  critical_function():

		'''A Function will runs the above *add_something* fucntion for 1024*128(131,072) times
		and create tons of cyclic references loading the memory.
		At last calling clear_memory to clean up the memory.'''
	
		collection = list()
		for i in  range(1, 1024 * 128):
			add_something(collection, i)
		clear_memory(collection)
