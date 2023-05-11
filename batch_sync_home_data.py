import requests
import pandas as pd

def read_new_home_csv():
    df = pd.read_csv('new_homes/new_home_20_03.csv')
    result = df[["sc_home_id", "ep_edge_barcode"]].values
    result = tuple(map(tuple, result))
    return result

def sync_home_data(home_id, edge_id):
    endpoint = f"https://aafq-api.scg-trinity.tech/internal/{home_id}/edge_association/{edge_id}"
    token = "eyJraWQiOiIwblJ3ME0rZEdPTGpyWVo2a2RtTVwvNmhnQkd0aFV2a0hrOXMyZnRwMlwvTVE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIzb3RtZGxoaXA5M2s1aTRqYmNhdWhnamk0bSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidHJpbml0eS1hYWZxLWFwaS1wcm9kXC9zYy1hc3NldC1wcm9kIiwiYXV0aF90aW1lIjoxNjc5MjkwOTg5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfUHFmR1d1aVdkIiwiZXhwIjoxNjc5Mzc3Mzg5LCJpYXQiOjE2NzkyOTA5ODksInZlcnNpb24iOjIsImp0aSI6Ijg0OWQ2NDhiLTQwNzItNDE3OC1iNTI0LWEwZjQ0MzFiYzMxNyIsImNsaWVudF9pZCI6IjNvdG1kbGhpcDkzazVpNGpiY2F1aGdqaTRtIn0.GshEKrebH7V5b7dlf8oqCdatzsthcPpMTIlPRUeKUabljd0Bs84hozYxqcb-kKMt3lHMA1-PX_OmAUqQCfeWpaqEn3hFTZfPxGmKfu_qNQIFWkdQ5ZAn4G8oAAnjeAIwqO6W1mCFLpTvtbRiRiUeVwmBjjDW-mH8RDbxwGijRATrnuvAFO-rgC9lUjSKMa9pEolNpU-hyK6DfvIgkwEUTbvMJdBiS_FM2-yVl3xrR66_L3VpOFUG6CelPKDpwodb_J-V64IGyS00AdUzGQL9vTRLMDyotjdTNotip1E0paRhpiUUak0TpjMOTabr8pN1Zhyg7XbOlZhB38cVMv_YNA"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        requests.post(url=endpoint, headers=headers)
    except Exception as e:
        with open("error_logs/new_home_error", "w") as error_log_file:
            error_log_file.writelines(f"{home_id}-{edge_id}")


if __name__ == "__main__":
    print("batch sync")
    new_homes = read_new_home_csv()
    for new_home in new_homes:
        sync_home_data(home_id=new_home[0], edge_id=new_home[1])
