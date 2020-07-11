from defines import getCreds, makeApiCall

def getInstagramMediaComment(params):
    """ Get instagram users's media

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-media-id}/comments?access_token={your-access-token}
    """
    
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['ga_media_id'] + '/comments'

    return makeApiCall(url, endpointParams, params['debug'])   

def getInstagramMediaCommentResponse():
    params = getCreds()
    params['debug'] = 'no'
    response = getInstagramMediaComment(params)
    return response

params = getCreds()
params['debug'] = 'no'
response = getInstagramMediaComment(params)
    
