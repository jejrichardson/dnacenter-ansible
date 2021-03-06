#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: global_credential_cli
short_description: Manage GlobalCredentialCli objects of Discovery
description:
- Adds global CLI credential.
- Updates global CLI credentials.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description:
    - An object to send in the Request body.
    - Required for state create.
    type: list
    elements: dict
    suboptions:
      comments:
        description:
        - It is the global credential cli's comments.
        type: str
      credentialType:
        description:
        - It is the global credential cli's credentialType.
        type: str
      description:
        description:
        - It is the global credential cli's description.
        type: str
      enablePassword:
        description:
        - It is the global credential cli's enablePassword.
        type: str
        required: True
      id:
        description:
        - It is the global credential cli's id.
        type: str
      instanceTenantId:
        description:
        - It is the global credential cli's instanceTenantId.
        type: str
      instanceUuid:
        description:
        - It is the global credential cli's instanceUuid.
        type: str
      password:
        description:
        - It is the global credential cli's password.
        type: str
        required: True
      username:
        description:
        - It is the global credential cli's username.
        type: str
        required: True

  comments:
    description:
    - CLICredentialDTO's comments.
    type: str
  credentialType:
    description:
    - CLICredentialDTO's credentialType.
    - Available values are 'GLOBAL' and 'APP'.
    type: str
  description:
    description:
    - CLICredentialDTO's description.
    type: str
  enablePassword:
    description:
    - CLICredentialDTO's enablePassword.
    - Required for state update.
    type: str
  id:
    description:
    - CLICredentialDTO's id.
    type: str
  instanceTenantId:
    description:
    - CLICredentialDTO's instanceTenantId.
    type: str
  instanceUuid:
    description:
    - CLICredentialDTO's instanceUuid.
    type: str
  password:
    description:
    - CLICredentialDTO's password.
    - Required for state update.
    type: str
  username:
    description:
    - CLICredentialDTO's username.
    - Required for state update.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_cli
# Reference by Internet resource
- name: GlobalCredentialCli reference
  description: Complete reference of the GlobalCredentialCli object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialCli reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: create_cli_credentials
  cisco.dnac.global_credential_cli:
    state: create  # required
    payload:  # required
    - enablePassword: SomeValue  # string, required
      password: SomeValue  # string, required
      username: SomeValue  # string, required
      comments: SomeValue  # string
      credentialType: SomeValue  # string
      description: SomeValue  # string
      id: SomeValue  # string
      instanceTenantId: SomeValue  # string
      instanceUuid: SomeValue  # string
  
- name: update_cli_credentials
  cisco.dnac.global_credential_cli:
    state: update  # required
    enablePassword: SomeValue  # string, required
    password: SomeValue  # string, required
    username: SomeValue  # string, required
    comments: SomeValue  # string
    credentialType: SomeValue  # string, valid values: 'GLOBAL', 'APP'.
    description: SomeValue  # string
    id: SomeValue  # string
    instanceTenantId: SomeValue  # string
    instanceUuid: SomeValue  # string
  
"""

RETURN = """
create_cli_credentials:
    description: Adds global CLI credential.
    returned: success
    type: dict
    contains:
    response:
      description: CLICredentialDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the global credential cli's taskId.
          returned: success
          type: dict
        url:
          description: It is the global credential cli's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: CLICredentialDTO's version.
      returned: success
      type: str
      sample: '1.0'

update_cli_credentials:
    description: Updates global CLI credentials.
    returned: changed
    type: dict
    contains:
    response:
      description: CLICredentialDTO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the global credential cli's taskId.
          returned: changed
          type: dict
        url:
          description: It is the global credential cli's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: CLICredentialDTO's version.
      returned: changed
      type: str
      sample: '1.0'

"""
