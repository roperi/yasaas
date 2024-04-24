


https://github.com/roperi/YaSaas/assets/9901508/6579f96b-c39b-438a-af55-c72245c2b4c1


<h1 align="center">YaSaas - Monetize your data</h1>
<h2 align="center">Open-source Django REST Framework + React SaaS Boilerplate</h2>

---

YaSaas is an open-source SaaS boilerplate built on Django REST Framework and React, offering a flexible foundation for entrepreneurs looking to monetize their data. 

With seamless integration of Stripe subscriptions and leveraging Django admin functionalities, YaSaas simplifies the process of selling various data products. Whether it's financial data, market insights, or custom datasets, YaSaas provides a practical starting point for individuals keen on exploring data monetization. 

As an open-source solution, YaSaas is freely available, making it accessible for those who want to kickstart their data-driven ventures.


### Rationale: Or why YaSaas uses Django Admin for end-users

YaSaas leverages Django's robust permission system, utilizing Groups and User permissions for precise data access control. In Django, a Group is a collection of Users, and permissions can be assigned to both Users and Groups. YaSaas utilizes Django admin's intuitive interface to manage these permissions effectively.

Entrepreneurs can create Groups representing different roles or access levels within their application. For example, a "Data Access" Group can be defined. Within this Group, specific permissions related to data access are assigned, ensuring that only authorized users can view or modify sensitive data.

By giving staff privileges to end-users and associating them with relevant Groups, YaSaas provides a flexible and secure way to control access to valuable data. This approach ensures that each user, based on their role or responsibilities, has precisely defined permissions, aligning with the principle of least privilege. This technical foundation empowers entrepreneurs to tailor access controls according to their specific data product offerings.

---

### Hero

![hero](../media/hero.png?raw=true)

### Services

![hero](../media/services.png?raw=true)

### Products

![hero](../media/product.png?raw=true)

### Pricing table 

![hero](../media/pricing-table.png?raw=true)

### About

![hero](../media/about.png?raw=true)

### Contact form
![hero](../media/contact-form.png?raw=true)

---

## Features

* Authentication and authorization: User signup, login, logout, email verification, account management, social login support.
* Subscriptions: Set up plans and collect recurring payments with Stripe Subscriptions. 
* Conditionally include or exclude columns or actions based on the user's group membership
* User login history tracking
* User action tracking (including requests within the admin)
* Emails
* Admin dashboard to edit frontend data
* Contact form 
* Light/dark mode
* And more!


---

## Tech stack 
### Front-end stack 
* React 18
* Typescript 4
* Material UI 5

### Backend stack 
* Django 4 
* Django Rest Framework 3 

### Third-party
* Stripe
* AWS Simple Email Service
* Google Analytics

### Django apps
* django-jazzmin
* django-allauth
* django-auth-style
* dj-user-login-history
* django-easy-audit
* django-cors-headers
---

### Prerequisites

Install the following prerequisites:

1. [Python 3.8, 3.9, 3.10 or 3.11](https://www.python.org/downloads/)
<br> This project uses **Django v4.2.4**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Node.js](https://nodejs.org/en/)
3. [Visual Studio Code](https://code.visualstudio.com/download) (Windows)
---

### Installation

#### Backend

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
cd backend
```
```bash
python -m venv venv
# or
virtualenv -p python3.8 ~/.virtualenvs/YaSaas  #  Example using python3.8.
```

#### 2. Activate the virtual environment

From the **backend** directory, run:

On macOS or Linux:

```bash
source venv/bin/activate
# or 
source ~/.virtualenvs/YaSaas/bin/activate

```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required backend dependencies

From the **backend** directory, run:

```bash
pip install -r requirements.txt
```

#### 4. Run migrations

From the **backend** directory, run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

#### 5. Create an admin user to access the Django Admin interface

From the **backend** directory, run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

#### Frontend

#### 1. Install required frontend dependencies

From the **root** directory, run:

```bash
cd frontend
```
```bash
npm install
```

### Run the application

To run the application, you need to have both the backend and the frontend up and running.

#### 1. Run backend

From the **backend** directory, first copy `.env.example` to `.env` and change the value if you want. It doesn't necessarily matter for local development, but the secret value in production should be a random alphanumeric string with symbols. Once that's configured, run:

```bash
python manage.py runserver
```

#### 2. Run frontend

From the **frontend** directory, run:

```bash
npm start
```

#### 3. View the application

Go to http://localhost:3000/ to view the application.

### Add data to the application

Add data through Django Admin.

Go to http://127.0.0.1:8000/admin to access the Django Admin interface and sign in using the admin credentials.

Note: The Services model has three fields:
1. Title
2. Description
3. Icon <- Use a MaterialUI outlined icon. For instance, if you want to use the MonetizationOnOutlined icon, write down __monetization_on_outlined__. Follow that pattern for any other outlined icon you want to use.    

All outlined MaterialUI icons available see [here](https://mui.com/material-ui/material-icons/?theme=Outlined).

### Customize the application

This section describes how to customize the application. 

#### Changing Section Titles and Subtitles 

#### 1. Products

To modify the title and subtitle of the **Products** section, make changes in the ```frontend/src/components/Products.tsx``` file.

#### 2. Services

To modify the title and subtitle of the **Services** section, make changes in the ```frontend/src/components/Services.tsx``` file.

#### 3. Pricing

To modify the title and subtitle of the **Pricing** section, make changes in the ```frontend/src/components/Pricing.tsx``` file.

#### 4. About

To modify the title and subtitle of the **About** section, make changes in the ```frontend/src/components/About.tsx``` file.

#### 5. Contact

To modify the title and subtitle of the **Contact** section, make changes in the ```frontend/src/components/Contact.tsx``` file.

#### Changing Colors

To modify the colors in the application, make changes in the ```frontend/src/theme/palette.ts``` file.

#### Changing Fonts

To modify the fonts in the application, first, add a new font to the ```frontend/public/index.html``` file, and then make changes in the ```frontend/src/theme/theme.ts``` file.

#### Changing Logo

To modify the logo in the application, make changes in the ```frontend/src/layout/Header.tsx``` and ```frontend/src/layout/Sidebar.tsx``` files.

#### Changing Buttons in the Hero Section

To modify the two buttons in the Hero section, make changes in the ```frontend/src/components/HeroButtons.tsx``` file.


### Configurations 

1. Append to the virtual environment file you created above (either `~/.virtualenvs/YaSaas/bin/activate`, `venv/bin/activate`,  or `venv\scripts\activate`). Make sure to put your own Stripe and AWS keys and don't forget to re-activate the virtual environment once you are done.
```
# ~/.virtualenvs/yasaas/bin/activate


# Django
export DJANGO_SECRET_KEY='YOUR-DJANGO-SECRET-KEY'

# Stripe
export STRIPE_PUBLISHABLE_KEY='YOUR-STRIPE-PUBLISHABLE-KEY'
export STRIPE_SECRET_KEY='YOUR-STRIPE-SECRET-KEY'
export STRIPE_ENDPOINT_SECRET='YOUR-STRIPE-ENDPOINT-SECRET'
export STRIPE_CUSTOMER_PORTAL_LINK=https://billing.stripe.com/p/login/test_YOUR-CUSTOMER-PORTAL-ID
export STRIPE_PRICING_TABLE_ID='YOUR-STRIPE-PRICING-TABLE-ID'

# AWS Email
export AWS_SES_ACCESS_KEY_ID='YOUR-SES-ACCESS-KEY'  # You can also use the AWS access key
export AWS_SES_SECRET_ACCESS_KEY='YOUR-SES-SECRET-ACCESS-KEY'  # You can also use the AWS Secret Key
```
   
2. As for the frontend, create a `.env` file to hold the env variables used by React in the frontend and put the following in it (put your Stripe keys). Save it on the frontend root folder (i.e. `frontend/.env`).
```
# frontend/.env


REACT_APP_BASE_URL=http://localhost:8000/
REACT_APP_SITE_URL=http://localhost:3000/
REACT_APP_SIGNUP_URL=http://localhost:8000/accounts/signup
REACT_APP_SIGNIN_URL=http://localhost:8000/admin
REACT_APP_PUBLISHABLE_KEY='YOUR-STRIPE-PUBLISHABLE-KEY'
REACT_APP_PRICING_TABLE_ID='YOUR-STRIPE-PRICING-TABLE-ID'
```
 
3. Update Google-Analytics references

   Update the following three files located in the frontend folder and put your Google Measurement ID in each of them.
```
# frontend/src/App.tsx
ReactGA.initialize('YOUR-GOOGLE-ANALYTICS-MEASUREMENT-ID');

# frontend/src/index.tsx
ReactGA.initialize('YOUR-GOOGLE-ANALYTICS-MEASUREMENT-ID');
```
 
4. Customise Django Admin with Jazzmin
* Jazzmin spices up the "ugly" Django Admin styles. 
* Some configurations were already applied in YaSaas (see bottom of `backend/settings.py` file). 
* See [Django Jazzmin](https://django-jazzmin.readthedocs.io/) for further customisation.

5. Customising django-allauth
* django-allauth is an integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
* Already installed and working in YaSaas. 
* See [Django All-auth docs](https://docs.allauth.org/en/latest/account/configuration.html) for further customisation.

6. Styling the Django-allauth templates with django-auth-style
* All django-allauth rendered templates will automatically be overridden with styled alternatives.
* Already installed and working in YaSaas. 
* For further customisation see [Django-auth-style](https://github.com/girder/django-auth-style)

7. Update `backend/settings.py` to your liking.
```
# CUSTOM TITLES AND HEADERS
INDEX_TITLE = "Data Dynamo"
SITE_TITLE = "API Portal"
SITE_HEADER = "Data Dynamo API"
```
 
8. Update the title tag in `frontend/public/index.html` to your liking.
``` 
<title>Data Dynamo</title>
```

9. Included in YaSaas is [dj-user-login-history](https://pypi.org/project/dj-user-login-history/) which keeps track of user login history. If you want to change its behaviour check in their [docs](https://pypi.org/project/dj-user-login-history/).

10. Included in YaSaas is [django-easy-audit](https://github.com/soynatan/django-easy-audit) which allows you to keep track of every action taken by your users. Please refer to its [docs](https://github.com/soynatan/django-easy-audit/wiki/Settings) to customise its behaviour.

11. In the `frontend/public/` folder update the favicon.ico and logo.svg with your own ones.

```
# frontend/public/img/logo.svg
# frontend/public/favicon.ico
```



### Stripe Subscriptions Workflow (see video at the top)
1. User clicks on a place-holder pricing table in homepage
2. User gets redirected to a signup page to give email, username and password.
3. User gets redirected to another page holding Stripe's pricing table 
4. User selects a subscription plan 
5. User gets redirected to a Stripe checkout page
6. User pays and gets redirected (and logged-in) to Admin page - Stripe will send an event telling us user has paid successfully, which will grant staff status and give Group permission according to the chosen subscription plan. 
7. User subscription ends - Stripe will send an event telling us the subscription is over and our handler will then revoke user's staff and group permissions.



### Stripe
These guidelines assume you have a Stripe account. If you haven't create one. For development purposes make sure to use the Test Mode whenever you are testing the webhooks, creating test products or a test subscription, getting a test pricing tables, testing clocks, etc. Test Mode has its own set of keys and secret keys; use the "Live Mode" ones only after thoroughly testing and you are ready to go live.

Some useful resources:
* [How to create products and prices](https://support.stripe.com/questions/how-to-create-products-and-prices)
* [Create subscriptions](https://stripe.com/docs/no-code/subscriptions)
* [Embeddable pricing table for SaaS businesses](https://stripe.com/docs/payments/checkout/pricing-table)
* [Use incoming webhooks to get real-time updates](https://stripe.com/docs/webhooks)
* [Test your integration with test clocks](https://stripe.com/docs/billing/testing/test-clocks)

In general, you should first create products, then subscriptions, and then a pricing table.

### Stripe webhooks for local development

Install stripe client (linux)
```
cd ~/opt
wget https://github.com/stripe/stripe-cli/releases/download/v1.18.0/stripe_1.18.0_linux_x86_64.tar.gz
tar -xvf stripe_1.18.0_linux_x86_64.tar.gz 
mv stripe /usr/local/bin
```
  
In order to test the Stripe webhook we need to open up our computer to the external world to listen for Stripe events. In another terminal execute the following:
  
```    
  stripe listen --forward-to localhost:8000/webhook
  ``` 

All the logic related to handling Stripe events is in the `backend/subscriptions/views.py` module. The most basic events are already being handled by YaSaas (like `checkout.session.completed` or `customer.subscription.deleted`). Please feel free to expand the if/else clauses to handle your specific use-cases (there are tons of events!).

### Structure your Stripe subscription plans around Django Groups and User models
This is the most crucial aspect for monetising your data using Django Admin. YaSaas leverages the Django Admin to provide access to end-users as staff members with Group privileges. That way you can group users based on how much data access you want to give them. For instance, a subscription named "Basic Plan" might give a user permission to view a single table. Whereas a subscription named "Premium Level" might give a user permission to view multiple tables.  

Things to consider:

* In Stripe lingo Pricing Tables are made up Products. Say, your Pricing Table "A" contains three products: "Basic Plan", "Advanced Plan" and "Premium Plan". 
* YaSaas gives end-users staff privileges otherwise they won't be able to access Django Admin. End-users will be able to enter the Django Admin interface but they will only be able to view whatever you give them permission to view.  
* __Make sure to name your Django User Groups exactly as your Stripe subscription plan's products__
* For instance, if you name the Product in your plan as "Basic Plan" then your User Group must be named "Basic Plan" too.  
* When configuring your Stripe product's payment settings __make sure to check "Don't show confirmation page" and redirect customers to http://localhost:8000/admin__
* Review the following Subscription webhook view to make sure you understand how Staff and Group permissions are granted to the user after he/she successfully pays:

```
## Excerpt from the stripe_webhook view found in backend/subscriptions/views.py

 product_name = stripe.Product.retrieve(subscription.plan.product).name

 # Add Group to user
 logger.info(f'Adding {user.username} (user #{user.id}) to Group `{product_name}`')
 user.groups.add(Group.objects.get(name=product_name))

 # Add staff status to user
 logger.info(f'Granting {user.username} (user #{user.id}) with staff status')
 user.is_staff = True
 user.save()

```

### Adding your data product to the backend

Once you got the backend and frontend running, you are now ready to add your own Django data product app. 

There is a dataproduct app already set up as you can see in the backend folder. This app was created as a toy example to be featured in the demo video. You could keep it by rewriting the models.py file, or create an entirely new app to hold your data product models.   

If you create a new app do the following:

1. Create new app
```
# stop runserver

cd backend/
python manage.py startapp your_app_name
```

2. Configure the App in settings.py:
Open the settings.py file in your Django project directory and add your app to the INSTALLED_APPS list. Find the INSTALLED_APPS section and add your app's name.
```
INSTALLED_APPS = [
    # ...
    'your_app_name',
]

```

You can now safely disable the dataproducts app by commenting it. 

```
INSTALLED_APPS = [
    # dataproducts,
    'your_app_name',
]

```
2. Create Models

   In your app directory (your_app_name), you'll find various files. The key one is models.py. The urls.py and views.py can be left empty because the backend will take the app as part of its own.


4. Run Migrations:

    After defining your models, run the following commands to apply the initial database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server to see your changes:

`python manage.py runserver`

### Conditionally include or exclude columns from the list_display based on the user's group membership

If you want to conditionally include or exclude columns from the `list_display` based on the user's group membership, you can create a function that generates the list of columns dynamically. Here's an example:

```
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = self.get_dynamic_list_display(request)
        return list_display

    def get_dynamic_list_display(self, request):
        default_list_display = [
            # List of default columns
            'some_column',
            'some_other_column',
            # ... (other columns)
        ]

        additional_columns = []

        # Add additional columns based on the user's group membership
        if request.user.is_superuser:
            # Superusers see all columns
            additional_columns += ['column_for_superusers']
        elif request.user.groups.filter(name='Group1').exists():
            # Users in Group1 see specific columns
            additional_columns += ['column_for_group1']
        elif request.user.groups.filter(name='Group2').exists():
            # Users in Group2 see different columns
            additional_columns += ['column_for_group2']

        # Combine default columns and additional columns
        dynamic_list_display = default_list_display + additional_columns

        return dynamic_list_display

admin.site.register(YourModel, YourModelAdmin)

```


### Conditionally include actions based on the user's group membership

Likewise, if you want to conditionally display actions based on user's group membership you could do modify the `get_actions` method. Example:

```
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import YourModel

class YourModelAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)

        # Conditionally add actions based on the user's group membership
        if request.user.is_superuser or request.user.groups.filter(name='Group1').exists():
            actions['action_for_group1'] = (
                self.action_for_group1,
                'action_for_group1',
                'Message to display'
            )
        return actions

    def action_for_group1(self, modeladmin, request, queryset):
        # Action logic for users in Group1
        pass

    # ... rest of your code ...

admin.site.register(YourModel, YourModelAdmin)

```


### Create Groups and add permissions to each of them

Once you have created your data product app, you can now create Groups based on the product plans created on Stripe. Remember to name your Groups with the same names as your subscription plans. 

Go to Authentication and Authorization in the Admin dashboard, and click on Groups and start creating some. For instance, if you created a Stripe subscription plan named "Basic Plan", create a "Basic Plan" group. In this "Basic Plan" group you add **view** permissions to a "Basic Table".  Apply the same logic when creating other Groups.

### Test the application

Replicate what you see in the video at the top of this page. In another browser or incognito window:
1. Open the site and click on the pricing table to be taken to the SignUp page. 
2. Fill the form with made and hit the register button, this will send an email to the user (you can confirm this by checking the backend's terminal console). 
3. Wait to be redirected to a page with Stripe's pricing table. Click on a plan to be sent to the Customer Portal. 
4. Fill out the payment form with the following card details:
    * Email: The email of the fake user you registered in step 2
    * Card number: 4242 4242 4242 4242 
    * Expiration date: 03/25 (or any date in the future)
    * CVC: 123 (or any other 3 digits)
    * Name on card: Name of the user you registered in step 2
    * Country/Postcode: Whatever you want
5. Click on the Subscribe button and wait to be redirected to the admin dashboard. In the backend's terminal console you should see the user getting granted Staff and Group permissions.
6. Once in the admin dashboard your user should have a restricted view of the dashboard (i.e. User won't be able to see anything but his/her Group models). 


### Stripe Live Mode

Before deploying in production you need to do some work on Stripe:

* Change from Test Mode to Live Mode. 
* Create your products, subscriptions and pricing table.  Don't forget to change the redirect link in your product's payment settings. That is, make sure to check "Don't show confirmation page" and redirect customers to http://api.your-domain-name.com/admin
* __You need to use https for the Stripe webhook__. I'd recommend you LetsEncrypt to enable https in your site. 


### Production Deployment

To deploy you could use Nginx, Gunicorn and Django in tandem. 

#### Update main project's settings

``` 
# backend/backend/settings.py


DEBUG = False

# ...

ALLOWED_HOSTS = [
    'your-domain-name.com',
    'api.your-domain-name.com',
]

# ...

CORS_ALLOWED_ORIGINS = [
    'your-domain-name.com',
    'api.your-domain-name.com',
]

ACCOUNT_LOGOUT_REDIRECT_URL = 'http://your-domain-name.com/'

# ...

CUSTOM_SIGNUP_REDIRECT_URL = 'http://your-domain-name.com/pricing-table/?user_id='

# ...

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # Disable Django's email backend...
EMAIL_BACKEND = 'django_ses.SESBackend'  #  ...and enable AWS SES (if using it)

# ...

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # One year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
```


#### Update environment variables for production use

Update your backend's virtual environment files for production use:

``` 
# ~/.virtualenvs/yasaas/bin/activate 


# Django
export DJANGO_SECRET_KEY='YOUR-DJANGO-SECRET-KEY'

# Stripe
export STRIPE_PUBLISHABLE_KEY='YOUR-STRIPE-PUBLISHABLE-KEY'
export STRIPE_SECRET_KEY='YOUR-STRIPE-SECRET-KEY'
export STRIPE_ENDPOINT_SECRET='YOUR-STRIPE-ENDPOINT-SECRET'
export STRIPE_CUSTOMER_PORTAL_LINK=https://billing.stripe.com/p/login/live_YOUR-CUSTOMER-PORTAL-ID
export STRIPE_PRICING_TABLE_ID='YOUR-STRIPE-PRICING-TABLE-ID'

# AWS Email
export AWS_SES_ACCESS_KEY_ID='YOUR-SES-ACCESS-KEY'  # You can also use the AWS access key
export AWS_SES_SECRET_ACCESS_KEY='YOUR-SES-SECRET-ACCESS-KEY'  # You can also use the AWS Secret Key
```

Update your frontend's env file for production use. Note that so far we have been using the "api" subdomain for the backend server. But you could use __dashboard__ instead of __api__ , or whatever you want, remember that your customer will access his/her data from __https://subdomain-name.domain-name.com/admin__. Whatever subdomain you end up using, just make sure to update whenever you see __api__ in all snippets shown in this document.

```
# frontend/.env


# Add to .env
REACT_APP_BASE_URL=http://api.your-domain-name.com/
REACT_APP_SITE_URL=http://your-domain-name.com/
REACT_APP_SIGNUP_URL=http://api.your-domain-name.com/accounts/signup/
REACT_APP_SIGNIN_URL=http://api.your-domain-name.com/admin/
REACT_APP_PUBLISHABLE_KEY='YOUR-STRIPE-PUBLISHABLE-KEY'
REACT_APP_PRICING_TABLE_ID='YOUR-STRIPE-PRICING-TABLE-ID'
```


#### Build backend

Build backend example:

``` 
cd backend/
python manage.py collectstatic
sudo mkdir -p /var/www/html/yasaas/backend/static
sudo cp -r staticfiles/* /var/www/html/yasaas/backend/static/
```

#### Build frontend

Build frontend example:
``` 
export REACT_APP_BASE_URL=http://localhost:8000/
export REACT_APP_SITE_URL=http://localhost:3000/
export REACT_APP_SIGNUP_URL=http://localhost:8000/accounts/signup
export REACT_APP_SIGNIN_URL=http://localhost:8000/admin
export REACT_APP_PUBLISHABLE_KEY='YOUR-STRIPE-PUBLISHABLE-KEY'
export REACT_APP_PRICING_TABLE_ID='YOUR-STRIPE-PRICING-TABLE-ID'

npm run build 
sudo cp -r build/* /var/www/html/yasaas/frontend/
```

Give the project folder access to the Nginx server: 

`sudo chown www-data:www-data -R /var/www/html/yasaas/`


#### Gunicorn 

In the backend folder there's a `bin` subfolder. In it create a `gunicorn_start_backend.sh` bash script. Update it to fit your needs (i.e. app name, paths and/or username). 

``` 
# backend/bin/gunicorn_start_backend.sh


#!/bin/bash
NAME="my-dataproduct-app"                                  # Name of the application
DJANGODIR=/home/YOUR-USERNAME/yasaas/backend  # App project directory
SOCKFILE=/home/YOUR-USERNAME/yasaas/backend/run/backend.sock  # we will communicte using this unix socket
USER=your-username                                        # the user to run as
GROUP=your-username                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=backend.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=backend.wsgi                     # WSGI module name
TIMEOUT=1800

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/YOUR-USERNAME/.virtualenvs/yasaas/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start Gunicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/YOUR-USERNAME/.virtualenvs/yasaas/bin/gunicorn ${DJANGO_WSGI_MODULE} \
  --name $NAME \
  --workers $NUM_WORKERS \
  --max-requests 50 \
  --max-requests-jitter 10 \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --timeout $TIMEOUT \
  --log-level=debug \
  --log-file=-
```

Make it executable:

`chmod +x bin/gunicorn_start_backend.sh`

Run it 

`bin/gunicorn_start_backend.sh`



#### Nginx setup

Example Nginx configuration file for the backend (note I'm using the 'api' subdomain):

```
# /etc/nginx/sites-available/yasaas__backend



upstream backend_server {
    server unix:///home/your-username/yasaas/backend/run/backend.sock fail_timeout=9000; # for a file socket
}

server {
    server_name api.your-domain-name.com; 
    charset     utf-8;

    client_max_body_size 75M;   # adjust to taste

    access_log /home/your-username/yasaas/backend/log/nginx-access.log combined;
    error_log /home/your-username/yasaas/backend/log/nginx-error.log;

    # Django media
    location /media/  {
        root /var/www/html/yasaas/backend;  # your Django project's media files - amend as required
    }

    location /static/ {
        root /var/www/html/yasaas/backend; # your Django project's static files - amend as required
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_buffering off;
        proxy_pass http://backend_server;
        proxy_read_timeout 1800;
        proxy_connect_timeout 1800;
        proxy_send_timeout 1800;
        send_timeout 1800;
    }

}
```

Example Nginx configuration file for the frontend example:

```
# /etc/nginx/sites-available/yasaas__frontend 


server {
    server_name your-domain-name.com;

    location / {
        root /var/www/html/yasaas/frontend;
        index index.html;  
        try_files $uri $uri/ /index.html;
    }
}
```

Enable both nginx config files

``` 
sudo ln -s /etc/nginx/sites-available/yasaas__backend /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/yasaas__frontend /etc/nginx/sites-enabled/
```
Restart Nginx server

`sudo service nginx restart`

At this point both backend and frontend should be accessible from the browser when you navigate to 

http://api.your-domain.com/admin

http://your-domain.com/ 

---

### TODO
* Adding an email confirmation page

---


### Copyright and licenses
Copyright © 2022 Bob's Programming Academy. MIT License.

Copyright © 2023 Roperi. MIT License.
