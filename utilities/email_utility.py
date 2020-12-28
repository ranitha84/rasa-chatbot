from threading import Thread
from flask import Flask, render_template
from flask_mail import Mail, Message
import settings

global mail_app
mail_app = Flask(__name__, template_folder='templates')

# configuration of mail
mail_app.config['MAIL_SERVER'] = settings.MAIL_SERVER
mail_app.config['MAIL_PORT'] = settings.MAIL_PORT
mail_app.config['MAIL_USERNAME'] = settings.MAIL_USERNAME
mail_app.config['MAIL_PASSWORD'] = settings.MAIL_PASSWORD
mail_app.config['MAIL_USE_TLS'] = settings.MAIL_USE_TLS
mail_app.config['MAIL_USE_SSL'] = settings.MAIL_USE_SSL

mail = Mail(mail_app)


def send_async_email(app, recipient, response):
    print('Inside email sent')
    try:
        with mail_app.app_context():
            if '<mailto' in recipient:
                recipient = recipient.split("|", 1)[1]
                recipient = recipient.split(">", 1)[0]
            print(recipient)
            msg = Message(subject="Restaurant Details powered by bot", sender=settings.MAIL_USERNAME, recipients=[recipient])
            restaurant_names = response['restaurant_name'].values
            restaurant_photo = response['restaurant_photo'].values
            restaurant_location = response['restaurant_address'].values
            restaurant_url = response['restaurant_url'].values
            restaurant_budget = response['budget_for2people'].values
            restaurant_rating = response['restaurant_rating'].values

            restaurants = []
            for i in range(len(restaurant_names)):
                restaurant = {'name' : restaurant_names[i],
                              'location' : restaurant_location[i],
                               'image': restaurant_photo[i],
                               'url':restaurant_url[i],
                               'budget':restaurant_budget[i],
                               'rating':restaurant_rating[i]
                              }

                restaurants.append(restaurant)
            print(restaurants)
            msg.html = render_template('send_mail.html', len=len(restaurants), restaurants=restaurants)
            mail.send(msg)
    except Exception as e:
        print('error occurred while sending email {}'.format(e))


def send_email(recipient, response):
    thread = Thread(target=send_async_email, args=[mail_app, recipient, response])
    thread.start()
