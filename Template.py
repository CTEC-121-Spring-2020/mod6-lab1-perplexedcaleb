"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # definite loop example
    for i in range(0, 11, 2):
        print(i)
    print()

    # same behavior but coded as indefinite or while loop
    count = 0
    while(count < 11):
        print(count)
        #count = count + 2
        count += 2

    x = True
    y = True
    if(x):
        if(y):
            print("both true")
        else:
            print("y false")
    else:
        print("x false")
        
    print()
    
main()    