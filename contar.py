#!/usr/bin/env python
arquivo = file("text.txt")
palavras = arquivo.read().split()
unicas = set(palavras)
 
print 'Palavras: %d. Tirando as repetidas: %d' % (len(palavras), len(unicas))
