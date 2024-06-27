contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop(
    "guilherme@gmail.com"
)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {"chave não encontrada"})  # {}
print(resultado)


resultado = contatos.pop(
    "guilherme@gmail.com", "chave não encontrada"
)  # retorna somente a string sem estar dentro de uma lista ou dicionário
print(resultado)
