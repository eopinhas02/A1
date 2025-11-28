idade = int(input("Digite sua idade: ")) # o usuario está declarando o valor da variavel 

if idade < 18: # SE a idade do usuario for menor que 18, ele não podera ir para o baile 
    print("Você não pode ir para o evento, tudo no seu tempo") # aqui estamos imprimindo
elif idade >= 50: # OU, se o sujeito for mais velho que 50 anos de idade, ele não poderá entrar no evento
    print("Você é velho para o evento") # aqui estamos imprimindo
else: # SE NÂO, o jovem pode participar do evento. Caso ele tenha entre 18 e 49 anos 
    print("Você pode ir para o evento, aproveite a juventude!") # aqui estamos imprimindo