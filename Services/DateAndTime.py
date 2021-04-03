from datetime import datetime


def getTime() -> str:
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    return f'{date}T{time}'
