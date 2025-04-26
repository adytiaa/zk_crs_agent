import requests

MASUMI_ENDPOINT = "https://api.masumi.network/submit_task"

def submit_task(task_payload):
    response = requests.post(MASUMI_ENDPOINT, json=task_payload)
    if response.status_code == 200:
        return response.json().get('task_id')
    else:
        raise Exception(f"Failed to submit task: {response.text}")
