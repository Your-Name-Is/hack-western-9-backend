

	# Here's how you upload an image. 
	# name image 'Person.jpg'

from auth import authenticate

from datetime import datetime

# Pull authentication from the auth example (see auth.py)

album = None # You can also enter an album ID here
image_path = 'Person.jpeg'

album = None # You can also enter an album ID here
image_path = 'Person.jpg'


def upload_person(client):
	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  'Person',
		'title': 'Person',
		'description': 'Face {0}'.format(datetime.now())
	}
	image = client.upload_from_path(image_path, config=config, anon=False)
	return image

# If youwant to run this as a standalone script
if __name__ == "__main__":
	client = authenticate()
	image = upload_person(client)

	# print("You can find it here: {0}".format(image['link']))
	# ^useful reference