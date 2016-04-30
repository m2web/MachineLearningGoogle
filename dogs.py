#The file below was a no go on my Windows 10 system
#apparently matplotlib 1.5 is required.
import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stack=True, color=['r','b'])
plt.show()
#What markes a good feature?
#Ideal features are:
#-Informative
#-Independent
#-Simple