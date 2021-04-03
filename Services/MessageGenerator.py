from Services.DateAndTime import getTime
from Services.Twitter import tweet
from Services.UVIndex import getUVIndexResults, verifyLatestUVIndex

uvRangeDictionary = {
    0: "low",
    1: "low",
    2: "low",
    3: "moderate",
    4: "moderate",
    5: "moderate",
    6: "high",
    7: "high",
    8: "very high",
    9: "very high",
    10: "very high",
    11: "EXTREME"
}

messageDictionary = {
    "low": "Shiok weather :) Enjoy the great outdoors!",
    "moderate": "Just another typical day in the Sunny Island.",
    "high": "Some protection against sun damage is recommended, do not stay out in this sun for too long!",
    "very high": "Avoid being outside for a prolonged period of time. Make sure to seek shade and use sunscreen (at "
                 "least SPF 30)!",
    "EXTREME": "Avoid being outside, but if you have to go out, make sure to seek shade and use sunscreen (at "
                 "least SPF 30). Bring along an umbrella and remember to hydrate yourself frequently. Stay safe!"
}


def generateUVTweetNow():
    currTime = getTime()
    results = getUVIndexResults(currTime)
    result = verifyLatestUVIndex(currTime, results)

    if result is not None:
        uvIndex = result.get("Value")
        tweet(generateUVMessage(uvIndex))

    print(f'Current time is: {currTime}. No results available')
    return


def generateUVMessage(uvIndex: int) -> str:
    uvLevel = uvRangeDictionary.get(min(uvIndex, 11))
    uvMessage = messageDictionary.get(uvLevel)
    punctuation = "."
    if uvIndex > 7:
        punctuation = "!"
    if uvIndex > 10:
        punctuation = "!!!"

    message = f'The current UV Index is {uvLevel} at {uvIndex}{punctuation}\n' \
              f'{uvMessage}'
    return message
