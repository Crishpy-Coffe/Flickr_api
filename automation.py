import flickrapi 
from flickrapi import * 
api_key = u'd094257bdf24e33aa57a90af17a059ad' 
api_secret = u'2bf9965300d9aed2'
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json') 
photos = flickr.photos.search(user_id='195783907@N07', per_page='10') 
sets = flickr.photosets.getlist(user_id='195783907@N07') 
print('First set title: %s' % sets)