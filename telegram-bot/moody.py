import indicoio

indicoio.config.api_key = 'b09e30618dac907d86f8afb6dbeff68e'

# dictOfLists is supplied -> dictOfList with usr:mood is returned
def evaluate(dictOfList):
	result = dict()
	for key in dictOfList:
		result[key] = evalMood(dictOfList[key])
	return result
pass

# listOfStrings is supplied -> mood of those strings
def evalMood(listOfStr):
	stats=indicoio.emotion(str(listOfStr))
	return max(stats, key=stats.get)
pass
