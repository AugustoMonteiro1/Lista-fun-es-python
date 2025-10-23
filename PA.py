def PA(primeiro_termo, razao):
    for i in range(10):
        termo = primeiro_termo + i * razao
        print(termo)
        
termo1 = int(input("Digite o primeiro termo da PA: "))
razaopa = int(input("Digite a razão da PA: "))

PA(termo1, razaopa)