from itertools import chain, repeat

def quick_sort(l: list):
    entrance = {}
    for i in l:
        if i not in entrance.keys():
            entrance[i] = 1
        else:
            entrance[i] += 1
    return list(chain.from_iterable(repeat(key, n) for key, n in sorted(entrance.items())))


print(quick_sort([3, 1, 4, 2]))
print(quick_sort([5, 4, 3, 2, 1]))
print(quick_sort([3, 1, 3, 2]))
print(quick_sort([0, -2, 3, -1]))
print(quick_sort([5]))
print(quick_sort([]))
