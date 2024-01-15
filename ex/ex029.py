
nome = str(input("Digite seu nome completo: "))
parte_do_nome = nome.split()
primeiro_nome = parte_do_nome[0]
ultimo_nome = parte_do_nome[-1]
print(f"Prazer em conhecer você!\n" "Seu primeiro nome é {}\n" "Seu ultimo nome é {}\n".format(primeiro_nome, ultimo_nome))
