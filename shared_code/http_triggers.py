import azure.functions as func
from function_app import app

@app.route(route="orchestrators/{functionName}", auth_level=func.AuthLevel.ANONYMOUS)
@app.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')
    instance_id = await client.start_new(function_name)
    response = client.create_check_status_response(req, instance_id)
    return response