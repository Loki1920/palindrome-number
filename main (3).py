# a number is palindrome or not

i = int(input())
rev = 0
x = i
while(i>0):
  rev = (rev*10)+i%10
  i=i//10
if(x==rev):
  print("the number is palindrome")
else:
  print("the number is not palindrome")
