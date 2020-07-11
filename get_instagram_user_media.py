from defines import getCreds, makeApiCall

def getInstagramUserMedia(params):
    """ Get instagram users's media

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?access_token={your-access-token}
    """

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id'] + '/media'

    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'yes'
response = getInstagramUserMedia(params)


