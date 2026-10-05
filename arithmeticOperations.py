    # 1d Array 
    # Addition 

import numpy as np
x = np.array([2 , 3 ,4 , 5 ])
y = np.array([5 , 6 , 7 , 8])
z = x + y
print(z)


     # 2d Array 

import numpy as np
x = np.array([[2 , 3 ,4 , 5 ], 
              [3 , 5 , 7 , 9]])

y = np.array([[5 , 6 , 7 , 8],
              [4 , 6 , 8 , 10]])

z = x + y
print(z)

  
    # Subtraction

import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 6 ]])

z = x - y
print(z)


import numpy as np
x = np.array([[2 , 3 ,4 , 5 ], 
              [3 , 5 , 7 , 9]])

y = np.array([[5 , 6 , 7 , 8],
              [4 , 6 , 8 , 10]])

z = x - y
print(z)

    # Multiplication

import numpy as np
x = np.array([[2 , 3 ,4 , 5 ], 
              [3 , 5 , 7 , 9]])

y = np.array([[5 , 6 , 7 , 8],
              [4 , 6 , 8 , 10]])

z = x * y
print(z)


    #  Matrix Multiplicaion

import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 3 ]])

z = x @ y
print(z)


    # Division


import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 3 ]])

z =  y / x
print(z)


    # Floor Division


import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 3 ]])

z =  y // x
print(z)


    #  Exponentiation

import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 3 ]])

z =  y ** x
print(z)


    # Modulus

import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 3 ]])

z =  y % x
print(z)


    #   Transpose


import numpy as np
x = np.array([[2 , 3  ], 
              [3 , 5 ]])

y = np.array([[5 , 6 ],
              [4 , 3 ]])

print(y.transpose())







