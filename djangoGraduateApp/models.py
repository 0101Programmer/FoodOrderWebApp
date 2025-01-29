from django.db import models


# Create your models here.

class NewClientReg(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    password_confirmation = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    discount = models.IntegerField(default=20)

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.password}, {self.password_confirmation}, {self.email}, {self.discount}'


class CurrentSessionClient(models.Model):
    current_session_client = models.CharField(max_length=40, default='Не клиент')
    current_session_client_email = models.CharField(max_length=40, default='No data')
    current_session_client_discount = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.current_session_client}, {self.current_session_client_email}, {self.current_session_client_discount}'


class ClientsOrders(models.Model):
    client_name = models.CharField(default='No data', max_length=40)
    client_email = models.CharField(default='No data', max_length=40)
    food_name = models.CharField(default='No data', max_length=40)
    food_amount = models.IntegerField()
    food_price = models.IntegerField()
    food_page_path = models.CharField(default='No data', max_length=40)

    def __str__(self):
        return f'{self.client_name}, {self.client_email}, {self.food_name}, {self.food_amount}, {self.food_price}'
