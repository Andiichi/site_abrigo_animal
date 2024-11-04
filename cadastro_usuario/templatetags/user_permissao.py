from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    """
    Checa qual grupo o usuario faz parte
    """
    return user.groups.filter(name = group_name).exists()
