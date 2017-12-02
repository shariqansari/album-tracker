from django.conf import settings

def titles(request):
    return {
        'site_title':       settings.SITE_TITLE,
        'site_title_short': settings.SITE_TITLE_SHORT,
        }
