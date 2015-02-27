class MaraudersMapError(Exception):
	'''Should hopefully not get many of these, can't figure out where I'd need them'''
	pass

class RowlingError(Exception):
	''' These should be if user is trying to do something they can't,
        like go north from a room with one path to the south'''
	pass

class LegilimensError(Exception):
	'''These are for weird commands I don't understand'''
	pass

class Messages(object):

    GOBBLEDEGOOK = "I'm sorry, I didn't understand any of that."
    UNKNOWN_VERB = "I'm sorry, I don't know how to do that."

