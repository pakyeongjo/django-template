import ast
import os

import boto3
from botocore.exceptions import ClientError

STAGE = os.getenv('STAGE', 'local')
PROJECT = ""
AWS_PROFILE = ""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

secret_manager_objects = {
    'secret_key': f"{STAGE}/{PROJECT}/secret_key",
    'db': f"{STAGE}/{PROJECT}/database"
}


def get_secret_by_path(name):
    session = boto3.session.Session(profile_name=AWS_PROFILE)
    client = session.client(
        service_name='secretsmanager',
        region_name="ap-northeast-2",
        endpoint_url="https://secretsmanager.ap-northeast-2.amazonaws.com"
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
    else:
        # Decrypted secret using the associated KMS CMK
        # Depending on whether the secret was a string or binary, one of these fields will be populated
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            return ast.literal_eval(secret)
        else:
            binary_secret_data = get_secret_value_response['SecretBinary']
            return binary_secret_data


def get_config(stage):
    if stage == "local":

        from configparser import RawConfigParser

        config_local = RawConfigParser()
        config_local.read(os.path.join(BASE_DIR, '', 'settings/settings-local.ini'), encoding='utf-8')

        conf_info = {
            'secret_key': {
                'SECRET_KEY': config_local.get('base', 'SECRET_KEY'),
            },
            'db': {
                'NAME': config_local.get('db', 'NAME'),
                'HOST': config_local.get('db', 'HOST'),
                'PASSWORD': config_local.get('db', 'PASSWORD'),
                'PORT': config_local.get('db', 'PORT'),
                'USER': config_local.get('db', 'USER'),
            },
        }
    else:
        conf_info = {
            'secret_key': get_secret_by_path(secret_manager_objects['secret_key']),
            'db': get_secret_by_path(secret_manager_objects['db']),
        }
        return conf_info

    return conf_info


conf_info = get_config(STAGE)
