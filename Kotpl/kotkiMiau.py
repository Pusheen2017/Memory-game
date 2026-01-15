running = True
def rysujkotki(ilerazy):
    for i in range(ilerazy):
        print("=^.^=")
while running:
    ilerysowac = int(input("Ile razy narysować kotka? "))
    rysujkotki(ilerysowac)
    taklubnie = str(input("Kontynuować?(t/n):"))
    if taklubnie.lower()=="t":
        pass
    else:
        running = False