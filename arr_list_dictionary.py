arr=[1, 2, 3, 7, 8, 9]
print("Array:", arr)
arr.append(4)
print("Array:", arr)
print("Array size :", len(arr))
arr[3] = 5
print("Array:", arr)
for i in range(len(arr)):
    print(i)      #print each index of the array
arr.pop(2)
print("Array:", arr)
for i in arr:
    print(i)      #print each element of the array


my_list = [1, 2, 3, 3, 9, 12]
print("List:", my_list)
print("Index 5 element:", my_list[5])
my_list.append(4)   
print("List:", my_list)      
my_list[0] = 99                      
print("List:", my_list)
my_list.remove(3)
print("List:", my_list)
my_list.pop(4)
print("List:", my_list)

my_dict = {"a": 1, "b": 2}
print("Dictionary:", my_dict)
my_dict["c"] = 3  
print("Dictionary:", my_dict)                   
my_dict["a"] = 100                 
print("Dictionary:", my_dict)
print("Value of key 'b':", my_dict["b"])
print(my_dict.keys())
print(my_dict.values())
