# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(Httpexamplepart3) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging
from flask import Flask, request
import math
Httpexamplepart3 = func.Blueprint()


@Httpexamplepart3.route(route="Httpexamplepart3, auth_level=func.AuthLevel.ANONYMOUS")
def Httpexamplepart3(req: func.HttpRequest) -> func.HttpResponse:
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