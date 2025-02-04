import azure.functions as func
import azure.durable_functions as df

# Create the app instance
app = df.DFApp()

# Import all function modules to register them with the app
from shared_code.activities import hello
from shared_code.orchestrators import hello_orchestrator
from shared_code.http_triggers import http_start