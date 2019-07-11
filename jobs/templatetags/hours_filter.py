from django import template

register = template.Library()


@register.filter(name="hours")
def hours(value):
    """Format half_hour_count to display it as %H%Hh%M%M."""
    return f"{value//2}{('h00', 'h30')[value % 2]}"
