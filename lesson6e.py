# On try and except block: You run some codes/statements and if it is successful they try block will get executed other the executed when there is an anticipated error.


try:
    number = 100 
    answer = number / 0
    print ("The answer is: ",answer)
except Exception as e:
    print("There is an error: ", e)