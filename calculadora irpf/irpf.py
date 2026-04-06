def formatar_real(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return "R$ " + texto


def ler_salario():
    entrada = input("Digite o salário bruto (ou 'sair' para encerrar): ").strip().lower()

    if entrada == "sair":
        return "sair"

    entrada = entrada.replace("r$", "").replace(" ", "")

    if "," in entrada and "." in entrada:
        if entrada.rfind(",") > entrada.rfind("."):
            entrada = entrada.replace(".", "")
            entrada = entrada.replace(",", ".")
        else:
            entrada = entrada.replace(",", "")
    elif "," in entrada:
        entrada = entrada.replace(".", "")
        entrada = entrada.replace(",", ".")

    try:
        salario = float(entrada)
        if salario < 0:
            print("Erro: o salário não pode ser negativo.\n")
            return None
        return salario
    except:
        print("Erro: digite um valor numérico válido.\n")
        return None


def calcular_imposto_bruto(salario):
    if salario <= 2428.80:
        imposto = 0
    elif salario <= 2826.65:
        imposto = salario * 0.075 - 182.16
    elif salario <= 3751.05:
        imposto = salario * 0.15 - 394.16
    elif salario <= 4664.68:
        imposto = salario * 0.225 - 675.49
    else:
        imposto = salario * 0.275 - 908.73

    if imposto < 0:
        imposto = 0

    return imposto


def calcular_reducao(salario, imposto_bruto):
    if salario <= 5000:
        reducao = 312.89
    elif salario <= 7350:
        reducao = 978.62 - (0.133145 * salario)
    else:
        reducao = 0

    if reducao < 0:
        reducao = 0

    if reducao > imposto_bruto:
        reducao = imposto_bruto

    return reducao


print("=== Calculadora de IRPF Mensal 2026 ===")
print("Digite os salários para calcular.")
print("Para sair do programa, digite: sair\n")

while True:
    salario = ler_salario()

    if salario == "sair":
        print("Programa encerrado.")
        break

    if salario is None:
        continue

    imposto_bruto = calcular_imposto_bruto(salario)
    reducao = calcular_reducao(salario, imposto_bruto)
    imposto_final = imposto_bruto - reducao
    salario_liquido = salario - imposto_final

    if salario > 0:
        aliquota_efetiva = (imposto_final / salario) * 100
    else:
        aliquota_efetiva = 0

    print("\n--- Resultado ---")
    print("Salário bruto: ", formatar_real(salario))
    print("Imposto bruto: ", formatar_real(imposto_bruto))
    print("Valor da redução: ", formatar_real(reducao))
    print("Imposto a recolher: ", formatar_real(imposto_final))
    print("Salário líquido: ", formatar_real(salario_liquido))
    print(f"Alíquota efetiva: {aliquota_efetiva:.2f}%")
    print()
