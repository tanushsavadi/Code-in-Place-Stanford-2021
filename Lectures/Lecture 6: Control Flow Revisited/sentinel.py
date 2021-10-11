#Sentinel Loops
#Write a program that prompts the user for numbers until the user types -1, 
#then output the total of the numbers. 
#In this case, -1 is called a sentinel value

def main(): 
   #total is a variable to track the sum of the numbers
   #at the start of the program, we initialize total to be 0
   total = 0 
   
   # we get the first number from the user
   num = int(input("Type a number: "))
   # we have to first get a value for num because the next line of 
   # code checks for num's value 

   # -1 is our sentinel value. Our loop will stop if num == -1 
   while num != -1: 
      # update total to include our new number
      total += num
      num = int(input("Type a number: "))

   print(total) #print out the total once the user enters -1

if __name__ == '__main__':
   main()
