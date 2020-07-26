from collections import namedtuple
import json


def buildConstantsContainer(name, values):
    """Returns a namedtuple object of type [name] populated by [values].
    Tuple members are values.keys() and the dictionary is used to populate
    the returned tuple.
    """
    Container = namedtuple(name, [key for key in values])
    return Container(**values)


def loadConstantsFile(name, path):
    """Returns a namedtuple object of type [name] populated by [values].
    [values] is a json dictionary stored in a file found at [path].
    """
    with open(path, "r") as data:
        return buildConstantsContainer(name, json.loads(data.read()))
