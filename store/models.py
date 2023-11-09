from django.db import models
# Create your models here.


class Customer(models.Model):
    cust_name = models.CharField(help_text='Имя клиента', max_length=50)
    amount_of_purchases = models.IntegerField(help_text='Сумма покупок', default=0)
    cust_balance = models.IntegerField(help_text='На счету')
    cust_ceiling = models.IntegerField(help_text='Лимит кредита')
    cust_debt = models.IntegerField(help_text='Долг')
    comment = models.TextField(help_text='Комментарий', max_length=1024)

    def __str__(self):
        return self.cust_name

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'


class Products(models.Model):
    prod_name = models.CharField(max_length=255)
    prod_cost = models.IntegerField()
    prod_amount = models.IntegerField()

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'




