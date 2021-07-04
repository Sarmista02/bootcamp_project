import hashlib
result = hashlib.md5(b'Sarmista')
# printing the equivalent byte value.
print("What is your name : ", end="")
print(result.digest())