my_list = [1,2,3,4]

list_ref_at_memory = iter(my_list)
# <list_iterator object at 0x7e505e05b580> reference of the iterable object in the memory

print(list_ref_at_memory)
# initially next is at first element\

# Now we have run it once now it goes to second and so on
print(list_ref_at_memory.__next__())
print(list_ref_at_memory.__next__())
