# -*- coding: utf-8 -*-

"""
    flowroutenumbersandmessaging.models.data

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import flowroutenumbersandmessaging.models.attributes

class Data(object):

    """Implementation of the 'Data' model.

    TODO: type model description here.

    Attributes:
        attributes (Attributes): TODO: type description here.
        id (string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attributes" : "attributes",
        "id" : "id",
        "mtype" : "type"
    }

    def __init__(self,
                 attributes=None,
                 id=None,
                 mtype='message'):
        """Constructor for the Data class"""

        # Initialize members of the class
        self.attributes = attributes
        self.id = id
        self.mtype = mtype


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        attributes = flowroutenumbersandmessaging.models.attributes.Attributes.from_dictionary(dictionary.get("attributes")) if dictionary.get("attributes") else None
        id = dictionary.get("id")
        mtype = dictionary.get("type") if dictionary.get("type") else 'message'

        # Return an object of this model
        return cls(attributes,
                   id,
                   mtype)

