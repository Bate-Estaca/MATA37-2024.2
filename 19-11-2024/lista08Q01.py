def my_sum(_list):
    totalSum = 0;
    for value in _list:
        totalSum += sum(value)
    print(totalSum)

my_sum([[1,2],[3],[4,5,6]])
