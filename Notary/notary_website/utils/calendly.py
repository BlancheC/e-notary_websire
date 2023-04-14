import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

cal_api_key = os.environ['CAL_API_KEY']

def get_calendly_event_types():
    headers = {
        "Authorization": f"Bearer {cal_api_key}",
        "Content-Type": "application/json"
    }

    url = "https://api.calendly.com/event_types"

    response = requests.get(url, headers=headers)

    if response.ok:
        event_types = response.json()['collection']
        return {event['name']: event['uuid'] for event in event_types}
    else:
        raise Exception(f"Error fetching event types: {response.content}")

def create_calendly_event(event_type, start_time, end_time):
    headers = {
        "Authorization": f"Bearer {cal_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "event_type_uuid": event_type,
        "start_time": start_time,
        "end_time": end_time,
        "invitee_email": "",
        "invitee_first_name": "",
        "invitee_last_name": "",
        "timezone": "UTC"
    }

    response = requests.post("https://api.calendly.com/scheduled_events", headers=headers, data=json.dumps(data))

    if response.ok:
        event = response.json()
        return event['uri'], event['event_memberships'][0]['user']['name'], event['start_time'], event['id']
    else:
        raise Exception(f"Error creating event: {response.content}")
