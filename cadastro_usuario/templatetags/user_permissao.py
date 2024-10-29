from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    """
    Checa qual grupo o usuario faz parte
    """
    return user.groups.filter(name = group_name).exists()

# @register.filter
# def is_vol(user):
#     """
#     Checa se o usuário logado é um voluntario
#     """
#     return user.groups.filter(name = 'Voluntários')