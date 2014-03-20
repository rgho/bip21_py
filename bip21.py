#BIP 0021 Bitcoin Payment URI Scheme
#https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki#ABNF_grammar

# A function that takes and bitcoin address, optional label, and optional amount.
# Returns BIP21 compliant URI that should work

import urllib

def isValidAddr(address):
	return True

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def create_BIP21_URI(address, label=None, amount=None, message=None):
	# bitcoin:175tWpb8K1S7NmH4Zx6rewF9WQrcZv245W?amount=50&label=Luke-Jr&message=Donation%20for%20project%20xyz
	if not isValidAddr(address): return 'None'
	uri = 'bitcoin:' + address

	# Populate a dict of key value pairs. percent encode the values.
	key_value_pairs = {}
	if message != None: key_value_pairs['message'] = urllib.quote(message) 
	if amount != None and is_number(amount): key_value_pairs['amount'] = urllib.quote(str(amount)) #Must convert to string to avoid rstrip errors later.
	if label != None: key_value_pairs['label'] = urllib.quote(label) 

	# Detect if any keys actually exist and add a '?' and url encoded string accrodingly.
	if len(key_value_pairs) > 0: uri += '?' + '&'.join([key+'='+key_value_pairs[key] for key in key_value_pairs])
	return uri
	

print create_BIP21_URI('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', 'Roger Andrews', 3, 'Nike shoes')
