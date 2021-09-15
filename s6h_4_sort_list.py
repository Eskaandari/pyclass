numbers_list = [5, 1, 4, 3, 8, 2, 10, 9, 7, 6]
def sort(numbers):
    """
    barnamei baraye inke adade dakhele list
    ra bedune estefade az method sort moratab
    konad
    """
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i],numbers[j] = numbers[j],numbers[i]
    return numbers
import inspect
print(inspect.getdoc(sort))
print(sort(numbers_list))
