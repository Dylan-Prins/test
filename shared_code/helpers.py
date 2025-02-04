from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.core.core_client import CoreClient
import os

__all__ = ['get_azure_client', 'get_azure_devops_core_client']

def get_azure_client(subscription_id: str = None):
    """
    Authenticeer met Azure using managed identity en return een ResourceManagementClient.

    Args:
        subscription_id (str, optional): Azure subscription ID. Als None, wordt de subscription ID uit de omgevingsvariabele gebruikt.

    Returns:
        ResourceManagementClient: Een geauthenticeerde Azure client
    """
    if not subscription_id:
        subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        if not subscription_id:
            raise ValueError("Subscription ID moet worden meegegeven of in AZURE_SUBSCRIPTION_ID environment variable staan")

    credential = DefaultAzureCredential()
    return ResourceManagementClient(
        credential=credential,
        subscription_id=subscription_id
    )

def get_azure_devops_core_client(organization_url: str = None):
    """
    Krijg een Azure DevOps Core client met managed identity authenticatie.

    Args:
        organization_url (str, optional): Azure DevOps organization URL. Als None, wordt de URL uit de omgevingsvariabele gebruikt.

    Returns:
        CoreClient: Een Azure DevOps Core client voor project management
    """
    if not organization_url:
        organization_url = os.getenv('AZURE_DEVOPS_ORG_URL')
        if not organization_url:
            raise ValueError("Organization URL moet worden meegegeven of in AZURE_DEVOPS_ORG_URL environment variable staan")

    # Get token using managed identity with the correct scope voor Azure DevOps
    credential = DefaultAzureCredential()
    token = credential.get_token("499b84ac-1321-427f-aa17-267ca6975798")  # Azure DevOps Resource ID

    # Create connection using managed identity token
    connection = Connection(
        base_url=organization_url,
        creds=BasicAuthentication('', token.token)
    )

    return connection.clients.get_core_client()
