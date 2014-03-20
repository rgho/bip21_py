# BIP 21 URI Generator

### Description

A simple script that generates BIP21 compliant URI, given bitcoin address and optional label, amount, and message. The BIP0021 URI Scheme is described here: #https://github.com/bitcoin/bips/blob/master/bip-0021.mediawiki#ABNF_grammar


### Installation
import the script in your python file.
```python
import bip21
```

###Usage
There is only one function:

create_BIP21_URI(address, label, amount, message)

The address param is required. Must be valid bitcoin address.
All other params are optional
Amount must be a number with no commas


Below is a sample program that prints a bip21 URI, given an address, label, amount in bitcoins, and a message.
```python
import bip21
print bip21.create_BIP21_URI('1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i', 'Roger Andrews', 3, 'Nike shoes')

```

Output:
```
bitcoin:1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i?message=Nike%20shoes&amount=3&label=Roger%20Andrews
```
