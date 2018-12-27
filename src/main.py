import json
from logging import getLogger
from os import getenv
import requests

log = getLogger()
log.setLevel('INFO')

session = requests.Session()
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {0}'.format(getenv('AUTH_TOKEN')),
}
session.headers.update(headers)

def lambda_handler(event, context):
    log.info(event)
    for record in event['Records']:
        data = {
          'notify': 'true',
          'color': 'red',
          'message_format': 'text',
          'from': record['Sns']['TopicArn'].split(':')[-1],
          'message': record['Sns']['Message'],
        }
        session.post(getenv('HIPCHAT_ENDPOINT'), data=json.dumps(data))
