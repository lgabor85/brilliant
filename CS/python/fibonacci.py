a = 0   # first term
print(a)
b = 1   # second term
print(b)
# loop runs 18 times to get to 20th term
for i in range(18):
  # complete the code in this loop
  # next term is sum of previous terms
  c = a + b
  print(c)
  # update previous terms
  a = b
  # this needs to happen last
  b = c