# Definición de la tupla
config_servidor = ("192.168.10.5", 8080, True)
# Acceso al segundo elemento (índice 1)
puerto = config_servidor[1]
print(f"Servidor configurado en el puerto: {puerto}")