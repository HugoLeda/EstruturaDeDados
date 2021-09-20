""""
  Implemente  uma  função  que  retorne  uma  sequência de  números  conforme  explicado  a  seguir: Considere um algoritmo para determinar os números primos entre 2 e n. O algoritmo usa um conjunto de inteiros. 
  Inicialmente, o conjunto contém todos os inteiros entre 2 e n. O primeiro número primo é2  e  todos  os  múltiplos  de  2  são  removidos  do  conjunto.  O  próximo  número  do  conjunto(3)   é   primo   e   todos   os   seus   múltiplos   são   removidos   do   conjunto.   
  O   procedimento   serepete até que restem no conjunto somente os números primos.
  Por exemplo, n = 20.
  Passo  1: 2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20O primeiro número (2) é primo e todos seus múltiplos devem ser removidos. 
  Portanto:
  Passo 2: 2     3     5     7     9     11     13     15     17     19O próximo número (3) é primo e todos seus múltiplos devem ser removidos. 
  Portanto:
  Passo 3: 2 3 5 7 11 13 17 19O próximo número (5) é primo e todos seus múltiplos devem ser removidos. 
  Portanto:
  Passo 4: 2 3 5 7 11 13 17 19
e assim por diante.
"""