class Arvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def __repr__(self):
        return '%s <- %s -> %s' % (
        self.esquerda and self.esquerda.chave,
        self.chave,
        self.direita and self.direita.chave)

def sequencia(raiz):
  if not raiz:
    return

  sequencia(raiz.esquerda)
  print(raiz.chave)
  sequencia(raiz.direita)

def insert(raiz, No):
  if raiz is None:
    raiz = No
  elif raiz.chave < No.chave:
    if raiz.direita is None:
      raiz.direita = No
    else:
      insert(raiz.direita, No)
  else:
    if raiz.esquerda is None:
      raiz.esquerda = No
    else: 
      insert(raiz.esquerda, No)

def busca(raiz, chave):
    if raiz is None:
        return None
    if raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    return busca(raiz.esquerda, chave)

raiz = Arvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = Arvore(chave)
    insert(raiz, nodo)

for chave in [-20, -10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))