#Given an unsorted array, sort it in such a way that the first
#element is the largest value, the second element is the smallest,
#the third element is the second largest element and so on.
#[2, 4, 3, 5, 1] -> [5, 1, 4, 2, 3]
#can you do it without using extra space
#public void sortAlternate(int[] nums){}

#import io
#
#def print_to_string(*args, **kwargs):
#    output = io.StringIO()
#    print(*args, file=output, **kwargs)
#    contents = output.getvalue()
#    output.close()
#    return contents

class BaseList:

  def __init__(self):
    length = int(input('Enter list length:').strip())
    self.intlist = [int(input('Enter element #'+str(i)+':').strip()) for i in range(length)]
    # todo check input

  def __str__(self):
    #return print_to_string(self.intlist)
    return str(self.intlist)

  def get_min_i(self, start_from = 0):
    min = self.intlist[start_from]
    min_i = start_from
    for i, value in enumerate(self.intlist[start_from:], start_from):
        if value < min:
            min_i = i
            min = value
    return min_i

  def get_max_i(self, start_from = 0):
    max = self.intlist[start_from]
    max_i = start_from
    for i, value in enumerate(self.intlist[start_from:], start_from):
        if value > max:
            max_i = i
            max = value
        print(i, value, max_i)
    return max_i

  def swap(self, one_i, another_i):
       # temp = self.intlist[one_i]
       # self.intlist[one_i] = self.intlist[another_i]
       # self.intlist[another_i] = temp
       self.intlist[one_i], self.intlist[another_i] = self.intlist[another_i], self.intlist[one_i]


class AlternS(BaseList):

  def do(self):
    for i, v in enumerate(self.intlist):
        if i % 2 == 0:
            max_i = self.get_max_i(i)
            print(i, v, i % 2, max_i)
            self.swap(i, max_i)
        else:
            min_i = self.get_min_i(i)
            print(i, v, i % 2, min_i)
            self.swap(i, min_i)
        try:
            print(self)
        except Exception as e:
            print(e)

arr = AlternS()
arr.do()

print(arr)
