# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    return ' '.join(i[1:] + i[:1] + "ay" if i.isalpha()
                    else i for i in text.split())


print(pig_it('Pig latin is cool'))
# 'igPay atinlay siay oolcay'

print(pig_it('Quis custodiet ipsos custodes ?'))
# 'uisQay ustodietcay psosiay ustodescay ?'
