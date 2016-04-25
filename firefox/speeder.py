class SpeederClass(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Speeder(object):

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.parts = []

    def __str__(self):
        result = '%s (%s):' % (self.name, self.kind.name)

        for part in self.parts:
            result += '\n' + part

        return result