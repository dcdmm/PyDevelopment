from pybind11_cmake.func0_base import add, sub

print(add(1, 2))
print(add.__doc__)

print(sub(i=4, j=10))
print(sub.__doc__)