from main.models import Url, Client
from hashids import Hashids


def generate_shortcode():
    primary_key = 1

    try:
        primary_key = Url.objects.latest('id').id + 1
    except Exception:
        primary_key = 1
    finally:
        hashids = Hashids(min_length=6)
        hashid = hashids.encode(primary_key)

        return hashid


def shortcode_is_valid(shortcode):
    """verifies that shortcode does not exist and that
    and that shortcode is atleast 4 chars"""
    shortcode_exists = Url.objects.filter(shortcode=shortcode).exists()
    length_ok = True if len(shortcode) >= 4 else False

    if shortcode_exists==False and length_ok==True:
        return True
    return False


def get_or_create_client(request):
    if 'clientId' in request.COOKIES:
        client_id = request.COOKIES['clientId']
        client, _ = Client.objects.get_or_create(client_id=client_id)
        return client
    else:
        client_id = generate_shortcode()
        return Client.objects.create(client_id=client_id)


def set_cookie(request, response, client_id):
    if not 'clientId' in request.COOKIES:
        response.set_cookie('clientId', client_id, max_age=31556952)

