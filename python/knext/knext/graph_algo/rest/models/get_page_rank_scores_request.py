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


class GetPageRankScoresRequest(object):
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
        'project_id': 'int',
        'target_vertex_type': 'str',
        'start_nodes': 'list[GetPageRankScoresRequestStartNodes]'
    }

    attribute_map = {
        'project_id': 'projectId',
        'target_vertex_type': 'targetVertexType',
        'start_nodes': 'startNodes'
    }

    def __init__(self, project_id=None, target_vertex_type=None, start_nodes=None, local_vars_configuration=None):  # noqa: E501
        """GetPageRankScoresRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._target_vertex_type = None
        self._start_nodes = None
        self.discriminator = None

        self.project_id = project_id
        self.target_vertex_type = target_vertex_type
        self.start_nodes = start_nodes

    @property
    def project_id(self):
        """Gets the project_id of this GetPageRankScoresRequest.  # noqa: E501


        :return: The project_id of this GetPageRankScoresRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GetPageRankScoresRequest.


        :param project_id: The project_id of this GetPageRankScoresRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def target_vertex_type(self):
        """Gets the target_vertex_type of this GetPageRankScoresRequest.  # noqa: E501


        :return: The target_vertex_type of this GetPageRankScoresRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_vertex_type

    @target_vertex_type.setter
    def target_vertex_type(self, target_vertex_type):
        """Sets the target_vertex_type of this GetPageRankScoresRequest.


        :param target_vertex_type: The target_vertex_type of this GetPageRankScoresRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_vertex_type is None:  # noqa: E501
            raise ValueError("Invalid value for `target_vertex_type`, must not be `None`")  # noqa: E501

        self._target_vertex_type = target_vertex_type

    @property
    def start_nodes(self):
        """Gets the start_nodes of this GetPageRankScoresRequest.  # noqa: E501


        :return: The start_nodes of this GetPageRankScoresRequest.  # noqa: E501
        :rtype: list[GetPageRankScoresRequestStartNodes]
        """
        return self._start_nodes

    @start_nodes.setter
    def start_nodes(self, start_nodes):
        """Sets the start_nodes of this GetPageRankScoresRequest.


        :param start_nodes: The start_nodes of this GetPageRankScoresRequest.  # noqa: E501
        :type: list[GetPageRankScoresRequestStartNodes]
        """
        if self.local_vars_configuration.client_side_validation and start_nodes is None:  # noqa: E501
            raise ValueError("Invalid value for `start_nodes`, must not be `None`")  # noqa: E501

        self._start_nodes = start_nodes

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
        if not isinstance(other, GetPageRankScoresRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPageRankScoresRequest):
            return True

        return self.to_dict() != other.to_dict()
