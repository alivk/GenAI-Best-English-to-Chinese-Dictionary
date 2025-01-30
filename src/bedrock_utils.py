import boto3
import json
import streamlit as st

def get_bedrock_client():
    credentials = get_bedrock_credentials()
    if credentials:
        return boto3.client(
            'bedrock-runtime',
            region_name=credentials['region_name'],
            aws_access_key_id=credentials['aws_access_key_id'],
            aws_secret_access_key=credentials['aws_secret_access_key']
        )
    return None

def get_bedrock_credentials():
    secrets_client = boto3.client('secretsmanager')
    secret_name = "bedrocksecrets"
    try:
        response = secrets_client.get_secret_value(SecretId=secret_name)
        secrets = json.loads(response['SecretString'])
        return {
            'region_name': secrets.get('AWS_REGION'),
            'aws_access_key_id': secrets.get('AWS_ACCESS_KEY_ID'),
            'aws_secret_access_key': secrets.get('AWS_SECRET_ACCESS_KEY'),
            'kendra_index_id': secrets.get('AWS_KENDRA_INDEX_ID'),
            'session_secret': secrets.get('SESSION_SECRET'),
            'session_secret_bdm1': secrets.get('SESSION_SECRET_BDM1'),
            'session_secret_bmd2': secrets.get('SESSION_SECRET_BMD2'),
            'session_secret_instructor1': secrets.get('SESSION_SECRET_INSTRUCTOR1'),
            'session_secret_instructor2': secrets.get('SESSION_SECRET_INSTRUCTOR2')
        }
    except Exception as e:
        st.error(f"Error retrieving Bedrock credentials: {e}")
        return None 