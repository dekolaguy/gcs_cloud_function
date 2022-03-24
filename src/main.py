import pandas as pd
from google.cloud import bigquery


def handle_event(event, context):
    storage_url = get_file_name(event)
    df = load_with_pandas(storage_url)
    aggregate = aggregate_data(df)
    job = load_to_bq(aggregate)


def load_with_pandas(storage_url):
    df = pd.read_json(storage_url, lines=True)
    return df


def aggregate_data(df: pd.DataFrame):
    aggregated = df.groupby(["domain_sessionid", "event_id"]).count()
    return aggregated


def load_to_bq(df: pd.DataFrame):
    client = bigquery.Client()
    job = client.load_table_from_dataframe(df, 'table_id')
    return job.result()


def get_file_name(event):
    bucket = event["bucket"]
    file = event["name"]
    return f'gs://{bucket}/{file}'