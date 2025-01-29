from django.http import HttpResponseRedirect
from django.shortcuts import render

from djangoGraduateApp.forms import *

current_session_client_table = CurrentSessionClient.objects.all()
if not current_session_client_table:
    CurrentSessionClient.objects.all().delete()
    CurrentSessionClient.objects.create(current_session_client='Не клиент')

new_client_reg_table = NewClientReg.objects.all()
if not new_client_reg_table:
    NewClientReg.objects.create(firstname='Базовый пользователь', lastname=True, password=True,
                                password_confirmation=True, email=True, discount=True)

clients_orders_table = ClientsOrders.objects.all()
if not clients_orders_table:
    ClientsOrders.objects.create(client_name='SomeValue', client_email=True,
                                 food_name=True, food_amount=True, food_price=True, food_page_path=True)


# Create your views here.

def check_client():
    for _ in CurrentSessionClient.objects.all():
        if _.current_session_client != 'Не клиент':
            return True
        else:
            return False


def home_page(request):
    if check_client() is True:
        client = True
        return render(request, 'djangoGraduateAppTemplates/home_page.html',
                      {
                          'client': client,
                      })
    return render(request, 'djangoGraduateAppTemplates/home_page.html')


def main_dishes_page(request):
    return render(request, 'djangoGraduateAppTemplates/food_pages/main_dishes_page.html')


def redirect(request):
    return render(request, 'djangoGraduateAppTemplates/redirect.html')


def page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir, food_page_price):
    client = False
    show_food_order_amount = 0
    if check_client() is True:
        client = True
        for i in CurrentSessionClient.objects.all():
            for value in ClientsOrders.objects.filter(client_email=i.current_session_client_email,
                                                      food_name=food_page_name):
                show_food_order_amount += value.food_amount

    if request.method == 'GET':
        return render(request, f'djangoGraduateAppTemplates/{food_page_dir}/{food_page_html}',
                      {
                          'client': client,
                          'show_food_order_amount': show_food_order_amount,
                          'food_page_name': food_page_name,
                      })

    elif 'add_product' in request.POST:
        form = FoodAmount(request.POST)
        if form.is_valid():
            add_product_amount = int(form.cleaned_data['food_order_amount'])
            for current_client in CurrentSessionClient.objects.all():
                if current_client.current_session_client_email not in [i[0] for i in
                                                                       ClientsOrders.objects.values_list(
                                                                           'client_email')]:
                    ClientsOrders.objects.create(client_name=current_client.current_session_client,
                                                 client_email=current_client.current_session_client_email,
                                                 food_name=food_page_name,
                                                 food_amount=add_product_amount, food_price=food_page_price,
                                                 food_page_path=food_page_url)
                    redirect_time = '1.2'
                    redirect_url = food_page_url
                    redirect_message = 'Спасибо за заказ!'

                    return render(request, 'djangoGraduateAppTemplates/redirect.html', {
                        'request': request,
                        'redirect_time': redirect_time,
                        'redirect_url': redirect_url,
                        'redirect_message': redirect_message,
                        'client': client,
                        'show_food_order_amount': show_food_order_amount,
                    })

                else:
                    found_food_name = ClientsOrders.objects.filter(
                        client_email=current_client.current_session_client_email, food_name=food_page_name)
                    if not found_food_name:
                        ClientsOrders.objects.create(client_name=current_client.current_session_client,
                                                     client_email=current_client.current_session_client_email,
                                                     food_name=food_page_name,
                                                     food_amount=add_product_amount, food_price=food_page_price,
                                                     food_page_path=food_page_url)
                        redirect_time = '1.2'
                        redirect_url = food_page_url
                        redirect_message = 'Спасибо за заказ!'

                        return render(request, 'djangoGraduateAppTemplates/redirect.html', {
                            'request': request,
                            'redirect_time': redirect_time,
                            'redirect_url': redirect_url,
                            'redirect_message': redirect_message,
                            'client': client,
                            'show_food_order_amount': show_food_order_amount,
                        })

                    else:
                        new_value = 0
                        for old_value in ClientsOrders.objects.filter(
                                client_email=current_client.current_session_client_email,
                                food_name=food_page_name):
                            new_value += old_value.food_amount
                        new_value += add_product_amount
                        ClientsOrders.objects.filter(client_email=current_client.current_session_client_email,
                                                     food_name=food_page_name).update(food_amount=new_value)

                        redirect_time = '1.2'
                        redirect_url = food_page_url
                        redirect_message = 'Спасибо за заказ!'

                        return render(request, 'djangoGraduateAppTemplates/redirect.html', {
                            'request': request,
                            'redirect_time': redirect_time,
                            'redirect_url': redirect_url,
                            'redirect_message': redirect_message,
                            'client': client,
                            'show_food_order_amount': show_food_order_amount,
                        })

    elif 'remove_product' in request.POST:
        form = FoodAmount(request.POST)
        if form.is_valid():
            remove_product_amount = int(form.cleaned_data['food_order_amount'])
            for current_client in CurrentSessionClient.objects.all():
                new_value = 0
                for old_value in ClientsOrders.objects.filter(
                        client_email=current_client.current_session_client_email,
                        food_name=food_page_name):
                    new_value += old_value.food_amount
                new_value -= remove_product_amount
                if new_value <= 0:
                    null_filter = ClientsOrders.objects.filter(
                        client_email=current_client.current_session_client_email,
                        food_name=food_page_name)
                    null_filter.delete()
                    redirect_time = '1.2'
                    redirect_url = food_page_url
                    redirect_message = 'Позиция убрана из заказа'
                    return render(request, 'djangoGraduateAppTemplates/redirect.html', {
                        'request': request,
                        'redirect_time': redirect_time,
                        'redirect_url': redirect_url,
                        'redirect_message': redirect_message,
                        'client': client,
                        'show_food_order_amount': show_food_order_amount,
                    })
                else:
                    ClientsOrders.objects.filter(client_email=current_client.current_session_client_email,
                                                 food_name=food_page_name).update(food_amount=new_value)
                    redirect_time = '1.2'
                    redirect_url = food_page_url
                    redirect_message = 'Позиция убрана из заказа'
                    return render(request, 'djangoGraduateAppTemplates/redirect.html', {
                        'request': request,
                        'redirect_time': redirect_time,
                        'redirect_url': redirect_url,
                        'redirect_message': redirect_message,
                        'client': client,
                        'show_food_order_amount': show_food_order_amount,
                    })


def dolma_info(request):
    food_page_name = 'Долма'
    food_page_url = '/dolma_info'
    food_page_html = 'dolma_info.html'
    food_page_dir = 'main_dishes_info'
    food_page_price = 375
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def falaf_info(request):
    food_page_name = 'Фалафель'
    food_page_url = '/falaf_info'
    food_page_html = 'falaf_info.html'
    food_page_dir = 'main_dishes_info'
    food_page_price = 205
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def meat_bites_info(request):
    food_page_name = 'Шашлычная тарелка'
    food_page_url = '/meat_bites_info'
    food_page_html = 'meat_bites_info.html'
    food_page_dir = 'main_dishes_info'
    food_page_price = 1300
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def plov_info(request):
    food_page_name = 'Плов'
    food_page_url = '/plov_info'
    food_page_html = 'plov_info.html'
    food_page_dir = 'main_dishes_info'
    food_page_price = 550
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def potato_info(request):
    food_page_name = 'Картофельные оладьи'
    food_page_url = '/potato_info'
    food_page_html = 'potato_info.html'
    food_page_dir = 'main_dishes_info'
    food_page_price = 234
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def ragu_info(request):
    food_page_name = 'Овощное рагу с мясом'
    food_page_url = '/ragu_info'
    food_page_html = 'ragu_info.html'
    food_page_dir = 'main_dishes_info'
    food_page_price = 404
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def pizza_page(request):
    return render(request, 'djangoGraduateAppTemplates/food_pages/pizza_page.html')


def marg_info(request):
    food_page_name = 'Маргарита'
    food_page_url = '/marg_info'
    food_page_html = 'marg_info.html'
    food_page_dir = 'pizza_info'
    food_page_price = 550
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def mush_info(request):
    food_page_name = 'Грибная'
    food_page_url = '/mush_info'
    food_page_html = 'mush_info.html'
    food_page_dir = 'pizza_info'
    food_page_price = 670
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def pep_info(request):
    food_page_name = 'Пепперони'
    food_page_url = '/pep_info'
    food_page_html = 'pep_info.html'
    food_page_dir = 'pizza_info'
    food_page_price = 405
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def sea_info(request):
    food_page_name = 'Морепродукты'
    food_page_url = '/sea_info'
    food_page_html = 'sea_info.html'
    food_page_dir = 'pizza_info'
    food_page_price = 330
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def drinks_page(request):
    return render(request, 'djangoGraduateAppTemplates/food_pages/drinks_page.html')


def cof_info(request):
    food_page_name = 'Кофе'
    food_page_url = '/cof_info'
    food_page_html = 'cof_info.html'
    food_page_dir = 'drinks_info'
    food_page_price = 185
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def ju_info(request):
    food_page_name = 'Сок'
    food_page_url = '/ju_info'
    food_page_html = 'ju_info.html'
    food_page_dir = 'drinks_info'
    food_page_price = 89
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def milksh_info(request):
    food_page_name = 'Милкшейк'
    food_page_url = '/milksh_info'
    food_page_html = 'milksh_info.html'
    food_page_dir = 'drinks_info'
    food_page_price = 105
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def zero_info(request):
    food_page_name = 'Кола зеро'
    food_page_url = '/zero_info'
    food_page_html = 'zero_info.html'
    food_page_dir = 'drinks_info'
    food_page_price = 69
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def desserts_info(request):
    return render(request, 'djangoGraduateAppTemplates/food_pages/desserts_info.html')


def bun_info(request):
    food_page_name = 'Слойка с начинкой'
    food_page_url = '/bun_info'
    food_page_html = 'bun_info.html'
    food_page_dir = 'desserts_info'
    food_page_price = 50
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def cookie_info(request):
    food_page_name = 'Печенье'
    food_page_url = '/cookie_info'
    food_page_html = 'cookie_info.html'
    food_page_dir = 'desserts_info'
    food_page_price = 33
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def ice_info(request):
    food_page_name = 'Мороженое'
    food_page_url = '/ice_info'
    food_page_html = 'ice_info.html'
    food_page_dir = 'desserts_info'
    food_page_price = 66
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def pie_info(request):
    food_page_name = 'Кусочек торта'
    food_page_url = '/pie_info'
    food_page_html = 'pie_info.html'
    food_page_dir = 'desserts_info'
    food_page_price = 87
    page_process_func = page_process(request, food_page_name, food_page_url, food_page_html, food_page_dir,
                                     food_page_price)
    return page_process_func


def registration_page(request):
    if request.method == 'POST':
        form = NewClientRegForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_confirmation']:
                return render(request, 'djangoGraduateAppTemplates/invalid_password_confirmation.html')
            all_clients = NewClientReg.objects.all()
            for i in all_clients:
                if form.cleaned_data['email'] != i.email:
                    pass
                else:
                    return render(request, 'djangoGraduateAppTemplates/email_already_exist.html')
            CurrentSessionClient.objects.all().delete()
            CurrentSessionClient.objects.create(current_session_client=form.cleaned_data['firstname'],
                                                current_session_client_email=form.cleaned_data['email'],
                                                current_session_client_discount=20)
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = NewClientRegForm()
    return render(request, 'djangoGraduateAppTemplates/registration_page.html',
                  {'form': form, })


def login_page(request):
    if request.method == 'POST':
        form = ExistedClientForm(request.POST)
        if form.is_valid():
            existed_users = []
            for j in NewClientReg.objects.all():
                existed_users.append([j.firstname, j.lastname, j.password, j.email])
            check_user = [form.cleaned_data['firstname'], form.cleaned_data['lastname'],
                          form.cleaned_data['password'], form.cleaned_data['email']]
            if check_user in existed_users:
                disc = 0
                for _ in NewClientReg.objects.filter(email=form.cleaned_data['email']):
                    disc += _.discount
                CurrentSessionClient.objects.all().delete()
                CurrentSessionClient.objects.create(current_session_client=form.cleaned_data['firstname'],
                                                    current_session_client_email=form.cleaned_data['email'],
                                                    current_session_client_discount=disc)
                return HttpResponseRedirect("/")
            elif check_user not in existed_users:
                return render(request, 'djangoGraduateAppTemplates/login_error.html')
    else:
        form = ExistedClientForm()
    return render(request, 'djangoGraduateAppTemplates/login_page.html',
                  {'form': form, })


def user_data_page(request):
    if request.method == 'POST':
        CurrentSessionClient.objects.all().delete()
        CurrentSessionClient.objects.create(current_session_client='Не клиент')
        return render(request, 'djangoGraduateAppTemplates/home_page.html')
    return render(request, 'djangoGraduateAppTemplates/user_data_page.html')


def client_orders_page(request):
    food = {}
    total = 0
    discount = 0
    delivery = 0

    for i in CurrentSessionClient.objects.all():
        discount += i.current_session_client_discount
        filter_orders = ClientsOrders.objects.filter(client_email=i.current_session_client_email)
        for j in filter_orders:
            if j.food_name not in food and j.food_amount != 0:
                food[j.food_name] = [j.food_amount, j.food_amount * j.food_price, j.food_page_path]
                total += j.food_amount * j.food_price
    if total < 1500:
        delivery += 450
    total += delivery
    total_discount = (total - (total * (discount / 100)))

    context = {
        'food': food,
        'total': total,
        'discount': discount,
        'total_discount': total_discount,
        'delivery': delivery,
    }

    if 'clean_cart' in request.POST:
        for i in CurrentSessionClient.objects.all():
            filter_orders = ClientsOrders.objects.filter(client_email=i.current_session_client_email)
            filter_orders.delete()
            return HttpResponseRedirect("/user_data_page")
    return render(request, 'djangoGraduateAppTemplates/client_orders_page.html', context)
