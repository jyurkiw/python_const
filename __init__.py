from collections import namedtuple


def buildConstantsContainer(name, values):
    """Returns a namedtuple object of type [name] populated by [values].
    Tuple members are values.keys() and the dictionary is used to populate
    the returned tuple.
    """
    Container = namedtuple(name, [key for key in values])
    return Container(**values)
