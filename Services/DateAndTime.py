from datetime import datetime
import pytz


def getTime() -> str:
    now = datetime.utcnow()
    now = now.replace(tzinfo=pytz.utc)
    now = now.astimezone(pytz.timezone("Singapore"))
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    return f'{date}T{time}'
