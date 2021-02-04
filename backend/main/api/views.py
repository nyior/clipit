from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, redirect

from main.api.utils import (
                            shortcode_is_valid, 
                            generate_shortcode)
from main.models import Url

import time

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
                                "shortcodeInvalid": True
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
                                "shortcode": url.shortcode
                            }
                            )



def redirect_view(request, shortcode):
    """
        Redirect to original url given shortcode.
    """
    model = Url
    obj = get_object_or_404(model, shortcode=shortcode)
    obj.visited()
    return redirect(obj)


@api_view(['GET'])
def get_url_stats(request, shortcode):
    """
        gets the stats for the specified shortcode
    """
    
    model = Url
    obj = get_object_or_404(model, shortcode=shortcode)
    visited = obj.last_accessed

    #converts datetime to human readable form: 04-Feb-2021 at 21:26
    date_created = obj.created_at.strftime("%d-%b-%Y at %H:%M")
    visited.strftime("%d-%b-%Y at %H:%M") if visited is not None else visited
    hits = obj.hits

    return Response(
                        {
                            "dateCreated": date_created,
                            "lastAccessed": visited,
                            "hits": hits
                        }
                        )