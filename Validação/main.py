from util import validar_email, validar_cpf

email = input("Digite seu email: ")
print("Email válido: ", validar_email(email))

cpf = input("Digite seu CPF: ")
print("CPF válido: ", validar_cpf(cpf))