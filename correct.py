# Соблюдение DIP: OrderProcessor и сервисы отправки зависят от абстракции NotificationSender

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass


class EmailNotificationSender(NotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] Отправка письма на {recipient}: {message}")


class SmsNotificationSender(NotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] Отправка сообщения на {recipient}: {message}")


class MessengerNotificationSender(NotificationSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Messenger] Отправка сообщения в мессенджер {recipient}: {message}")


class OrderProcessor:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self._notification_sender = notification_sender

    def process_order(self, order_id: str, recipient: str) -> None:
        print(f"Обработка заказа {order_id}...")
        message = f"Ваш заказ #{order_id} был успешно обработан."
        self._notification_sender.send(recipient, message)


if __name__ == "__main__":
    email_service = EmailNotificationSender()
    processor_with_email = OrderProcessor(email_service)
    processor_with_email.process_order("12345", "customer@example.com")

    sms_service = SmsNotificationSender()
    processor_with_sms = OrderProcessor(sms_service)
    processor_with_sms.process_order("12345", "+79991234567")

    messenger_service = MessengerNotificationSender()
    processor_with_messenger = OrderProcessor(messenger_service)
    processor_with_messenger.process_order("12345", "customer_profile")
