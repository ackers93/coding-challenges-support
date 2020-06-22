#Heres that one we looked at in Python Tutor. 

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
        
deliver_presents_recursively(houses)


Here are some simple iterative problems that have a simple recursive solution. I'll have the solution in the other file. DON'T PEEK.

#REVERSE A STRING

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s))

#Now do the same, but recursion.
def reverse_recursion(s): 
    #your code here.
    
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using recursion) is : ",end="") 
print (reverse(s)) 



#TOTAL CONSONANTS
# Iterative Python3 program to count  
# total number of consonants  
  
# Function to check for consonant 
def isConsonant(ch): 
      
    # To handle lower case 
    ch = ch.upper() 
  
    return not (ch == 'A' or ch == 'E' or 
                ch == 'I' or ch == 'O' or 
                ch == 'U') and ord(ch) >= 65 and ord(ch) <= 90
  
def totalConsonants(string): 
      
    count = 0
      
    for i in range(len(string)): 
  
        # To check is character is Consonant 
        if (isConsonant(string[i])): 
            count += 1
              
    return count 
  
# Driver code 
string = "abc de"
print(totalConsonants(string)) 

