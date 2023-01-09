from prometheus_client.core import GaugeMetricFamily
import prometheus_client as prom
import time
from sonarqube_exporter import get_all_projects_with_metrics

class CustomSonarExporter:

    def __init__(self):
        pass

    def collect(self):
        projects = get_all_projects_with_metrics()

        for project in projects:
            for metric in project.metrics:
                label_list = ['id', 'key', 'name']
                label_values = []
                value_to_set = None

                label_values.append(project.id)
                label_values.append(project.key)
                label_values.append(project.name)
                for metric_value in metric.values:
                    if metric_value[0] == 'value':
                        value_to_set = metric_value[1]
                    else:
                        label_list.append(metric_value[0])
                        label_values.append(metric_value[1])

                gauge = GaugeMetricFamily(
                    name="sonar_{}".format(metric.key),
                    documentation=metric.description,
                    labels=label_list
                )

                gauge.add_metric(
                    labels=label_values,
                    value=value_to_set
                )
                yield gauge

if __name__ == "__main__":
    custom_exporter = CustomSonarExporter()
    prom.REGISTRY.register(custom_exporter)
    prom.start_http_server(9120)

    while True:
        time.sleep(2)