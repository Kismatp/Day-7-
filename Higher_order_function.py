# Iterable and iterator
'''
# Iterable 
    # iterable are those objects whose elements can be accesed using loops 
    # Exaples: List ,tuple, set ,dictionary , string 
    # Iterables have methods like __iter() 

# Iterator
    # Iterator are those objects which stores stream of data 
    # Iterator has methods like next__() and Iter__()
    

my_list = [1,2,3,4,5,6]
# my list is iterable because we can access its elements using loops 
for num in my_list:
    print(num)

# my_list as iterator 
my_iterator= iter(my_list)



first_element = next(my_iterator)
print(first_element)

second_elememt= next(my_iterator)
print(second_elememt)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Converting iterator to list 
new_iterator= iter(my_list)
first_element= next (new_iterator)
print(first_element)
new_list= list(new_iterator)
print(new_list)

# map function in python     
    # map is a higher order function which takes two arguments viz,
    # 1. function 
    # 2. iterable
    # and applies the functuon to each element of the iterable
    # and returns an iterator 
    # Usage: we use map function when we have to apply a function to each element of an iterable

#Q. Write a function which returns square of a number and use it to calculate square of numbers in a list 

def square(num):
    return num**2

input_list = [1,2,3,4,5]
output_list= []

for num in input_list:
    print(square(num))
    m=square(num)
    output_list.append(m)

print(output_list)

# Using list comprehension 
output_list_using_comprehension = {square(num) for num in input_list}
print(output_list_using_comprehension)


square_using_map_function= map(square, input_list)
square_using_map_function= list(square_using_map_function)

print(square_using_map_function)

# Usin lambda function inside map 
square_using_map_lambda_function=list(map((lambda num: num**2) , input list)))
print(square_using_map_lambda_function)

'''
#  Filter function 
    # It is similar to map function 
    # The function which we pass to filter function should return boolean value
    # Filter function returns an itreator that contains only those elements for which the function returns true

def is_even (num):
    if num%2==0:
        return True
    else:
        return False
    
input_list = [1,2,3,4,5]
output_list_with_comprehension= [num for num in input_list if is_even(num)]
print(f"Filtered even numbers: {output_list_with_comprehension}")

output_with_filter_func = list(filter(is_even, input_list))
print(f"Filtered even numbers with filter func: {output_with_filter_func}")

output_with_filter_lambda_function= list(filter(lambda num: num%2==0 ,input_list))
print(f"Filtered even numbers with filter lambda func: {output_with_filter_lambda_function}")















