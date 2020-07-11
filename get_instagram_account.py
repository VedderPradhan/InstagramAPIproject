from defines import getCreds, makeApiCall

def getInstagramAccount(params):
    """ Get instagram account
    
    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'

    url = params['endpoint_base'] + params['page_id']

    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'yes'
response = getInstagramAccount(params)

print("\n----INSTAGRAM ACCOUNT INFO----")
print("Page ID: " + response['json_data']['id'])
print("Instagram Business Account ID: " + response['json_data']['instagram_business_account']['id'])

