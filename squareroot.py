## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x, guess = 0.0): 
    if x < 0.00000: 
        return None 
    if good_enough(guess, x): 
        return guess 
    
    else: 
        new_guess = improve_guess(guess, x)  
        return sqrt(x, new_guess)

def good_enough(guess, x): 
    if abs(float(guess * guess - x)) < 0.00001: 
        return True
    else: 
        return False 
    

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(x, y):
    return abs(x + y)/2.00000



#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess, x):
    if guess == 0:
        return guess + 0.000001
    else:
	    return(float(guess*1.00000 + x*1.00000/guess)/2.00000)


#### End OF MARKER


