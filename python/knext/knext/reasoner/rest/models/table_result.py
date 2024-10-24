# coding: utf-8

"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.common.rest.configuration import Configuration


class TableResult(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total': 'int',
        'header': 'list[str]',
        'rows': 'list[list[str]]'
    }

    attribute_map = {
        'total': 'total',
        'header': 'header',
        'rows': 'rows'
    }

    def __init__(self, total=None, header=None, rows=None, local_vars_configuration=None):  # noqa: E501
        """TableResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._header = None
        self._rows = None
        self.discriminator = None

        self.total = total
        self.header = header
        self.rows = rows

    @property
    def total(self):
        """Gets the total of this TableResult.  # noqa: E501


        :return: The total of this TableResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TableResult.


        :param total: The total of this TableResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def header(self):
        """Gets the header of this TableResult.  # noqa: E501


        :return: The header of this TableResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this TableResult.


        :param header: The header of this TableResult.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and header is None:  # noqa: E501
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header

    @property
    def rows(self):
        """Gets the rows of this TableResult.  # noqa: E501


        :return: The rows of this TableResult.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this TableResult.


        :param rows: The rows of this TableResult.  # noqa: E501
        :type: list[list[str]]
        """
        if self.local_vars_configuration.client_side_validation and rows is None:  # noqa: E501
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TableResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TableResult):
            return True

        return self.to_dict() != other.to_dict()
