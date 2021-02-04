from rest_framework.decorators import api_view
from main.models import Url
from rest_framework.response import Response
from main.api.utils import (
                            shortcode_is_valid, 
                            generate_shortcode)

@api_view(['POST'])
def shorten_url(request):
    """
            Allows for the shortening of urls.
            this endpoint accepts a POST request
            with a payload in the form below
            {
                'longUrl' : 'the url to be shortened',
                'shortcode : 'some shortcode here' (optional)
            }

            it then returns a response in the form below:

            {
                'longUrl' : 'the url to be shortened',
                'shortcode' : 'the shortened url'
            }
    """
    data = request.data
    long_url = data['longUrl']

    try:
        shortcode = data['shortcode']

        if shortcode_is_valid(shortcode):
            url = Url.objects.create(
                                    long_url=long_url, 
                                    shortcode=shortcode,)
            
            return Response(
                                {
                                    "longUrl": long_url,
                                    "shortcode": url.shortcode
                                }
                                )
        
        return Response(
                            {
                                "shortcodeNotUnique": True
                            }
                            )
    except KeyError:
        shortcode = generate_shortcode()
        url = Url.objects.create(
                                  long_url=long_url, 
                                  shortcode=shortcode,)
        
        return Response(
                            {
                                "longUrl": long_url,
                                "shortcode": url.shortcode,
                                "shortcodeNotUnique": False
                            }
                            )