from Newsletter.celery import app
from django.core.mail import send_mail

@app.task(name='users-email-task')
def users_email(correo):
    print('se manda correo')
    send_mail(
        subject='Nuevo Usuario',
        message='Se ha agregado un nuevo usuario a nuestro sistema',
        from_email='sistema@gmail.com',
        recipient_list=[correo],
        fail_silently=False
    )