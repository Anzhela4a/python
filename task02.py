original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [original_list[x] for x in range(1, len(original_list)-1) if original_list[x] > original_list[x-1]]

print(f"Исходный список: {original_list}")
print(f"Результативный список: {result_list}")
