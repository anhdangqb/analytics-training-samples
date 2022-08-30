"""Utils functions for the assignment of Biquery-notebooks

The util functions will be imported to use in notebook
Version: 2022-08-29
"""

from google.cloud import bigquery
import pandas as pd


def bq_to_dataframe(bq_client: bigquery.Client, sql_script: str) -> pd.DataFrame:
    """
    Executes a SQL script and returns a pandas dataframe
    Args:
        bq_client: BigQuery client
        sql_script: SQL script to be executed
    Returns:
        pandas dataframe
    """
    query_job = bq_client.query(sql_script)
    return query_job.to_dataframe()


def bq_explore_schema(bq_client: bigquery.Client, project: str, dataset: str) -> pd.DataFrame:
    """
    Explores the schema of a BigQuery dataset
    Args:
        bq_client: BigQuery client
        project: project id
        dataset: dataset name
    Returns:
        pandas dataframe
    """
    sql_script = f'''
    SELECT *
    FROM `{project}.{dataset}.INFORMATION_SCHEMA.COLUMNS`
    '''
    return bq_to_dataframe(bq_client, sql_script)