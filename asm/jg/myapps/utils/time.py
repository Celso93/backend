from datetime import datetime

def msg_saudacao():
    hora_atual = datetime.now().hour
    if 0 <= hora_atual < 12:
        # maneira de verificar valor entre valores
        texto = 'Bom dia'
    elif 12 <=  hora_atual < 18:
        texto = 'Boa tarde'
    else:
        texto = 'Boa noite'
    return texto
