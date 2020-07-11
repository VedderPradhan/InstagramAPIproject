from defines import getCreds, makeApiCall
import re

def getCommentInfo(params, commentID):
    """ Get instagram media commentator's username

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-comment-id}?
            fields={fields}&access_token={your-access-token}
    """

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'username,text'

    url = params['endpoint_base'] + '/' + commentID

    return makeApiCall(url, endpointParams, params['debug'])


def getCommentatorAndComment(commentID):
    params = getCreds()
    params['debug'] = 'no'
    response = getCommentInfo(params, commentID)

    commentator = response['json_data']['username']
    comment = response['json_data']['text']

    return commentator, comment


##tags = re.search('(@\S*).*(@\S*).*(@\S*)(\s{1}|$)', comment)

##if (len(tags.groups()) >= 3 ):
##    print ("Tagged accounts: " + tags.group(1) + ", " 
##                           + tags.group(2) + ", "
##                           + tags.group(3) )

"""m = re.search('(@.*)(@.*)(@.*)\s{1}', 'hey fsadf@adb@adf@dfd hey')"""

"""m = re.search('(@\S*)(@\S*)(@\S*)\s{1}', 'hey fsadf @adb@adf@dfd hey dsfd')"""

"""m = re.search('(@\S*).*(@\S*).*(@\S*)\s{1}', 'hey fsadf @adb@adf@dfd hey dsfd')"""
