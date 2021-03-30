class Sanitise(object):
	def gender(args):
		arb = ''
		for each in args:
			arb += each
		arb = arb.lower()
		if arb == 'male' or arb == 'boy' or arb =='man' or arb == 'm':
			return 'Male'
		elif arb == 'female' or arb == 'girl' or arb == 'woman' or arb == 'f':
			return 'Female'
		else:
			raise ValueError
	
	def game(args):
		arb = ''
		for each in args:
			arb += each
		arb = arb.lower()
		if arb == 'sapphire':
			return 'Sapphire'
		elif arb == 'ruby':
			return 'Ruby'
		elif arb == 'emerald':
			return 'Emerald'
		elif arb == 'perla':
			return 'Perla'
		elif arb == 'firered' or arb == 'fire':
			return 'Fire'
		elif arb == 'leafgreen' or arb == 'leaf':
			return 'Leaf'
		elif arb == 'chaosblack' or arb == 'chaos':
			return 'Chaos'
		else:
			raise ValueError
