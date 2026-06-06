def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return duplicates

data = [1, 2, 3, 2, 4, 5, 1, 6, 7, 7, 7]
result = find_duplicates(data)

print(f"Original list: {data}")
print(f"Duplicate numbers found: {result}")
