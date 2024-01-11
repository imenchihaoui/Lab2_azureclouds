import azure.functions as func
import logging
from flask import Flask, request
import math
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


app = Flask(__name__)

def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    result = 0.0

    for i in range(N):
        x_i = lower + i * dx
        result += abs(math.sin(x_i)) * dx

    return result

@app.route('/numericalintegralservice/<lower>/<upper>')
def integrate(lower, upper):
    lower = float(lower)
    upper = float(upper)
    results = {}

    for N in [10, 100, 1000, 10000, 100000, 1000000]:
        results[N] = numerical_integration(lower, upper, N)

    return results

if __name__ == '__main__':
    app.run(debug=True)


@app.route(route="HTTPEXAMPLE", auth_level=func.AuthLevel.ANONYMOUS)
def HTTPEXAMPLE(req: func.HttpRequest) -> func.HttpResponse:
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
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )