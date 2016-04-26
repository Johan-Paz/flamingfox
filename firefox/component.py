class MalformedComponent(Exception):
    pass

class ComponentClass(object):

    def __init__(self, name, weight_func=None, resistence_func=None, power_func=None, **kwargs):
        self.name = name
        self.weight_func = weight_func
        self.resistance_func = resistence_func
        self.power_func = power_func
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        parts = {}
        for attr in self.__dict__:
            if attr != 'name':
                parts[attr] = self.__dict__[attr]
        return self.name + ': ' + str(parts)

    def validate(self, component):
        for key in component.__dict__:
            if key in ['name', 'kind']:
                continue
            if key not in self.__dict__:
                raise MalformedComponent('Component attribute %s is not required in this class.' % key)
            if not isinstance(component.__dict__[key], self.__dict__[key]):
                raise MalformedComponent('Attribute %s should be of type %s and it is %s.' %(key, self.__dict__[key], type(component.__dict__[key])))

    def weight(self, instance):
        return self.weight_func(instance) if self.weight_func else 0

class Component(object):

    def __init__(self, name, kind, **kwargs):
        self.name = name
        self.kind = kind
        for key, value in kwargs.items():
            setattr(self, key, value)
        kind.validate(self)
        self.weight = self.kind.weight(self)

    def __str__(self):
        parts = {}
        for attr in self.__dict__:
            if attr not in ['name', 'kind']:
                parts[attr] = self.__dict__[attr]
        return self.kind.name + ' ' + self.name + ': ' + str(parts)

    def get_weight(self):
        return 0