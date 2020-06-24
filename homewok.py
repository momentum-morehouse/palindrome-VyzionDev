
#regular 
def get_input():
  answer = input("Give me something")
  return answer

def check_if(str):
    if str == str[::-1]:
      print("Yes") 
    else: 
      print("No") 
 

def checkiter_isPalindrome(str,): 
    for i in range(0, int(len(str)/2)):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
#iterative  
def iter_ispalindrome(str):
  str = checkiter_isPalindrome(str) 
  if (str): 
    print("Yes") 
  else: 
    print("No") 


def call_every():
 check_if(get_input())
 iter_ispalindrome(get_input(),)


call_every()
  