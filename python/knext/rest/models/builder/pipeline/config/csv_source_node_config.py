# coding: utf-8
# Copyright 2023 Ant Group CO., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.rest.configuration import Configuration


class CsvSourceNodeConfig(object):
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
        "type": "str",
        "start_row": "int",
        "url": "str",
        "columns": "list[str]",
    }

    attribute_map = {
        "type": "type",
        "start_row": "startRow",
        "url": "url",
        "columns": "columns",
    }

    def __init__(
        self,
        type="CSV_SOURCE",
        start_row=None,
        url=None,
        columns=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """CsvSourceNodeConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._start_row = None
        self._url = None
        self._columns = None
        self.discriminator = type

        self.type = type
        if start_row is not None:
            self.start_row = start_row
        if url is not None:
            self.url = url
        if columns is not None:
            self.columns = columns

    @property
    def type(self):
        """Gets the type of this CsvSourceNodeConfig.  # noqa: E501


        :return: The type of this CsvSourceNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CsvSourceNodeConfig.


        :param type: The type of this CsvSourceNodeConfig.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "CSV_SOURCE",
            "SPG_TYPE_MAPPING",
            "RELATION_MAPPING",
            "SUBGRAPH_MAPPING",
            "USER_DEFINED_EXTRACT",
            "LLM_BASED_EXTRACT",
            "GRAPH_SINK",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def start_row(self):
        """Gets the start_row of this CsvSourceNodeConfig.  # noqa: E501


        :return: The start_row of this CsvSourceNodeConfig.  # noqa: E501
        :rtype: int
        """
        return self._start_row

    @start_row.setter
    def start_row(self, start_row):
        """Sets the start_row of this CsvSourceNodeConfig.


        :param start_row: The start_row of this CsvSourceNodeConfig.  # noqa: E501
        :type: int
        """

        self._start_row = start_row

    @property
    def url(self):
        """Gets the url of this CsvSourceNodeConfig.  # noqa: E501


        :return: The url of this CsvSourceNodeConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CsvSourceNodeConfig.


        :param url: The url of this CsvSourceNodeConfig.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def columns(self):
        """Gets the columns of this CsvSourceNodeConfig.  # noqa: E501


        :return: The columns of this CsvSourceNodeConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CsvSourceNodeConfig.


        :param columns: The columns of this CsvSourceNodeConfig.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, CsvSourceNodeConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CsvSourceNodeConfig):
            return True

        return self.to_dict() != other.to_dict()
