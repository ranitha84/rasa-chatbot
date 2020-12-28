# Restaurant Chat Bot

## Problem Statement
    An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities.
    The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 

    The bot takes the following inputs from the user:
    - City: Take the input from the customer as a text field. 
    - Cuisine Preference: Take the cuisine preference from the customer. The bot should list out six cuisine categories to choose from
    - Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. 
    
    While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). 
    Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. 
    If the user replies 'yes', the bot should ask for user�s email id and then send it over email. Else, just reply with a 'goodbye' message. 

### Working Example :
    ```
        Your input ->  Hi

        Bot -> Hey, How is it going. How May I help you Today

        Your input ->  find me a restaurant in delhi

        Bot-> What kind of cuisine would you like? 1. Chinese 2. Mexican 3. Italian
        4. American 5. Thai
        6. North Indian

        Your Input -> 2: Italian (Italian)

        Bot -> What is the average budget you are looking for? 
        1. Lesser than Rs. 300 2. Rs. 300 to 700
        3. Greater than 700

        Your Input -> 3: greater than 700 (greater than 700)
        
        -----
        We found the following restaurants for you!!!
        Cafe Lota (rated 4.9) in National Crafts Museum, Gate 2, Bhairon Marg, Pragati Maidan, New Delhi and the average budget for two people 1200
        Indian Accent (rated 4.9) in The Lodhi, Lodhi Road, New Delhi and the average budget for two people 5000
        Sevilla - The Claridges (rated 4.7) in The Claridges, 12, Dr. A.P.J. Abdul Kalam Road, Aurangzeb Road, New Delhi and the average budget for two people 4500
        Diggin (rated 4.5) in 10, Santushti Shopping Complex, Race Course Road, Chanakyapuri, New Delhi and the average budget for two people 1400
        Cafe Wink (rated 4.5) in G-1, Plot 9, Sikka Galaxy, Shreshtha Vihar, Anand Vihar, New Delhi and the average budget for two people 800
        
        Bot-> Would you like the details of the top 10 restaurants on email?

        Your input ->  yes

        Bot -> Please specify the email address to which I can sent the restaurant details

        Your input ->  shyjunair.in@gmail.com
    ```

#### Requirements 
    absl-py==0.10.0
    aio-pika==6.7.1
    aiofiles==0.6.0
    aiohttp==3.6.3
    aiormq==3.3.1
    aniso8601==8.1.0
    APScheduler==3.6.3
    astunparse==1.6.3
    async-generator==1.10
    async-timeout==3.0.1
    attrs==20.2.0
    blinker==1.4
    blis==0.4.1
    boto3==1.16.40
    botocore==1.19.40
    cachetools==4.2.0
    catalogue==1.0.0
    certifi==2020.12.5
    cffi==1.14.4
    chardet==3.0.4
    click==7.1.2
    cloudpickle==1.4.1
    colorama==0.4.4
    colorclass==2.2.0
    coloredlogs==14.3
    colorhash==1.0.3
    cryptography==3.3.1
    cycler==0.10.0
    cymem==2.0.5
    decorator==4.4.2
    dm-tree==0.1.5
    dnspython==1.16.0
    docopt==0.6.2
    en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.2.5/en_core_web_md-2.2.5.tar.gz
    fbmessenger==6.0.0
    Flask==1.1.2
    Flask-Mail==0.9.1
    flask-restx==0.2.0
    future==0.18.2
    gast==0.3.3
    google-auth==1.24.0
    google-auth-oauthlib==0.4.2
    google-pasta==0.2.0
    grpcio==1.34.0
    h11==0.9.0
    h5py==2.10.0
    httpcore==0.11.1
    httplib2==0.18.1
    httptools==0.1.1
    httpx==0.15.4
    humanfriendly==9.1
    idna==2.10
    itsdangerous==1.1.0
    Jinja2==2.11.2
    jmespath==0.10.0
    joblib==0.15.1
    jsonpickle==1.4.2
    jsonschema==3.2.0
    kafka-python==2.0.2
    Keras-Preprocessing==1.1.2
    kiwisolver==1.3.1
    Markdown==3.3.3
    MarkupSafe==1.1.1
    matplotlib==3.3.3
    mattermostwrapper==2.2
    multidict==4.7.6
    murmurhash==1.0.5
    networkx==2.5
    numpy==1.18.5
    oauth2client==4.1.3
    oauthlib==3.1.0
    opt-einsum==3.3.0
    packaging==20.8
    pamqp==2.3.0
    pandas==1.1.5
    Pillow==8.0.1
    plac==1.1.3
    preshed==3.0.5
    prompt-toolkit==2.0.10
    protobuf==3.14.0
    psycopg2-binary==2.8.6
    pyasn1==0.4.8
    pyasn1-modules==0.2.8
    pycparser==2.20
    pydot==1.4.1
    PyJWT==1.7.1
    pykwalify==1.7.0
    pymongo==3.10.1
    pyparsing==2.4.7
    pyreadline==2.1
    pyrsistent==0.17.3
    pyTelegramBotAPI==3.7.4
    python-crfsuite==0.9.7
    python-dateutil==2.8.1
    python-engineio==3.13.2
    python-socketio==4.6.1
    python-telegram-bot==12.8
    pytz==2020.4
    PyYAML==5.3.1
    questionary==1.5.2
    rasa==2.2.2
    rasa-sdk==2.2.0
    redis==3.5.3
    regex==2020.9.27
    requests==2.25.1
    requests-oauthlib==1.3.0
    requests-toolbelt==0.9.1
    rfc3986==1.4.0
    rocketchat-API==1.9.1
    rsa==4.6
    ruamel.yaml==0.16.12
    ruamel.yaml.clib==0.2.2
    s3transfer==0.3.3
    sanic==20.9.0
    Sanic-Cors==0.10.0.post3
    sanic-jwt==1.4.1
    Sanic-Plugins-Framework==0.9.4.post1
    scikit-learn==0.23.2
    scipy==1.5.4
    sentry-sdk==0.19.5
    six==1.15.0
    sklearn-crfsuite==0.3.6
    slackclient==2.9.3
    sniffio==1.2.0
    spacy==2.2.4
    SQLAlchemy==1.3.22
    srsly==1.0.5
    tabulate==0.8.7
    tensorboard==2.4.0
    tensorboard-plugin-wit==1.7.0
    tensorflow==2.3.1
    tensorflow-addons==0.11.2
    tensorflow-estimator==2.3.0
    tensorflow-hub==0.9.0
    tensorflow-probability==0.11.1
    termcolor==1.1.0
    terminaltables==3.1.0
    thinc==7.4.0
    threadpoolctl==2.1.0
    tornado==6.1
    tqdm==4.50.2
    twilio==6.45.4
    typeguard==2.10.0
    tzlocal==2.1
    ujson==3.2.0
    urllib3==1.26.2
    wasabi==0.8.0
    wcwidth==0.2.5
    webexteamssdk==1.6
    websockets==8.1
    Werkzeug==1.0.1
    wincertstore==0.2
    wrapt==1.12.1
    yarl==1.5.1

### Installation

Install the dependencies
```sh
$ pip install -r requirements.txt
```
Install the spacy en library
```sh
$ python -m spacy download en
```

### Training Rasa 
cd to  the folder of this repo

#### Trains both Core and NLU
```sh
$ rasa train
```

#### Training  only NLU
```sh
$ rasa train nlu
```

#### Training  only Core
```sh
$ rasa train core
```

### Running Rasa 
Once training is done, cd to the folder

#### Running action server
```sh
$ rasa run actions
```

#### Running rasa in command line
```sh
$ rasa run shell
```

#### Running rasa in interactive mode
```sh
$ rasa interactive
```


