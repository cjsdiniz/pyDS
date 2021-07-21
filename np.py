import numpy as np
print("\n** Array 2 dim **")
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x[1][2])

print("\n** Array 3 dim **")
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x.ndim)  # 2
print(x.size)  # 9
print(x.shape)  # (3, 3)


print("\n** Array Operations **")
x = np.array([2, 1, 3])
print("Initial: ", x)

x = np.append(x, 4)
x = np.delete(x, 0)
x = np.sort(x)

print("Final: ", x)

print("** Cria array **")
x = np.arange(2, 10, 3)
print("Arange: ", x)


print("** Cria array de pares **")
x = np.arange(2, 8, 2)

x = np.append(x, x.size)
print(x)
x = np.sort(x)

print(x[1])

print("** Reshape **")
x = np.arange(1, 7)
print(x)
z = x.reshape(3, 2)
print(z)

print("** Reshape to less **")
x = np.array([[1, 2], [3, 4], [5, 6]])
print(x)
z = x.reshape(6)
print(z)
y = x.flatten()
print(y)

print("** Reshape again **")
x = np.arange(1, 8, 3)
print(x)
z = x.reshape(3, 1)
print(z)
print(z[1][0])

print("** Indexing and Slicing **")

x = np.arange(1, 10)
print(x)
print(x[0:2])
print(x[5:])
print(x[:2])
print(x[-3:])


print("** Conditions **")
print("* #1 *")
x = np.arange(1, 10)
print(x)
print(x[x < 4])

print("* #2 *")
print(x[(x > 5) & (x % 2 == 0)])

print("* #3 *")
y = (x > 5) & (x % 2 == 0)
print(x[y])

print("** Array Operations **")
print("* Simple Operations *")
x = np.arange(1, 10)
print("\nSum:", x.sum())
print("\nMax:", x.max())
print("\nMin:", x.min())
y = x*2
print(y)
y1 = x // 2
print(y1)

print("* Simple Operations *")
x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])

print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))


print("** Exer **")
x = np.arange(3, 9)
print(x)
y = x.reshape(2, 3)
print(y)
print(y[1][1])
