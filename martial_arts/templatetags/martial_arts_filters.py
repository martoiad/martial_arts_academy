from django import template

register = template.Library()


@register.filter
def martial_art_image(name):
    images = {
        'Wing Tsun': 'images/wing_tsun.jpg',
        'Karate': 'images/karate.jpg',
        'Tai Chi': 'images/tai_chi.jpg',
    }

    return images.get(name, 'images/hero.jpg')