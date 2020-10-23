""" A simple social network for tracking connections between people"""

class Person:
    """ A person in the social network.
    
    Attributes:
        name (str): the person's name
        connections(set of person): other people in the social network who
            know this person.
    """
    