import json
from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.utils.dates import days_ago

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}


with DAG(
    dag_id='invoke_aws_lambda',
    default_args=default_args,
    description='A simple DAG to invoke an existing AWS Lambda function',
    schedule_interval=None,
    catchup=False
) as dag:

    # Task to invoke the AWS Lambda function
    invoke_lambda = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda_function',
        function_name='test_lambda_function', 
        log_type='Tail',  
        payload=json.dumps({
            'Airflow1': 'Astro1',
            'Airflow2': 'Astro2',
            'Airflow3': 'Astro3'
        }),
        aws_conn_id='aws_lambda', 
        region_name='us-east-1'
    )

    invoke_lambda