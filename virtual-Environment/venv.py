# virtual environment 

# steps

# 1 - pip install virtualenv
# 2 - virtualenv env
# 3 - .\env\Scripts\Activate.ps1
# 4 - deactivate

import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))