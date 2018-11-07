country = input('Nationality:')
age = input('Age:')
age = int(age) 
if country == 'Taiwan':
	if age >= 18:
		print('can drive')
	else:
		print('cannot drive')
elif country == 'US':
	if age >= 16:
		print('can drive')
	else: 
		print('cannot drive')
else:
	print('can only enter Taiwan or US')
