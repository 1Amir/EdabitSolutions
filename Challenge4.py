#Given a list of cities, how many possible paths can be taken.
#Aka, find the factorial of a number
def paths(n):
  factorial = 1
  if int(n)>=1:
    for i in range(1,(n)+1):
      factorial = factorial * 1
