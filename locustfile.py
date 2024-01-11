from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    wait_time = between(1, 3)
    host="https://webappimenchihaoui.azurewebsites.net"
    @task
    def numerical_integration(self):
        self.client.get("/numericalintegralservice/0/3.14159")
