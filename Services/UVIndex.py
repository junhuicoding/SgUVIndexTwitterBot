import requests

BASE_URL = "https://api.data.gov.sg/v1/environment/uv-index"


def getUVIndexResults(requestTime: str) -> []:
    request = BASE_URL + f'?date_time={requestTime}'
    print(f"requesting {request}")
    response = requests.get(request)

    response_json = response.json()
    result_list = response_json.get("items")

    return result_list[0].get("index")


def verifyLatestUVIndex(requestTime: str, result_list: [dict]) -> dict:
    trimmedTime = requestTime[:-5]
    for result in result_list:
        if trimmedTime in result.get("timestamp"):
            return result

    return None
