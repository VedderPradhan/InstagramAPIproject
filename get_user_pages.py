from defines import getCreds, makeApiCall

def getUserPages(params):
    """ Get facebook pages for a user

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}
    Returns:
            object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'me/accounts'

    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'yes'
response = getUserPages(params)

print ("\n----FACEBOOK PAGE INFO----\n")
print ("Page Name: " + response['json_data']['data'][0]['name'])
print ("Page ID: " + response['json_data']['data'][0]['id'])
