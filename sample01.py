import urllib.request
import json
if __name__ == "__main__":
 url = 'https://www.googleapis.com/youtube/v3/channels'
 params = {
    'part': 'statistics',
    'id' : '',              #チャンネルID
    'key':''                #API Key
    }
 req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
 with urllib.request.urlopen(req) as res:
     result = res.read()
     json_dict = json.loads(result)

     print(json_dict['items'][0]['statistics']['subscriberCount'])