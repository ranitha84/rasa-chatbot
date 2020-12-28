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


