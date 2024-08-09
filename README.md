# Analisador Sintático LL(1)

Trabalho feito para a matéria de compiladores com base no Analisador Sintático Descendente **(faz a análise da raiz da árvore para o folhas, tendo sua derivação para o elemento mais a esquerda, até chegar ao terminal correspondente)**, de um compilador básico, implementado em PYTHON utilizando a seguinte gramatica:

**1. E  -> T E'**

**2. E' -> + T E' | ε**

**3. T  -> F T'**

**4. T' -> * F T' | ε**

**5. F  -> id | ( E )**

Gramatica já fatorada para que possa ser considerada como LL(1) (L = Left to Right, L = Leftmost, 1 = 1 token por vez)
