#Calculating strength of a text by summing all the ASCII values of its characters
def strength (text):

    List=[char for char in text]    # storing each character in a list
    sum=0
    for x in List:
     sum=sum+ord(x)					#Extracting ASCII values using ord() function and then adding it in a loop
    return sum