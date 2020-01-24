def division(list_input,left,right):
    # 以最左边的数(left)为基准
    base = list_input[left]
    while (left < right):
        # 从序列右端开始，向左遍历，直到找到小于base的数
        while ((left < right) and (list_input[right] >= base)):
            right-=1
        # 找到了比base小的元素，将这个元素放到最左边的位置
        list_input[left] = list_input[right]

        # 从序列左端开始，向右遍历，直到找到大于base的数
        while ((left < right) and (list_input[left] < base)):
            left+=1
        # 找到了比base大的元素，将这个元素放到最右边的位置
        list_input[right] = list_input[left]

    # 最后将base放到left位置。此时，left位置的左侧数值应该都比left小；
    # 而left位置的右侧数值应该都比left大。
    list_input[left] = base
    return left;

def quickSort(list_input,left,right):

    # 左下标一定小于右下标，否则就越界了
    if (left < right):
        # 对数组进行分割，取出下次分割的基准标号
        base = division(list_input, left, right)

        print("base = {0}:\t".format(list_input[base]))
        print(list_input, left, right)

        # 对“基准标号“左侧的一组数值进行递归的切割，以至于将这些数值完整的排序
        quickSort(list_input, left, base - 1)

        # 对“基准标号“右侧的一组数值进行递归的切割，以至于将这些数值完整的排序
        quickSort(list_input, base + 1, right)

