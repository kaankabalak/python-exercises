name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
	if len(arr1) >= len(arr2):
		tuples = zip(arr1, arr2)
		new_dict = dict(tuples)
		return new_dict
	else:
		tuples = zip(arr2, arr1)
		new_dict = dict(tuples)
		return new_dict

print make_dict(name, favorite_animal)