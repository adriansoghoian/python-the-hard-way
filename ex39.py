states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'JacksonVille'
}

for state, name in cities.items():
	print "The state abbreviation is %s and the name is %s" % (state, name)

state = states.get("Texas")
florida = states.get('Florida')

if state:
	print "TRUE"
else:
	print "FALSE"
print florida

city = cities.get('TX', 'Boogley I"m a default value!!')
print city