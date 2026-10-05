#  1d Array
import numpy as np
array1 = np.array([10 ,20 ,30 ,40 , 50 , 60 , 70 , 80 ,90 ])
print(array1[1:3])
print(array1[1:6:2])
print(array1[-1:-3:-1])
print(array1[::5])
print(array1[::-2])

# 2d Array

import numpy as np
array1 = np.array([[10 ,20 ,30 ],
                   [40 , 50 , 60 ],
                   [70 , 80 ,90 ]])
print(array1[1, ])
print(array1[:,1])
print(array1[1:3])
print(array1[1:6,1:2])
print(array1[1:3, ])
print(array1[:, 1:2])
print(array1[1:3, :1])


# 3d Array

import numpy as np
array1 = np.array([[[10 ,20 ,30 ],
                   [40 , 50 , 60 ],
                   [70 , 80 ,90 ],
                   [36 , 56 , 76]]])
print(array1[0, ])
print(array1[:,1])
print(array1[1:3 , 1:3])
print(array1[1:3 , ])
print(array1[:,1:3 ])
print(array1[1:2 , 1])
print(array1[1:3,:1])
