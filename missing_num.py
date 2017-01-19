class MissingNumber():

    def __init_():
        super(MissingNumber, self).__init__()

    def find_missing(arr1, arr2):

      if len(arr1) == 0 and len(arr2) == 0:
        print len(arr1)
        return 0
      else:
        if len(arr1) > len(arr2):
          for item in arr1:
            if item not in arr2:
              return item

        else:
          for item in arr2:
            if item not in arr1:
              return item


    print find_missing([1,3,4],[1,2,3,4])
