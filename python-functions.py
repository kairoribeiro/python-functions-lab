
# Ex 1
def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(10))


# # Ex 2

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest
  
def largest(nums):
  nums.sort()
  return nums[-1]

print(largest([4, 5, 3, 7, 8]))


# # Ex 3

def occurances(string, substr):
  stripped_string = string.replace(substr, '')
  return (len(string) - len(stripped_string)) // len(substr)
	
def occurances(string, substr):
  return string.count(substr)

print(occurances("house home horse", "h"))



# # Ex 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(5, 8, -9))