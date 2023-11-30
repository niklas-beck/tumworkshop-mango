import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="http-trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. But who are you?",
             status_code=200
        )


# Add a new function here
def sum(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python sum function processed a request.')

    a = req.params.get(a)
    b = req.params.get(b)
    if isinstance(a, int) & isinstance(b, int):
        a = req_body.get(a)
        b = req_body.get(b)
        sum = a + b
    else:
        try:
            req_body = req.get_json()
        except ValueError:
            pass

    
    if isinstance(sum, int):
        return func.HttpResponse(f"sum is {sum}")
    else:
        return func.HttpResponse(
             "Not correct number",
             status_code=200
        )

# TODO
