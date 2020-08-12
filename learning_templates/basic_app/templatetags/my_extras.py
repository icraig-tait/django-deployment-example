from django import template

register = template.Library()

# def cut(value, arg):
# 	"""
# 	This cuts out all values of "arg" from the string!
# 	"""
# 	return value.replace(arg, '') + 'dddd'
#
# register.filter('cut', cut)
#
#
#-----------------------------------------------------------
# is equvalent to using a 'decorator'
@register.filter(name='cuttt')
def cut(value, arg):
	"""
	This cuts out all values of "arg" from the string!
	"""
	return value.replace(arg, '') + 'eeee'

