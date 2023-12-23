from django.shortcuts import render, redirect
from apps.contact.models import Contact
from apps.base.models import Settings, Base
from apps.telegram.views import get_text


# Create your views here.
def contact(request):
    title = "Контакты"
    contact = Contact.objects.latest('id')
    settings = Settings.objects.latest('id')
    base = Base.objects.latest('id')

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        name_company = request.POST.get('name_company')
        number_email = request.POST.get('number_email')

        # Do not save the Contact object to the database
        # Comment or remove the following line
        # Contact.objects.create(firstname=firstname, name_company=name_company, number_email=number_email)

        get_text(f""" 
Оставлено заявка на партнерство! 
                 
Имя пользователя:  {firstname}
Название компании:  {name_company}
Адрес(email/телефона):  {number_email}
        """)
        return redirect('index')

    return render(request, "contact.html", locals())