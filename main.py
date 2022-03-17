if __name__ == "__main__":
    # Execute suas testagens manuais aqui
    from classes import Recipiente, Copo
    r = Recipiente(100)
    print(r)
    print (r.esta_limpo())
    print(r.esta_limpo())
    print(r.sujar())
    print(r.esta_limpo())
    
    c = Copo(300)
    print(c)
    print(c.encher('café'))
    print(c.bebida)
    print(c)
    print (c.beber(30))
    print(c)
    print(c.lavar())
    print(c.esta_limpo())