from main.models import Url
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
    pass


def set_cookie(request, response, client_id):
    pass

