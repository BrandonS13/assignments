

#method 1
import sandwich_functions
sandwich_functions.make_sandwich("Peanut Butter", "Jelly")

#method 2
from sandwich_functions import make_sandwich
make_sandwich("Turkey", "Cheese")

#method 3
from sandwich_functions import make_sandwich as ms
ms("Ham", "Cheese")

#method 4
import sandwich_functions as sf
sf.make_sandwich("Chicken", "Lettuce")

#method 5
from sandwich_functions import *
make_sandwich("Bacon", "Egg", "Cheese")