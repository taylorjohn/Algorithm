# Binary Search Iterative

import array as arr
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
flag=0
while(low<=high):
    mid=(low+high)//2
    if(key==list[mid]):
        print("Element found at ",mid,"position.")
        flag=1
        break
    elif(key < list[mid]):
        high=mid-1
    else:
        low=mid+1

if(flag==0):
    print("Element is not exists in lists.")
