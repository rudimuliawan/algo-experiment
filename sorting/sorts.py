class Sort:

    def __init__(self, data):
        self.data = data

    def show(self):
        print(self.data)

    def is_sorted(self):
        for i, val in enumerate(self.data[1:], 1):
            if self.data[i] < self.data[i-1]:
                return False
        
        return True

    def compare(self, data):
        return self.data == data


class SelectionSort(Sort):

    def sort(self):
        length = len(self.data)

        for i in range(length-1):
            min_index = i
            for j in range(i+1, length):
                if self.data[j] < self.data[min_index]:
                    min_index = j

            self.data[min_index], self.data[i] = self.data[i], self.data[min_index]


class InsertionSort(Sort):

    def sort(self):
        length = len(self.data)

        for i in range(1, length):
            while i > 0 and self.data[i] < self.data[i-1]:
                self.data[i], self.data[i-1] = self.data[i-1], self.data[i]
                i = i-1


class ShellSort(Sort):

    def sort(self):
        length = len(self.data)
        gap = length // 2

        while gap > 0:
            for i in range(gap, length):
                temp = self.data[i]
                j = i

                while j >= gap and self.data[j-gap] > temp:
                    self.data[j] = self.data[j-gap]
                    j -= gap

                self.data[j] = temp

            gap = gap // 2


def test_sorting_method(SortingMethod):
    sorting_method = SortingMethod([17, 33, 43, 40, 5, 44, 11, 22, 35, 10])
    sorting_method.sort()
    assert sorting_method.is_sorted()

    sorting_method.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorting_method.sort()
    assert sorting_method.is_sorted()

    sorting_method.data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorting_method.sort()
    assert sorting_method.is_sorted()



def main():
    methods = [SelectionSort, InsertionSort, ShellSort]

    for sorting_method in methods:
        test_sorting_method(sorting_method)
        

if __name__ == "__main__":
    main()