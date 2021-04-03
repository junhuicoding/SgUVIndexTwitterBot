# WhereToDineBot
Singapore is a very sunny place, with a high UV index. Most of us are used to it and are unaware of how it affects and damages our skin. This Twitter bot was built to update the masses of the current UV index hourly, as well as provide some recommended actions to help prevent those damages.
The account can be found [@SgUVIndexBot](https://twitter.com/SgUVIndexBot)

## Technical Details
The program uses the Ultra-violet Index API from [Data.gov.sg](https://data.gov.sg/dataset/ultraviolet-index-uvi) to pull the UV Index which is updated every hour between 7 AM and 7 PM everyday
A Twitter API is required to connect it to Twitter to post tweets automatically.

## Installation
Configure Keys.py with the respective twitter keys from twitter. Information on how to set up a developer account [here](https://developer.twitter.com/en).

###Run it with docker
```
docker build -t <name> .
```
```
docker run <name>
```
### Run from command line
```shell script
pip3 install -r requirements.txt

python3 App.py
```
## Planned Features
- More interesting and randomised messages
- DM feature to be able to reply to on Demand DM queries
- Hosting this app on a free remote server

## License
The MIT License (MIT)

Copyright (c) 2021 Jun Hui Chua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.