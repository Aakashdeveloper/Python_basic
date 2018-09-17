phones = {"apple", "samsung", "sony"}

>>> phones = {"apple", "samsung", "sony"}
>>> phones
{'apple', 'sony', 'samsung'}
>>> phones.add('sony')
>>> phones
{'apple', 'sony', 'samsung'}
>>> phones.add('mi')
>>> phones
{'apple', 'sony', 'mi', 'samsung'}
>>> phones.remove('mi')
>>> phones
{'apple', 'sony', 'samsung'}


laptop = set(("HP", "MAc", "Lenovo"))