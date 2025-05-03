# how this works

the `prepare()` function normally runs once. it exists to prepare stuff like punctuation and the conversion table to not recreate them on every function call of the other function.

the `korn(text, ipa)` function returns the korn translation of the `text` you provide into it. it can optionally give you the `ipa` of the phrase, set that parameter to True in that case.

***

hopefully this code will be implemented into Linku, though that is not definite