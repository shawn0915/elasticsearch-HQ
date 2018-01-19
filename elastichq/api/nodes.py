__author__ = 'royrusso'

from flask_restful import Resource

from ..common.status_codes import HTTP_Status
from . import api
from ..common.api_response import APIResponse
from ..service import NodeService
from ..common.exceptions import request_wrapper


class NodesSummary(Resource):
    @request_wrapper
    def get(self, cluster_name, node_ids=None):
        response = NodeService().get_node_summary(cluster_name, node_ids)
        return APIResponse(response, HTTP_Status.OK, None)

class NodesStats(Resource):
    @request_wrapper
    def get(self, cluster_name, node_ids=None):
        response = NodeService().get_node_stats(cluster_name, node_ids)
        return APIResponse(response, HTTP_Status.OK, None)


class NodesInfo(Resource):
    @request_wrapper
    def get(self, cluster_name, node_ids=None):
        response = NodeService().get_node_info(cluster_name, node_ids)
        return APIResponse(response, HTTP_Status.OK, None)


api.add_resource(NodesSummary, '/nodes/<string:cluster_name>/<string:node_ids>/_summary', '/nodes/<string:cluster_name>/_summary', endpoint='nodes_summary', methods=['GET'])
api.add_resource(NodesStats, '/nodes/<string:cluster_name>/<string:node_ids>/_stats', '/nodes/<string:cluster_name>/_stats', endpoint='nodes_stats', methods=['GET'])
api.add_resource(NodesInfo, '/nodes/<string:cluster_name>/<string:node_ids>/_info', '/nodes/<string:cluster_name>/_info', endpoint='nodes_info', methods=['GET'])