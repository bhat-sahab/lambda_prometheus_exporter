# Prometheus Lambda CPU Metrics Exporter

A Python-based AWS Lambda function that exports CPU metrics in Prometheus format. This exporter collects CPU statistics using a custom collector and exposes them through a Lambda endpoint that can be scraped by Prometheus.

## Features

- Exposes CPU metrics in Prometheus format
- Runs as an AWS Lambda function
- Uses the official `prometheus_client` library
- Handles errors gracefully with proper HTTP status codes
- Compatible with Prometheus scraping configurations

## Prerequisites

- Python 3.x
- AWS Lambda environment
- Required Python packages:
  - `prometheus_client`
  - Custom `reports.node_exporter` module

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd prometheus-lambda-exporter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Deploy to AWS Lambda:
   - Package the code and dependencies
   - Create a Lambda function
   - Configure the function handler as `lambda_handler`

## Usage

### AWS Lambda

The function is designed to be triggered via AWS Lambda. It will return Prometheus-formatted metrics with a `200` status code on success, or a `500` status code with an error message on failure.

### Local Testing

You can run the exporter locally for testing:

```python
python3 main.py
```

### Metric Format

The exporter exposes CPU statistics using the following format:
```
CPU_stats{stat="metric_name"} value
```

### Integration with Prometheus

Add the following job to your Prometheus configuration to scrape metrics from the Lambda function:

```yaml
scrape_configs:
  - job_name: 'lambda_cpu_metrics'
    metrics_path: '/path/to/lambda'
    static_configs:
      - targets: ['your-lambda-url']
```

## Code Structure

- `Veritas` class: Custom collector that implements the Prometheus collector interface
- `collect()` method: Generates CPU metrics using the node_exporter module
- `lambda_handler()`: AWS Lambda entry point that handles HTTP responses

## Error Handling

The exporter includes basic error handling:
- Returns HTTP 200 with metrics on success
- Returns HTTP 500 with error message on failure
