print(1+1)
print('a'+'b')
print()
# print('1' + 1) # Type Error - não da pra juntar string com int assim
print('1', type('1'))
print(int('1'), type('1'))
print(int('1'), type(int('1')))
print(1 + int('2'))
print(bool("")) # String vazia => False
print(bool(" ")) # String com qualquer valor => True
print(str(11) + 'b')