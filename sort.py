import numpy as np
x = np.array([2, 8, 5])
y =np.sort(x)
print(y)

    # Ascending order

import numpy as np
x = np.array([2, 8, 5])
y =np.argsort(x)
print(y)

    #  Descendimg Order

import numpy as np
x = np.array([2, 8, 5])
y =np.argsort(x)[::-1]
print(y)

import numpy as np
x = np.array([2, 8, 5])
y =np.sort(x)[::-1]
print(y) 


import numpy as np
x = np.array([2, 8, 5])
y =np.sort(x)[::]
print(y) 


import numpy as np 
x = np.array([[3, 1, 2],
              [5, 6, 3],
              [9, 7, 8]])
y = np.sort(x )
print(y)


import numpy as np 
x = np.array([[13, 10, 2],
              [5, 16, 13],
              [19, 17, 8]])
y = np.sort(x ,axis=0 )
print(y)

import numpy as np 
x = np.array([[13, 10, 2],
              [5, 16, 13],
              [19, 17, 8]])
y = np.array([[24, 23, 22],
              [32, 51, 34],
              [19, 17, 25]])
z = np.argsort(y, axis=1)
print(z)  


import numpy as np 
x = np.array([[13, 10, 2],
              [5, 16, 13],
              [19, 17, 8]])
y = np.array([[24, 23, 22],
              [32, 51, 34],
              [19, 17, 25]])
z = np.argsort(y, axis=0)
print(z)


import numpy as np 
x = np.array([[13, 10, 2],
              [5, 16, 13],
              [19, 17, 8]])
x= np.sort(x)
print(x)

