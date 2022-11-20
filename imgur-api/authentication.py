# authenticating yourself
from imgurpython import ImgurClient
from helpers import get_input, get_config

def authenticate():
	# Get client ID and secret from auth.ini (.ini was for different examples for the sake of consistency)
	config = get_config()
	config.read('auth.ini')
	client_id = config.get('credentials', 'client_id')
	client_secret = config.get('credentials', 'client_secret')

	client = ImgurClient(client_id, client_secret)

	# Authorization flow
	authorization_url = client.get_auth_url('pin')

	print("Go to the following URL: {0}".format(authorization_url))

	# Read in the pin, handle Python 2 or 3 here.
	pin = get_input("Enter pin code: ")

	# redirect user to `authorization_url`, obtain pin (or code or token)
	credentials = client.authorize(pin, 'pin')
	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])

	print("Authentication successful! Here are the details:")
	print("   Access token:  {0}".format(credentials['access_token']))
	print("   Refresh token: {0}".format(credentials['refresh_token']))

	return client

#can run as standalone script if needed
if __name__ == "__main__":
	authenticate()