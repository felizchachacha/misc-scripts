 # Given an array of integers:
  # 1. rearrange the array such that all non-zero members appear on the left of the array (order is not important)
  # 2. return the number of non-zero members

  # e.g. [1,2,0,5,3,0,4,0] => [1,2,5,3,4,0,0,0] and return 5. The non-zero array members can be in any order.



class NonZero:

    def __init__(self, l):
      #self.l, self.members = self.dowhatsneededtodo(l)
      self.l = self.dowhatsneededtodo(l)

    def dowhatsneededtodo(self, l):
      zeros_i = len(l) - 1
      for members, x in enumerate(l):
        if zeros_i == members:
          #return l, members
          return l
        if x == 0:
          while l[zeros_i] == 0 and zeros_i > members:
            zeros_i -= 1
          if zeros_i == 0:
            return l
          l[members], l[zeros_i] = l[zeros_i], l[members]
      return l


#nz = NonZero([1,2,0,5,3,0,4,0])
nz = NonZero([1,2,3,4,0,6,7,8,9])

#print nz.l, nz.members
print(nz.l)
