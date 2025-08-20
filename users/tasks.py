from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_otp_email(email, code):
    print("Sending...")
    send_mail(
        "Привет новый пользователь",
        f"На держи свой код: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    print("Отправлен")

@shared_task
def send_daily_report():
    print("Идет процесс...")
    pochta = "publicpacan1@gmail.com"
    send_mail(
        "Здравствуйте, вот свежий отчет",
        "сегодня я хорошо поел",
        settings.EMAIL_HOST_USER,
        [pochta],
        fail_silently=False,
    )
    print("Отправлено")