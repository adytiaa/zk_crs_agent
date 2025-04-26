from masumi_integration.masumi_client import MasumiClient

def submit_compute_task(query):
    client = MasumiClient()
    return client.submit_task({"query": query})