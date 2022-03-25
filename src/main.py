from decouple import config
from google.cloud import bigquery

bq_client = bigquery.Client()


def handle_event(event, context):
    """When a cloud storage upload happen run a new aggregation and store the resulting output on a destination table"""
    aggregate = aggregate_data()


def aggregate_data():
    project_name = config('project_name')
    dataset_id = config('dataset_id')
    tablename = config('tablename')
    destination_project = config('destination_project')
    destination_dataset = config('destination_dataset')
    destination_tablename = config('destination_tablename')
    # Configure the query job.
    job_config = bigquery.QueryJobConfig()
    job_config.destination = f"{destination_project}.{destination_dataset}.{destination_tablename}"
    job_config.create_disposition = 'CREATE_IF_NEEDED'
    job_config.write_disposition = 'WRITE_APPEND'

    query = """select count(domain_session_id) as domain_sessionid_count, count(event_id) as event_id_count
                from `{}.{}.{}` group by domain_session_id, event_id 
             """.format(project_name, dataset_id, tablename)
    aggregated = bq_client.query(query, job_config=job_config)
    return aggregated.result()
