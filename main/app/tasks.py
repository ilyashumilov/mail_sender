from celery import shared_task
from django.utils.html import strip_tags
from django.template import loader
from django.core.mail import send_mail

@shared_task()
def email_sender(data):
    html_message = loader.render_to_string(
        'index.html',
        {
            'user_name': data['first_name'],
            'second_name': data['second_name'],
        }
    )
    send_mail(
        'Test',
        strip_tags(html_message),
        'noreply@example.com',
        [data['email']],
        fail_silently=False,
        html_message=html_message
    )