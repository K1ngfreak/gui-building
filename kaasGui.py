kaas = str(input('Is de kaas geel? '))
if kaas == 'ja':
    gaten = str(input('Zitter er gaten in? '))
    if gaten == 'ja':
        duur = str(input('Is de kaas belachelijk duur? '))
        if duur == 'ja':
            print('Emmenthaler')
        else:
            print('Leerdammer')
    else:
        steen = str(input('Is de kaas hard als steen? '))
        if steen == 'ja':
            print('Pammigiano Reggiano')
        else:
            print('Goudse kaas')
else:
    schimmels = str(input('Heeft de kaas blauwe schimmels? '))
    if schimmels == 'ja':
        korst1 = str(input('Heeft de kaas een korst? '))
        if korst1 == 'ja':
            print('Bleu de Rochbaron')
        else:
            print('Foume d_Ambert')
    else:
        kosrt2 = str(input('Heeft de kaas een korst? '))
        if kosrt2 == 'ja':
            print('Camembert')
        else:
            print('mozzarella')