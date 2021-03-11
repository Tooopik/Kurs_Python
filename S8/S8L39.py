import sys
evenNumbers = [element for element in range(4400) if element % 2 == 0]
evenNumbersGenerator = (element for element in range(4400) if element % 2 == 0)

evenNumbersGenerator2 = (element ** 2 for element in range(101))

# print(evenNumbers)
# print(evenNumbersGenerator)


# for i in evenNumbersGenerator:
#   print(i)

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))

print(sum(evenNumbersGenerator2))
