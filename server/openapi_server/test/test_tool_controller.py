# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_tools import PageOfTools  # noqa: E501
from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.test import BaseTestCase


class TestToolController(BaseTestCase):
    """ToolController integration test stubs"""

    def test_create_tool(self):
        """Test case for create_tool

        Add a tool
        """
        tool = {
  "license" : "apache-2.0",
  "authorEmail" : "author@example.com",
  "author" : "Example Author",
  "name" : "awesome-tool",
  "description" : "An awesome tool that returns 42",
  "id" : "id",
  "repository" : "github:awesome-org/awesome-tool",
  "version" : "1.0.0",
  "url" : "https://openapi-generator.tech"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tools',
            method='POST',
            headers=headers,
            data=json.dumps(tool),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_tools(self):
        """Test case for list_tools

        List the tools in the registry
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/tools',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
