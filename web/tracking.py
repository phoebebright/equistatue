import requests
from django.conf import settings

import logging
logger = logging.getLogger('django')

def log_to_swetrix(request, ev=None, meta=None):
    try:
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        client_ip = _get_client_ip(request)

        payload = {
                'pid': settings.SWETRIX_PROJECT_ID,  # Set in settings.py
                'lc': request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'en-US',
                'pg': request.path,
                'tz': 'UTC',  # Or use pytz to detect timezone
                'unique': False,  # For unique visitor tracking
            }
        if ev:
            payload['ev'] = ev.replace(' ','_')

        if meta:
            payload['meta'] = meta

        requests.post(
            'https://api.swetrix.com/log',
            headers={
                'User-Agent': user_agent,
                'X-Client-IP-Address': client_ip,
                'Content-Type': 'application/json',
            },
            json=payload,
            timeout=2  # Avoid long delays
        )
    except Exception as e:
        logger.warning(f"Failed to log to Swetrix: {e}")
        pass
    else:
        logger.info(f"Logged to Swetrix: {request.path} from {client_ip} with ev {ev}")

def _get_client_ip(request):
    """Get the client IP, handling proxies."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # First IP in chain
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
