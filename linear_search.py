# Linear Search

import array as arr

size=int(input("Enter size of the array : "))

list = arr.array('i',[ ])

for k in range(0,size):
    list.append(int(input("Enter element : ")))
print(list)
key=int(input("Enter key to search : "))
flag=0
for i in range(0,size):
    if(list[i]==key):
        print("Element found at ",i," index position.")
        flag=1

if(flag==0):
    print("Element not exists in lists.")

# show with lists also.
