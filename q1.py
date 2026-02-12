import random
def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  """
  color = (shuffle(["red", "green", "yellow",  "blue"]))
  sides = (shuffle(["left" ,"right"]))
  appendage= (shuffle(["hand", "foot"]))

  #YOUR CODE HERE
  return [color[0], sides[0],appendage[0]]
def shuffle(x):
  y = x.copy()
  random.shuffle(y)
  return y
# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  print(spin_twister_spinner())