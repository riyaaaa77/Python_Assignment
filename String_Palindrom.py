#!/usr/bin/env python
# coding: utf-8

# In[16]:


def is_palindrome(string):
    # Convert the string to lowercase and remove non-alphabetic characters
    cleaned_string = ''.join(c.lower() for c in string if c.isalpha())

    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[-1::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[ ]:





# In[ ]:




