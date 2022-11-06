#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Draw a shape (triangle)
print("      /|")
print("     / |")
print("    /  |")
print("   /   |")
print("  /    |")
print(" /____ |")


# In[3]:


print("Mike\nThomas")


# In[5]:


print("Chakanetsa\" is our sekuru")


# In[3]:


phrase="Rushinga is in Mt Darwin."
print(phrase + " "  "Mt Darwin is in Mashonaland Central.")
print(phrase.index("R"))
print(phrase.upper().islower())
phrase.replace("Mt Darwin", "Mozambique")


# In[3]:


num_var=-5
print(abs(num_var))
print(pow(2,3))
print(2**3)


# In[5]:


print(round(4.2))
print(round(4.7))


# In[7]:


from math import *
print(ceil(3.5))
print(ceil(3.2))


# In[8]:


print(sqrt(4))


# In[5]:


#MadLibs
name=input("Enter your name: ")
district=input("Enter your district: ")
print(name +" " "was born in" +" "+ district+".")


# In[1]:


#Lists
friends_list=["Mike", "Madhara", "Ndikiye", "Martin", "Biggie"]
num_list=[10, 20, 30, 40, 50, 60]
print(num_list.extend(friends_list))


# In[9]:


#If statements
is_male=True
is_tall=True
if is_male or is_tall:
    print("You are a male, or tall or both.")
elif is_male and not (is_tall):
    print("You are a short male")
else:
    print("You are neither male nor tall.")
    


# In[ ]:





# In[11]:


#Finding the maximum beteen 3 numbers
def max_num(num_1, num_2, num_3):
    if num_1>=num_2 and num_1>=num_3:
        return num_1
    elif num_2>=num_1 and num_2>= num_3:
        return num_2
    else:
        return num_3
    


# In[12]:


print(max_num(5,5,2))


# In[24]:


#Building a calculator
num1=float(input("Enter the first number: "))
operator=input("Enter an operator: ")
num2=float(input("Enter the second number: "))
if operator=="+":
    print(num1 +num2)
elif operator =="-":
    print(num2-num1)
elif operator=="/":
    print(num2/num1)
elif operator=="*":
    print(num1 * num2)
else:
    print("You have entered an invalid operator. Try agin using a different operator such as: +,/,x or -.")


# In[11]:


#Month conversion
month_conversion={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
  }

print(month_conversion["Jan"])
print(month_conversion["Nov"])
print(month_conversion["Jul"])
print(month_conversion.get("Dec"))


# In[12]:


#While Loop
i=1
while i<=10:
    print(i)
    i+=1
print("End of this while loop.")


# In[ ]:





# In[17]:


#Secret word guess game
secret_word="giraffe"
guess=""
while guess!=secret_word:
    guess=input("Guess word: ")
print("You have won.")


# In[ ]:





# In[1]:


#For loops
count=0
friends_list=["Mike", "Clifford", "Dzenhu", " Duggie", "Teedzia"]
for friend in friends_list:
    print(friend)
    count=count+1
print(count)
print(len(friends_list))
    


# In[6]:


def powercalc(base, power):
    return base**power

powercalc(10,4)


# In[11]:


#Nested Loops
number_grid=[
  [1,2,3],  
  [4,5,6],
  [7,8,9],
  [0]
  ]
for row in number_grid:
    print(row)
print(number_grid)


# In[8]:


#Try Except for handling errors
try:
    10/0
    number=int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Division by zero error")
except Invalidinput:
    print("You have entered an invalid input, try again using a whole number.")

        


# In[24]:


import docx
my_siblings=open("MT siblings.docx", "a")
print(my_siblings.write("Madhara"))
my_siblings.close()


# In[ ]:





# In[ ]:




