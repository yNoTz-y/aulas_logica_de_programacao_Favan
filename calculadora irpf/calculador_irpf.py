def parse_valor_entrada(texto):
    texto = texto.strip()

    if not texto:
        raise ValueError("Entrada vazia.")

    if texto.lower() == "sair":
        return "sair"

    texto = texto.replace("R$", "").replace("r$", "").replace(" ", "")

    if "-" in texto:
        raise ValueError("Valores negativos não são permitidos.")

    if texto.count(",") > 1 or texto.count(".") > 1 and "," not in texto:
        pass

    # Regras de normalização:
    # - "5000" -> 5000
    # - "5000,00" -> 5000.00
    # - "5000.00" -> 5000.00
    # - "5.000,00" -> 5000.00
    # - "5,000.00" -> 5000.00
    if "," in texto and "." in texto:
        if texto.rfind(",") > texto.rfind("."):
            # formato brasileiro: 5.000,00
            texto = texto.replace(".", "")
            texto = texto.replace(",", ".")
        else:
            # formato americano: 5,000.00
            texto = texto.replace(",", "")
    elif "," in texto:
        texto = texto.replace(".", "")
        texto = texto.replace(",", ".")
    else:
        partes = texto.split(".")
        if len(partes) > 2:
            # Ex.: 1.234.567 ou 1.234.567,89 já teria entrado no caso acima
            # Aqui tratamos como separador de milhar se todos os grupos após o primeiro tiverem 3 dígitos
            if all(len(p) == 3 for p in partes[1:]):
                texto = "".join(partes)
            else:
                raise ValueError("Formato numérico inválido.")

    try:
        valor = float(texto)
    except ValueError:
        raise ValueError("Digite um número válido.")

    if valor < 0:
        raise ValueError("Valores negativos não são permitidos.")

    return valor


def formatar_real(valor):
    s = f"{valor:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def calcular_imposto_bruto(salario_bruto):
    # Tabela mensal válida a partir de janeiro/2026
    if salario_bruto <= 2428.80:
        aliquota = 0.0
        deducao = 0.0
    elif salario_bruto <= 2826.65:
        aliquota = 0.075
        deducao = 182.16
    elif salario_bruto <= 3751.05:
        aliquota = 0.15
        deducao = 394.16
    elif salario_bruto <= 4664.68:
        aliquota = 0.225
        deducao = 675.49
    else:
        aliquota = 0.275
        deducao = 908.73

    imposto = salario_bruto * aliquota - deducao
    return max(imposto, 0.0), aliquota, deducao


def calcular_reducao(salario_bruto, imposto_bruto):
    # Tabela de redução válida a partir de janeiro/2026
    if salario_bruto <= 5000.00:
        return min(312.89, imposto_bruto)
    elif salario_bruto <= 7350.00:
        reducao = 978.62 - (0.133145 * salario_bruto)
        reducao = max(reducao, 0.0)
        return min(reducao, imposto_bruto)
    else:
        return 0.0


def calcular_irpf_mensal(salario_bruto):
    imposto_bruto, aliquota_nominal, deducao = calcular_imposto_bruto(salario_bruto)
    reducao = calcular_reducao(salario_bruto, imposto_bruto)
    imposto_recolher = max(imposto_bruto - reducao, 0.0)
    salario_liquido = salario_bruto - imposto_recolher
    aliquota_efetiva = (imposto_recolher / salario_bruto * 100) if salario_bruto > 0 else 0.0

    return {
        "salario_bruto": salario_bruto,
        "aliquota_nominal": aliquota_nominal,
        "deducao_faixa": deducao,
        "imposto_bruto": imposto_bruto,
        "reducao": reducao,
        "imposto_recolher": imposto_recolher,
        "salario_liquido": salario_liquido,
        "aliquota_efetiva": aliquota_efetiva,
    }


def exibir_resultado(resultado):
    print("\n--- Resultado do Cálculo ---")
    print(f"Salário bruto:        {formatar_real(resultado['salario_bruto'])}")
    print(f"Imposto bruto:        {formatar_real(resultado['imposto_bruto'])}")
    print(f"Valor da redução:     {formatar_real(resultado['reducao'])}")
    print(f"Imposto a recolher:   {formatar_real(resultado['imposto_recolher'])}")
    print(f"Salário líquido:      {formatar_real(resultado['salario_liquido'])}")
    print(f"Alíquota efetiva:     {resultado['aliquota_efetiva']:.2f}%")
    print("----------------------------\n")


def main():
    print("Calculadora de IRPF Mensal - Vigência a partir de janeiro/2026")
    print("Digite o salário bruto para calcular.")
    print("Aceita formatos como: 5000 | 5.000 | 5000,00 | 5.000,00")
    print("Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Informe o salário bruto: ").strip()

        try:
            valor = parse_valor_entrada(entrada)

            if valor == "sair":
                print("Encerrando o programa.")
                break

            resultado = calcular_irpf_mensal(valor)
            exibir_resultado(resultado)

        except ValueError as e:
            print(f"Entrada inválida: {e}\n")


if __name__ == "__main__":
    main()