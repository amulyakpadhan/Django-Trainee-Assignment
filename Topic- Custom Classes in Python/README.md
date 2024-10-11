# Question: 
You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the Rectangle class requires length:int and width:int to be initialized.
2. We can iterate over an instance of the Rectangle class 
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}


# Solution:
Code for this is in the file and below is the description:
The Rectangle class has an __init__ method to initialize the instance with length and width attributes. The __iter__ method is used to define the iteration protocol, which allows us to iterate over the instance.

When we iterate over an instance of the Rectangle class, we yield two dictionaries: one with the length attribute and another with the width attribute. This ensures that we get the desired output format: {'length': <VALUE_OF_LENGTH>} followed by {'width': <VALUE_OF_WIDTH>}.

# Output:
![image](https://github.com/user-attachments/assets/9e41c565-5801-4eb1-87ee-dfacd431cb44)



**Note:** This repository contains a Python file to answer this question as described above. 
