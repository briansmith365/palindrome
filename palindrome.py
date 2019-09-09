# reverse slicing function to reverse a string
def reverse(s):
	return s[::-1]

# function to check if palindrome and store in variable rev
def isPalindrome(s):
	rev = reverse(s)

# checks to see if the string is the same forwards and backwards
# with boolean
	if (s == rev):
		return True
	return False

# gets input from user and makes it lower case store in variable s
s = input('Enter string: ').lower()
ans = isPalindrome(s)

# prints the string entered
print(s)
# prints the string entered in reverse
print(reverse(s))

# if statement that prints yes or no based on if ans is
# true or not
if ans == 1:
	print('Yes')
else:
	print('No')