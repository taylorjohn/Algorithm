# Binary Search Recursive

import array as arr

def binary_search(list,key,low,high):
    if(low<=high):
        mid=(low+high)//2
        if(key==list[mid]):
            print("Element is found at",mid,"position.")
            return 1
        elif(key<list[mid]):
            return binary_search(list,key,low,mid-1)
        else:
            return binary_search(list,key,mid+1,high)
    else:
        return 0

size=int(input("Enter the size of list : "))
list=[]

for k in range(0,size):
    list.append(int(input("Enter the element : ")))

print("Elements in list : ")
for k in list:
    print(k,end=' ')
print()
key=int(input("Enter key value : "))

low=0
high=len(list)-1
result=0
result=binary_search(list,key,low,high)
print(result)
if(result==0):
    print("Element is not exists in lists.")s
