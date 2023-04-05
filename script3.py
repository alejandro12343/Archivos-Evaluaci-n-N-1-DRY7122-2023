acl_num = input("Ingrese el número de ACL IPv4: ")

if acl_num.isdigit() and int(acl_num) >= 1 and int(acl_num) <= 99:
    print("La ACL " + acl_num + " es una ACL Estándar.")
elif acl_num.isdigit() and int(acl_num) >= 100 and int(acl_num) <= 199:
    print("La ACL " + acl_num + " es una ACL Extendida.")
else:
    print("El número ingresado no corresponde a una lista de acceso.")
