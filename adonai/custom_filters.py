from django import template
from django.utils.timezone import now
from datetime import timedelta

register = template.Library()

@register.filter
def custom_timesince(value):
    if not value:
        return ""
    
    now_time = now()
    time_difference = now_time - value
    if time_difference.days > 0:
        return f"{time_difference.days} {'day' if time_difference.days == 1 else 'days'} ago"
    elif time_difference.seconds >= 3600:
        hours = time_difference.seconds // 3600
        return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
    elif time_difference.seconds >= 60:
        minutes = time_difference.seconds // 60
        return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
    else:
        seconds = time_difference.seconds
        return f"{seconds} {'second' if seconds == 1 else 'seconds'} ago"
