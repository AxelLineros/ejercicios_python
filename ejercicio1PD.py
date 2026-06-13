CostoCurso  = 180000
CostoCertificado = 12000

def calcular_valores():
    asistencia = float(input("Ingrese la asistencia (0-100): "))
    tramo = input("Ingrese el tramo (A, B, C o D): ")

    DescuentoCurso = 0
    DescuentoCert = 0

    if asistencia >= 90:
        if tramo in ['A', 'B']:
            DescuentoCurso = 24
        elif tramo in ['C', 'D']:
            DescuentoCurso = 16
    elif 75 <= asistencia < 90:
        if tramo in ['A', 'B']:
            DescuentoCurso = 14
        elif tramo in ['C', 'D']:
            DescuentoCurso = 10
    else:
        DescuentoCurso = 0

    if tramo in ['A', 'B']:
        DescuentoCert = 10
        # Regla adicional por asistencia alta
        if asistencia >= 85:
            DescuentoCert += 5

    ValorFinalCurso = CostoCurso * (1 - DescuentoCurso / 100)
    ValorFinalCert = CostoCertificado * (1 - DescuentoCert / 100)

    print(f"Descuento aplicado al curso: {DescuentoCurso}%")
    print(f"Valor final del curso: ${ValorFinalCurso:,.0f}")
    print(f"Descuento aplicado al certificado: {DescuentoCert}%")
    print(f"Valor final del certificado: ${ValorFinalCert:,.0f}")

if __name__ == "__main__":
    calcular_valores()