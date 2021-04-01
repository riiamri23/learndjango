//membuat project django
django-admin startproject firstdjango

//menjalankan server
python manage.py runserver 10.4.68.72:7000

//menjalankan migrate (untuk fill database)
python manage.py migrate

//membuat superuser di admin
python manage.py createsuperuser

//membuat konten di django
python manage.py startapp products
python manage.py startapp blog
python manage.py startapp profiles
python manage.py startapp cart


//mengatur models

/************** Create Product Objects in the Python Shell ***************/
python manage.py shell
from products.models import Product
Product.objects.all()
Product.objects.create(title='New product 2', description="another one", price="1000", summary="hello")


/************** New Model Field ***************/
references https://docs.djangoproject.com/en/3.1/ref/models/fields/#model-field-types 


/************** Change a Model ***************/
boolean harus mempunyai default value


/************** Default Homepage to Custom Homepage ***************/
check files:
    - products/view.py


/************** URL Routing and Requests ***************/
def contactView(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")

def aboutView(*args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")

def socialView(*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

    
/************** Django templates***************/


/************** Django templating Engine Basics ***************/
check files:
    - templates/home.html
    - templates/base.html

    
/************** Include Template Tag ***************/
{% include 'navbar.html' %}


/************** Rendering Context in a Template ***************/
my_context = {
    "my_text": "this is about us",
    "my_number": 123,
    "my_list": [123, 4323, 12313]
}
<p>{{ my_text }}, {{ my_number }}</p>


/************** For Loop in a Template ***************/
<ul>
{% for my_item in my_list %}
    <li>{{ forloop.counter }} - {{ my_item }}</li>
{% endfor %}
</ul>


/************** Using Conditions in a Template ***************/
<ul>
{% for my_item in my_list %}
    {% if my_item == 123 %}
        <li>{{ forloop.counter }} - {{ my_item|add:22 }}</li>
    {% elif my_item == 'testing' %}
            <li>This is not an integer</li>
    {% else %}
        <li>{{ forloop.counter }} - {{ my_item }}</li>
    {% endif %}

{% endfor %}
</ul>

/************** Template Tags and Filters ***************/
references: https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

/************** Render Data from the Database with a Model ***************/


/************** How Django Templates Load with Apps ***************/

/************** Raw HTML Form ***************/
