"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
    return x
  else:
    ra = foo(x-1)
    rb = foo(x-2)
    return ra + rb

def longest_run(mylist, key):
  longest = 0
  counter = 0
  for x in mylist:
    if x == key:
      counter += 1
    else:
      if counter > longest:
        longest = counter
      counter = 0
  if counter > longest:
    longest = counter
  return longest

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  if len(mylist) == 1:
    if mylist[0]  == key:
      result = Result(0, 0, 1, True)
      return result
    else:
      result = Result(0, 0, 0, False)
      return result

  middle = len(mylist) // 2
  left_result = longest_run_recursive(mylist[:middle], key)
  right_result = longest_run_recursive(mylist[middle:], key)

  totalCount = 0
  leftCount = 0
  rightCount = 0
  for x in range(0, middle):
    if mylist[x] == key:
      leftCount += 1
    else:
      leftCount = 0
  for x in range(middle, len(mylist)):
    if mylist[x] == key:
      rightCount += 1
    else:
      break

  totalCount = leftCount + rightCount

  totalLongest = max(totalCount, left_result.longest_size, right_result.longest_size)

  result = Result(left_result.longest_size, right_result.longest_size, totalLongest, False)
  return result

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
print(to_value(longest_run_recursive([6, 12, 12, 12, 12, 6, 6, 6], 12)))
