#print hello_USERNAME!
def hello_name(user_name):
    print("hello_" + user_name +"!")
hello_name("USERNAME")

#odd from 1-100
for i in range(1, 101,2):
    print(i)

#find maximum value in list
def max_num_in_list(a_list):
    max_val = a_list[0]
    for i in range (len(a_list)):
        if a_list[i] <= max_val:
            max_val = a_list[i]
            return max_val
lst = [97, 17, 27, 57]
print("Maximum value of this list is: ",max_num_in_list (lst))

#if given year is leap year

    
#numbers in list are consecutive
def is_consecutive(a_list):
    if len(a_list) <2:
        return True
    sorted_list = sorted(a_list)
    for i in range(len(sorted_list) -1):
        if sorted_list[i] != sorted_list[i+1] -1:
            return False
    return True
list1 = [2, 3, 4, 5, 6, 7]
is_consecutive1 = is_consecutive(list1)
print(is_consecutive1)

list2 = [1, 2, 4, 5]
is_consecutive2 = is_consecutive(list2)
print(is_consecutive2)





    

    