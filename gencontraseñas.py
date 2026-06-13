import random
import string

contraseña = ""

variable = string.ascii_letters + string.digits

for i in range (8):
    contraseña = contraseña + random.choice(variable)
print(contraseña)
