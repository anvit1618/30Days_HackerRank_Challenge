num_test_cases = int(input()) #taking number of test cases

for i in range(num_test_cases): #loop from 0 to that num_test_cases
  
    test_string = input() #string input
    
    #assigning even and odd char
    even_char = ''  
    odd_char = '' 
    
    for j in range(len(test_string)): #generating a loop from 0 to the index of the last letter of that particualr string
        if (j % 2) == 0:
            even_char += test_string[j]
            
        else:
            odd_char += test_string[j]
            
    print(f'{even_char} {odd_char}') 
