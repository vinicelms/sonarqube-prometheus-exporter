from flask_restful import Resource
from sonarqube_exporter import get_all_metrics

class Metrics(Resource):
    def get(self):
        return get_all_metrics()