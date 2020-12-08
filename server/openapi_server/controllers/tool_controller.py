import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError

from openapi_server.config import Config
from openapi_server.dbmodels.tool import Tool as DbTool  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_tools import PageOfTools  # noqa: E501
from openapi_server.models.tool import Tool  # noqa: E501


def create_tool(tool=None):  # noqa: E501
    """Add a tool

    Add a tool # noqa: E501

    :param tool:
    :type tool: dict | bytes

    :rtype: Tool
    """
    res = None
    status = None

    if connexion.request.is_json:
        try:
            tool = Tool.from_dict(connexion.request.get_json())
            db_tool = DbTool(
                name=tool.name
            ).save()
            res = Tool.from_dict(db_tool.to_dict())
            status = 200
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))

    return res, status


def list_tools(limit=None, offset=None):  # noqa: E501
    """List the tools in the registry

    Returns the tools in the registry # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageOfTools
    """
    try:
        db_tools = DbTool.objects().skip(offset).limit(limit)
        tools = [Tool.from_dict(p.to_dict()) for p in db_tools]
        next_ = ""
        if len(tools) == limit:
            next_ = '{api_url}/tools?limit={limit}&offset={offset}'.format(
                api_url=Config().server_api_url,
                limit=limit,
                offset=offset + limit
            )
        res = PageOfTools(
            offset=offset,
            limit=limit,
            links={
                "next": next_
            },
            tools=tools
        )
        status = 200
    except DoesNotExist:
        status = 404
        res = Error("The specified resource was not found", status)
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))

    return res, status
