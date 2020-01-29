# (c) Copyright 2018-2019 Hewlett Packard Enterprise Development LP
"""Service request map."""


from enum import Enum

class HttpServiceRequestCode(Enum):
    """Enumerated list of REST operations supported by LCM.

    Note that LCM will support variety of operations and hence it is
    wise to group them appropriately and use the number distinctively.
    As of now, we do see following category:

        1) Service operations (1-99)
        2) Pool operations (100-199)
        3) Cluster lifecycle management operation(s) (200-599)
        4) Cluster consumption operations(s) (600-999)

    It will be good to retain this strategy.
    """

    SERVICE_DOWNLOAD_AGENT_SCRIPT = 1
    SERVICE_LIST_SCRIPT = 2
    ACTION_STATUS = 3

    POOL_NODE_GET_LIST = 100
    POOL_NODE_GET_INFO = 101
    POOL_ADD_NODE = 102
    POOL_AUTHORIZE_NODE = 103
    POOL_REMOVE_NODE = 104
    POOL_NODE_GET_ACTIONS = 105

    CLUSTER_CREATE = 200
    CLUSTER_GET_INFO = 201
    CLUSTER_ACTIVATE = 202
    CLUSTER_SCALE_UP = 203
    CLUSTER_SCALE_DOWN = 204
    CLUSTER_UPGRADE = 205
    CLUSTER_DELETE = 206
    CLUSTER_GET_LIST_INFO = 207
    CLUSTER_GET_ACTIONS = 208
    CLUSTER_GET_CLI = 209

    CLUSTER_DOWNLOAD_KUBECONFIG = 600
    CLUSTER_ADD_PROJECT = 601



service_request_map = {
    HttpServiceRequestCode.SERVICE_DOWNLOAD_AGENT_SCRIPT: {
        "cls": "DownloadAgentScript",
        "module": "service_download_script",
        "description": "Download host agent script request",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.SERVICE_LIST_SCRIPT: {
        "cls": "ListScript",
        "module": "service_list_scripts",
        "description": "List downloadable script(s)",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.POOL_NODE_GET_LIST: {
        "cls": "GetNodeList",
        "module": "pool_node_list",
        "description": "Get node list",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.POOL_NODE_GET_INFO: {
        "cls": "GetNodeInfo",
        "module": "pool_node_get",
        "description": "Get node information",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.POOL_ADD_NODE: {
        "cls": "AddNode",
        "module": "pool_node_add",
        "description": "Add node",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.POOL_AUTHORIZE_NODE: {
        "cls": "AuthorizeNode",
        "module": "pool_node_authorize",
        "description": "Authorize node(node must have been added)",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.POOL_REMOVE_NODE: {
        "cls": "RemoveNode",
        "module": "pool_node_remove",
        "description": "Remove node",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.POOL_NODE_GET_ACTIONS: {
        "cls": "GetNodeActions",
        "module": "pool_node_get_actions",
        "description": "List the set of supported node actions",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_CREATE: {
        "cls": "CreateCluster",
        "module": "cluster_create",
        "description": "Create cluster",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_GET_INFO: {
        "cls": "GetClusterInfo",
        "module": "cluster_get",
        "description": "Get cluster information",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_GET_LIST_INFO: {
        "cls": "GetClusterListInfo",
        "module": "cluster_list_get",
        "description": "Get cluster information",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_ACTIVATE: {
        "cls": "ActivateCluster",
        "module": "cluster_activate",
        "description": "Activate cluster(use after cluster is created)",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_SCALE_UP: {
        "cls": "ScaleUpCluster",
        "module": "cluster_scaleup",
        "description": "Scale up cluster(cluster must be in active state)",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_GET_CLI: {
        "cls": "GetCliCluster",
        "module": "cluster_get_cli",
        "description": "Get a webcli for Cluster",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_SCALE_DOWN: {
        "cls": "ScaleDownCluster",
        "module": "cluster_scaledown",
        "description": "Scale down service request"
                       "(cluster must be in active state)",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_UPGRADE: {
        "cls": "UpgradeCluster",
        "module": "cluster_upgrade",
        "description": "Upgrade cluster(cluster must be in active state)",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_DELETE: {
        "cls": "DeleteCluster",
        "module": "cluster_delete",
        "description": "Delete cluster(cluster must be in active state)",
        "type": "asynchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_GET_ACTIONS: {
        "cls": "GetClusterActions",
        "module": "cluster_get_actions",
        "description": "List the set of supported cluster actions",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_DOWNLOAD_KUBECONFIG: {
        "cls": "DownloadKubeConfig",
        "module": "cluster_download_kubeconfig",
        "description": "Download cluster kubeconfig",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.CLUSTER_ADD_PROJECT: {
        "cls": "AddProject",
        "module": "cluster_add_project",
        "description": "Map cluster to the project",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.ACTION_STATUS: {
        "cls": "ActionStatus",
        "module": "get_action_status",
        "description": "Get request processing status.",
        "type": "synchronous",
        "internal": 0
    },
    HttpServiceRequestCode.BACKGROUND_VERIFY_CLUSTER: {
        "cls": "BackgroundVerifyCluster",
        "module": "background_verify_cluster",
        "description": "Verify cluster composition in background.",
        "type": "synchronous",
        "internal": 1
    },
    HttpServiceRequestCode.BACKGROUND_VERIFY_NODE: {
        "cls": "BackgroundVerifyNode",
        "module": "background_verify_node",
        "description": "Verify node composition in background.",
        "type": "synchronous",
        "internal": 1
    },
}

code_to_enum = {str(k).split('.')[-1]: k for k in service_request_map}
module_map = {v["cls"]: v["module"] for v in service_request_map.values()}
cluster_opcode = [
        {
            "OPCODE": str(request).split('.')[-1],
            "Description":service_request_map[request]["description"],
            "Type": service_request_map[request]["type"]
        }
        for request in service_request_map if "CLUSTER" in str(request)
    ]

node_opcode = [
        {
            "OPCODE": str(request).split('.')[-1],
            "Description":service_request_map[request]["description"],
            "Type": service_request_map[request]["type"]
        }
        for request in service_request_map if "NODE" in str(request)
    ]


if __name__ == "__main__":
    print cluster_opcode