import azure.functions as func
from function_app import app
from shared_code.helpers import get_azure_client, get_azure_devops_core_client

@app.orchestration_trigger(context_name="context")
def hello_orchestrator(context):
    # Azure DevOps projecten ophalen met managed identity
    core_client = get_azure_devops_core_client(
        organization_url="https://dev.azure.com/dylanprins0604/"
    )

    projects = core_client.get_projects()

    result4 = ""  # Initialize result4 before using it
    for project in projects:
        print(f"Project: {project.name}")
        result4 += f", {project.name}"

    result1 = yield context.call_activity("hello", "Seattle")
    result2 = yield context.call_activity("hello", "Tokyo")
    result3 = yield context.call_activity("hello", "London")

    return [result1, result2, result3, result4]