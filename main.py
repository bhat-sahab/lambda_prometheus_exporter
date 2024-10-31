#!/usr/bin/python3
from prometheus_client import generate_latest
from prometheus_client.core import GaugeMetricFamily

import reports.node_exporter as node_exporter


class Veritas(object):
    def collect(self):
        """ Collects all gauges and metrics. Then exposes them as
        prometheus values that can be scraped.
        """
        gauge = GaugeMetricFamily("CPU_stats",
                                  "CPU Stats",
                                  labels=['stat'])

        report = node_exporter.generate_report()

        for stat in report:
            gauge.add_metric([stat], report[stat])

        yield gauge


def lambda_handler(event, lambda_context):
    try:
        return {"statusCode": 200, "headers": {"Content-Type": "text/plain"}, "body": generate_latest(Veritas())}
    except Exception as e:
        return {"statusCode": 500, "headers": {"Content-Type": "text/plain"}, "body": f'Error {e}'}


if __name__ == "__main__":
    lambda_handler('demo', 'run')
