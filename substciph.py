# Modules
from random import choice
from string import ascii_uppercase
# Applying the cipher operation on a string (using a cipher dict)
def ciph(cipher: dict, msg: str) -> str:
	"""Replaces letters in a string using a cipher dict."""
	s = []
	msg = msg.upper()
	for i in msg:
		s.append(i)
	for i in range(len(s)):
		if s[i] in cipher:
			s[i] = cipher[s[i]]
	out = ""
	for i in s:
		out += i
	return out
# Converting cipher text to cipher dict
def conciph(ctxt: str) -> dict:
	"""Converts a cipher text to a cipher dict."""
	ctxt = ctxt.upper()
	cipher = {}
	if (len(ctxt) == 0) or (len(ctxt) % 2 != 0):
		raise ValueError("Cipher text length must be even.")
	for i in range(0, len(ctxt), 2):
		if ctxt[i] == ctxt[i+1]:
			raise ValueError("Pairs of cipher text must not have the same letters.")
		elif (ctxt[i] in cipher) or (ctxt[i+1] in cipher):
			raise ValueError("Cipher text must not contain repetitions.")
		elif (not ctxt[i] in ascii_uppercase) or (not ctxt[i+1] in ascii_uppercase):
			raise ValueError("Invalid character(s) in cipher text.")
		cipher[ctxt[i]] = ctxt[i+1]
		cipher[ctxt[i+1]] = ctxt[i]
	return cipher
# Generating a cipher text
def genciph(pair: int) -> str:
	"""Generates a random cipher text with a set amount of pairs."""
	if not (1 <= pair <= 13):
		raise ValueError("Pair count must be between 1 and 13.")
	ltrs = list(ascii_uppercase)
	ciph = ""
	for _ in range(pair*2):
		c = choice(ltrs)
		ciph += c
		ltrs.remove(c)
	return ciph