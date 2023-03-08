from django import template

register = template.Library()


@register.filter
def translate_number(value):
    value = str(value)
    persian = '۰١٢٣٤٥٦٧٨٩'
    english = '0123456789'
    eng_to_per_table = value.maketrans(english, persian)  # ساخت جدول تبدیل نظیر به نظیر اعداد
    return value.translate(eng_to_per_table)
