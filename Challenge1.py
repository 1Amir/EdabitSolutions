#Based on the name of the person, return their relationship to luke
def relation_to_luke(name):
	solutions = {'Leia':'sister',
	'Darth Vader':'father',
	'Han':'brother in law',
	'R2D2':'droid'}
	return 'Luke, I am your {}.'.format(solutions[name])
