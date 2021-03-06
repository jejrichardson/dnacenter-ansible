import json

module_definition = json.loads(
    """{
    "family": "device_onboarding_pnp",
    "name": "pnp_device_claim",
    "operations": {
        "post": [
            "claim_device"
        ]
    },
    "parameters": {
        "claim_device": [
            {
                "name": "configFileUrl",
                "type": "string"
            },
            {
                "name": "configId",
                "type": "string"
            },
            {
                "array_type": "object",
                "name": "deviceClaimList",
                "required": false,
                "schema": [
                    {
                        "array_type": "object",
                        "name": "configList",
                        "required": false,
                        "schema": [
                            {
                                "name": "configId",
                                "required": false,
                                "type": "string"
                            },
                            {
                                "array_type": "object",
                                "name": "configParameters",
                                "required": false,
                                "schema": [
                                    {
                                        "name": "key",
                                        "required": false,
                                        "type": "string"
                                    },
                                    {
                                        "name": "value",
                                        "required": false,
                                        "type": "string"
                                    }
                                ],
                                "type": "array"
                            }
                        ],
                        "type": "array"
                    },
                    {
                        "name": "deviceId",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "licenseLevel",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "licenseType",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "name": "topOfStackSerialNumber",
                        "required": false,
                        "type": "string"
                    }
                ],
                "type": "array"
            },
            {
                "name": "fileServiceId",
                "type": "string"
            },
            {
                "name": "imageId",
                "type": "string"
            },
            {
                "name": "imageUrl",
                "type": "string"
            },
            {
                "name": "populateInventory",
                "type": "boolean"
            },
            {
                "name": "projectId",
                "type": "string"
            },
            {
                "name": "workflowId",
                "type": "string"
            }
        ]
    },
    "responses": {
        "claim_device": {
            "properties": [
                "jsonArrayResponse",
                "jsonResponse",
                "message",
                "statusCode"
            ],
            "type": "object"
        }
    }
}"""
)
