# arr = [-10, 0, 10]
arr = [2, 3, 6, 6, 5]
second_place = 0
for score in arr:
    if score > min(arr) and score < max(arr):
        second_place = score
print(second_place)
print(max([a for a in arr if a != max(arr)]))