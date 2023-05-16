import requests
import os
from slack_sdk import WebClient
import logging
from slack_sdk.errors import SlackApiError
logger = logging.getLogger(__name__)

data = {
    'email': 'wewang@redhat.com'
}
def get_userid_by_email(**email):

    #token=os.environ.get('SLACK_BOT_TOKEN')
    url = "https://slack.com/api/users.lookupByEmail"

    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer <token>',
        "type": "url_verification"
    }
    resp = requests.post(url,email, headers=headers)
    return resp.json().get('user',{}).get('id')
try: 
    print(get_userid_by_email(**data))
except SlackApiError as e:
    print(f"Error: {e}")
