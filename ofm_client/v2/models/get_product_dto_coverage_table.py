# coding: utf-8

"""
    Open:FactSet Marketplace API

    Headless CMS API used by the Open:FactSet Marketplace.  # noqa: E501

    OpenAPI spec version: v2.1.5
    Contact: openfactset-frontend-engineering@factset.com
    
"""


import pprint
import re  # noqa: F401

import six


class GetProductDtoCoverageTable(object):


    """
    Attributes:
      ofm_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    ofm_types = {
        'columns': 'list[GetProductDtoColumns]',
        'rows': 'list[object]'
    }

    attribute_map = {
        'columns': 'columns',
        'rows': 'rows'
    }

    def __init__(self, columns=None, rows=None):  # noqa: E501
        """GetProductDtoCoverageTable - a model defined in ofm"""  # noqa: E501

        self._columns = None
        self._rows = None
        self.discriminator = None

        if columns is not None:
            self.columns = columns
        if rows is not None:
            self.rows = rows

    @property
    def columns(self):
        """Gets the columns of this GetProductDtoCoverageTable.  # noqa: E501


        :return: The columns of this GetProductDtoCoverageTable.  # noqa: E501
        :rtype: list[GetProductDtoColumns]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this GetProductDtoCoverageTable.


        :param columns: The columns of this GetProductDtoCoverageTable.  # noqa: E501
        :type: list[GetProductDtoColumns]
        """

        self._columns = columns

    @property
    def rows(self):
        """Gets the rows of this GetProductDtoCoverageTable.  # noqa: E501


        :return: The rows of this GetProductDtoCoverageTable.  # noqa: E501
        :rtype: list[object]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this GetProductDtoCoverageTable.


        :param rows: The rows of this GetProductDtoCoverageTable.  # noqa: E501
        :type: list[object]
        """

        self._rows = rows

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.ofm_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetProductDtoCoverageTable, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetProductDtoCoverageTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other