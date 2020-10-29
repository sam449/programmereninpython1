PS C:\Users\sambd\Documents\Mediacollege2\programmereninpython
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is <Sam>')
Mijn naam is <Sam>
>>> naam = '<Sam>'
>>> print(naam)
<Sam>
>>> print(naam.upper())
<SAM>
>>> print(naam[0:2])
<S
>>> print(naam[::-1])
>maS<
>>> leeftijd = 19
>>> print('Hallo' + naam + 'ben je al' + str(leeftijd) + 'jaar?')
Hallo<Sam>ben je al19jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
20
>>> leeftijd-=1
>>> leeftijd
19
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Het is alweer 1 jaar geleden dat je 18 werd ;-)
>>> from random import randint
>>> randint(0,1000)
747
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
775
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 775
>>>
>>>
>>>
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-16 12:15:49.829710
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>>
>>>
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 16 settembre 2020'
