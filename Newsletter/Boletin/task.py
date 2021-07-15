from Newsletter.celery import app
from django.core.mail import send_mail

@app.task(name='boletin-email-task')
def boletin_email(correo):
    print('se manda correo')
    send_mail(
        subject='Nuevo boletin',
        message='un nuevo boletin se ha creado, puedes revisarlo en (aqui agregar alguna url)',
        from_email='sistema@gmail.com',
        recipient_list=[correo],
        fail_silently=False
    )