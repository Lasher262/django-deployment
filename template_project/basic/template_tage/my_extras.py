from django import template

register = template.Library()

@register.filter(name='my')
def cut(val,arg):
	"""cuts out all values of args from string"""
	retrun val.replace(arg,'')


# register.filter('cut',cut)