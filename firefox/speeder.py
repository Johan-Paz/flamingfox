class SpeederClass(object):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name + '(%s kg)' % self.weight

class Speeder(object):

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.parts = []

    def __str__(self):
        result = '%s (%s):\n Total weight: %skg' % (self.name, self.kind.name, self.kind.weight)

        for part in self.parts:
            result += '\n' + part

        return result