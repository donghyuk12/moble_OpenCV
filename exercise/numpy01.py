import numpy as np

# list = [1,2,3]
# array = np.array(list)
# array = np.zeros((2,3))
# array = np.ones(7)
# print(array)

# print(np.arange(10))
# print(np.arange(20,30,2))
# array = np.random.rand(2,3)
# array = np.arange(16)
# print(array)
# print(array.reshape(4,4))
# array = np.arange(16)
# print(array.shape)
# array = np.array([90,20,40,60,70])
# print(array[array >= 50])
# print(np.arange(10).reshape(2,5).transpose()) 
# print(np.arange(10).reshape(2,5).T) 
# print(np.arange(27).reshape(3,3,3))
# print(np.arange(27).reshape(3,3,3).transpose())  

print(np.arange(27).reshape(3,3,3).transpose(1,0,2))