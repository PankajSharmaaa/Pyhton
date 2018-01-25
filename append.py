Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> country =['India','usa','china','uk','canada']
>>> country
['India', 'usa', 'china', 'uk', 'canada']
>>> country =[India:1,usa:2,china:3,uk:4,canada:4]
SyntaxError: invalid syntax
>>> country =['India:1','usa:2','china:3','uk:4','canada:5']
>>> country
['India:1', 'usa:2', 'china:3', 'uk:4', 'canada:5']
>>> country.append('APGS')
>>> country
['India:1', 'usa:2', 'china:3', 'uk:4', 'canada:5', 'APGS']
>>> 
