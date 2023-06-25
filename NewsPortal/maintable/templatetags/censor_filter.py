from django import template

register = template.Library()

BAD_WORDS = [
    'Редиска',
    'Бяка',
    'Бяке',
    'Бука',
    'Буке',
]

@register.filter()
def censor_filter(word):
    if isinstance(word, str):
        for i in word.split():
            if i.capitalize() in BAD_WORDS:
                word = word.replace(i, i[0] + '*' * len(i))
    return word


