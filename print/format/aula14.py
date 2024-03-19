a = 'A'
b = 'B'
c = 1.1
formato = 'a={}\nb={}\nc={:.2f}'.format(a, b, c)
formatoIndex = 'a={0}\nb={1}\nc={2:.2f}'.format(a, b, c)
formatoNomeado = 'a={a}\nb={b}\nc={c:.2f}'.format(a=a, b=b, c=c)

print(formato)
print(formatoIndex)
print(formatoNomeado)