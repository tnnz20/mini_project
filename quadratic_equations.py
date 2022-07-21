def formulas(a, b, c):
    """
    Nature of roots:
    D > 0, roots are real and distinct (unequal)
    D = 0, roots are real and equal (coincident)
    D < 0, roots are imaginary and unequal
    """
    a, b, c = int(a), int(b), int(c)

    if a > 0:
        # Calculate discriminant
        d = (b**2) - 4*a*c
        val_sqrt = d**(1/2)

        # Check Condition discriminant
        if d > 0:
            formula_plus = (-b + val_sqrt) / (2 * a)
            formula_min = (-b - val_sqrt) / (2 * a)

            print('roots are real and distinct (unequal)')
            print(f'+ result = {formula_plus}')
            print(f'- result = {formula_min}')

        elif d == 0:
            print('roots are real and equal (coincident)')
            print(f'result = {-b /(2 * a)}')
        
        else:
            print('roots are imaginary and unequal')
            print(- b / (2 * a), " + i", val_sqrt) 
            print(- b / (2 * a), " - i", val_sqrt)
    else:
        raise ValueError('VALUE A MUST BE > 0') 