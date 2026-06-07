# Нарушение DIP: OrderProcessor напрямую зависит от конкретного класса EmailSender

class EmailSender:
    def send_email(self, to: str, subject: str, body: str) -> None:
        print(f"Отправка Email на {to}: [{subject}] {body}")


class OrderProcessor:
    def __init__(self) -> None:
        self._email_sender = EmailSender()

    def process_order(self, order_id: str, customer_email: str) -> None:
        print(f"Обработка заказа {order_id}...")
        self._email_sender.send_email(
            customer_email,
            "Заказ успешно оформлен",
            f"Ваш заказ #{order_id} был успешно обработан."
        )


if __name__ == "__main__":
    processor = OrderProcessor()
    processor.process_order("12345", "customer@example.com")
