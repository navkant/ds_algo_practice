class RepeatIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        self.source.value += 1
        return self.source.value


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeatIterator(self)
