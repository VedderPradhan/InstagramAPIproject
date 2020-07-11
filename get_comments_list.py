from get_instagram_media_comment import getInstagramMediaCommentResponse
from defines import getCreds

import requests
import json

def getCommentIdList():

    response = getInstagramMediaCommentResponse()

    commentIDs = []
    for data in response['json_data']['data']:
        commentIDs.append(data['id'])
    
    
    while 'paging' in response['json_data'].keys():
        nextCommentPageUrl = response['json_data']['paging']['next']

        data = requests.get(nextCommentPageUrl)
        response['json_data'] = json.loads(data.content)
        
        for data in response['json_data']['data']:
            commentIDs.append(data['id'])
            
    return commentIDs




