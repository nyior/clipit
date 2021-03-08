from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404, redirect

from main.api.utils import (
                            shortcode_is_valid, 
                            generate_shortcode,
                            get_or_create_client,
                            set_clientid_cookie)
from main.models import Url, Client

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
        #shortcode in request data?
        shortcode = data['shortcode']
    except KeyError:
        #create shortcode if not sent in request data
        shortcode = generate_shortcode()
    
    #shortcode atleast four chars long?
    if shortcode_is_valid(shortcode):
        client = get_or_create_client(request)

        url = Url.objects.create(
                                long_url=long_url, 
                                shortcode=shortcode,
                                created_by=client)
            
        response = Response(
                            {
                                "longUrl": long_url,
                                "shortcode": url.shortcode
                            }
                        )

        #sets cookie               
        set_clientid_cookie(request, response, client.client_id)
        return response
        
    return Response( {"shortcodeInvalid": True} )
    

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

    if visited is not None:
        visited = visited.strftime("%d-%b-%Y at %H:%M")

    hits = obj.hits

    return Response(
                        {
                            "dateCreated": date_created + " " + "GMT",
                            "lastAccessed": visited,
                            "hits": hits
                        }
                        )


@api_view(['GET'])
def get_client_urls(request):
    """this view returns a list of all the urls shortened
    by a user"""
    if 'clientId' in request.COOKIES:
        urls = []

        client_id = request.COOKIES['clientId']
        client, _ = Client.objects.get_or_create(
            client_id=client_id
        )

        url_objects = Url.objects.filter(
            created_by=client
        ).order_by("-created_at")
        
        for url in url_objects:
            url = {
                "longUrl": url.long_url,
                "shortcode": url.shortcode
            }

            urls.append(url)
            
        return Response({"urls": urls, "has_urls": True})

    return Response({"has_urls": False})