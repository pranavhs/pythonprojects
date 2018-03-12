#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while(x<5):
  #   print(x)
  #   x=x+1

  # define a for loop
  # for x in range(5, 10):
  #   print(x)

  # use a for loop over a collection
  # days=["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  # for i in days:
  #   print(i)
 
  # use the break and continue statements
  # for x in range(5, 10):
  #   if(x==7): break
  #   else: print(x)
  # for x in range(1, 10):
  #   if(x%2==1): continue
  #   print(x)

  #using the enumerate() function to get index 
  days=["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days):
    print(i+1, ",", d)


if __name__ == "__main__":
  main()
