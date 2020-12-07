import connexion

# from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.page_of_tools import PageOfTools  # noqa: E501
from openapi_server.models.tool import Tool  # noqa: E501
# from openapi_server import util


def create_tool(tool):  # noqa: E501
    """Add a tool

    Add a tool # noqa: E501

    :param tool:
    :type tool: dict | bytes

    :rtype: Tool
    """
    if connexion.request.is_json:
        tool = Tool.from_dict(connexion.request.get_json())  # noqa: E501
        print(f"tool: {tool}")
    return 'do some magic!'


def list_tools(limit=None, offset=None):  # noqa: E501
    """List the tools in the registry

    Returns the tools in the registry # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfTools
    """
    return 'do some magic!'
