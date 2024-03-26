""" CyclicIterator"""


class CyclicIterator:
    """CyclicIterator"""
    def __init__(self, obj):
        self.object = obj
        self.obj = iter(obj)

    def __iter__(self):
        return self

    def __next__(self):

        try:
            return next(self.obj)
        except StopIteration:
            self.obj = iter(self.object)
            return next(self.obj)


for i in CyclicIterator([1, 2, 3]):
    print(i)
