def PG(primeirotermo, razao):
    for i in range(10):
        termo = primeirotermo * i ** razao
        print(termo)

termo1 = int(input("digite o primeiro termo: "))
razaopg = int(input("digite a razão da PG: "))

PG(termo1, razaopg)