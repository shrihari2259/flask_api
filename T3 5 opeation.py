
#List – Remove duplicates from a list so it will give us an unique values

nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)


# Count word frequency of Dictionary
text = "apple banana apple orange banana apple"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)



# Find common elements of set

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
common = a & b
print(common)



#Tuple – Return multiple values from a function

def stats(nums):
    return min(nums), max(nums), sum(nums)

result = stats([10, 20, 30])
print(result)



##Dict + List =Student marks summary

students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 80, 74]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(name, "Average:", avg)

