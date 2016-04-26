class SpeederClass(object):

    def __init__(self, name, weight, parts=[]):
        self.name = name
        self.weight = weight
        self.parts = parts

    def __str__(self):
        return self.name + '(%s kg)' % self.weight

class Speeder(object):

    def __init__(self, name, kind, extra=[]):
        self.name = name
        self.kind = kind
        self.parts = extra

    def __str__(self):
        result = '%s (%s):\n Total weight: %skg' % (self.name, self.kind.name, self.kind.weight)

        for part in self.kind.parts:
            result += '\n ' + str(part)

        for part in self.parts:
            result += '\n ' + str(part)

        return result