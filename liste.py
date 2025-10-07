adresses_ip =["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]

Classes = {
    "classe C" : "192.168.0.1",
    "10.0.0.1" : "classe A",
    "172.16.0.1" : "classe B172.16.0.1" ,
    "adresse IP publique" : "200.100.50.1",
    "169.254.0.1" : "adresse IP de lien local (APIPA)"
}

#Question 1:
print(f"la premiére adresse dans la liste est : {adresses_ip[0]}")
print()

#Question 2:
print(f"la derniére adresse dans la liste est : {adresses_ip[-1]}")
print()

#Question 3:
print(f"la troisiéme adresse dans la liste est : {adresses_ip[2]}")
print()

#Question 4:
adresses_ip.append("172.31.0.1")
print(adresses_ip)
print()

#Question5:
adresses_ip.remove("200.100.50.1")
print(adresses_ip)
print()

#Question 6:
print("le nombres des adresses IP restantes sont : ",len(adresses_ip))
print()

#Question 7:
for adresse_ip in adresses_ip:
    if adresse_ip=="192.168.0.1":
        exist = True 
if exist :
    print("'192.168.0.1' est présente dans la liste.")
else:
    print("'192.168.0.1' n'est pas présente dans la liste.")
print()

#Question 8:
print(f"La classe de l'adresse IP de '10.0.0.1' est : {Classes["10.0.0.1"]}")
print()

#Question 9:
adresses_ip.sort()
print(f"les adresses IP en ordre croissant : {adresses_ip}")
print()

#Question 10:
print("Vérification si toute les adresses IP appartiennent à la classe C:")
for adresse_ip in adresses_ip:
    if adresse_ip == Classes["classe C"]:
        print(f"\t{adresse_ip} appartienne à la classe C.")
    else:
        print(f"\t{adresse_ip} n'appartienne pas à la classe C.")
print()

#Question 11:
num_adress=0
for adresse_ip in adresses_ip:
    if adresse_ip==Classes["adresse IP publique"]:
        num_adress+=1 
print(f"le nombre des adresses IP de la liste qui sont des adresse IP publiques sont : {num_adress}")