#Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]
            #a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
            #returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]
            #a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
            #returns []

def in_array(list1,list2):
    result=[]
    for i1 in list1:
        for i2 in list2:
            if i1 in i2:
                result.append(i1)
                break 
    return result 


list1=input("Enter names seperated by comma: ").split(",")
list2=input("Enter names seperated by comma: ").split(",")

print(in_array(list1,list2))
