from django import template

register = template.Library()

def media_folder_products(string):
    if not string:
        string = 'product_images/default.jpg'
    return settings.MEDIA_URL + string



register = filter('media_folder_products'.media_folder_products)

@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/default.jpg'
    return settings.MEDIA_URL + string