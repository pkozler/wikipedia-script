# Nástroj pro hledání článků na Wikipedii

CLI program, který po zadání vstupního textu
vypíše souhrn (např. první odstavec) článku z (české) Wikipedie s takovým názvem.
Neexistuje-li článek se zadaným názvem, program vypíše názvy článků, jež zadaný
text obsahují. Program si pamatuje již hledané výrazy, aby se zamezilo zbytečným
dotazům na servery Wikipedie.

### Požadavky

Ke spuštění programu je doporučeno použít Python **verze 3.9** nebo vyšší.

### Příklad výstupu

**Existující článek**

Při zadání textu "_python_" by měl program vypsat například následující text:

```
Python (anglická výslovnost [ˈpaiθən]) je vysokoúrovňový skriptovací
programovací jazyk, který v roce 1991 navrhl Guido van Rossum. Nabízí
dynamickou kontrolu datových typů a podporuje různá programovací
paradigmata, včetně objektově orientovaného, imperativního,
procedurálního nebo funkcionálního. V roce 2018 vzrostla jeho
popularita a zařadil se mezi nejoblíbenější jazyky. V řadě
různých žebříčků dosahuje jedno z prvních třech míst, výjimkou
nebývají první místa.
```

**Neexistující článek**

Při zadání textu "_rumbellion_" by měl program vypsat například následující text:

```
Článek s názvem 'rumbellion' nebyl nalezen. Zadaný text se vyskytuje
v článcích s tímto názvem:
Rum
```
