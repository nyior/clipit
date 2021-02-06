<h1 align="center">
	Shortster: A url shortner for the web
</h1>

<p align="center">
	<i>web application for creating short urls</i>
</p>


## what is shortster ?
Simple! Have you worked with bitly or tinyurl before? shortster 
does pretty much the same thing. It is a web application that allows
you create shorter versions of those overly long smelly urls :) you want to share
with other people. You know what? shortster is completely free ðŸ˜ƒ

If you like this repo, click the â­

## what can shortster be used for?
lol Nyior isn't that what you just explained in the paragraph above? 
Well yeah, but I want to be more specific. Here are the things you could 
do with shortster.

- you could submit a long URL and get an auto generated shortened version of that url
- as a user, sometimes you'd want to customize the short URL so that you could recall what URL it is referencing or give it a cool name. Shortster allows you to do that too. Just submit the long url along with a custom short url you'd want the system to use.
- shortster allows you retrieve a list of all the urls you had shortened in the past
- lastly, shortster also allows you see a report of your short URLs, when it was created it, and how many times it was clicked, and the last time it was accessed.


## Backend Project Setup(backend folder): 

* clone project to your local machine
* navigate to the project's backend directory
* Then create a virtual environemnt and install all the project dependencies in the pipfile using the command :

```
pipenv install

```
If the command above throws an error, then you most likely do not have pipenv installed. In that case use the command below to install pipenv.

```
pip install pipenv

```

Upon completion run the first command again

Don't know what virtual environments are or how to create virtual environments with pipenv?
Don't worry, we got you! learn about python virtual environments and pipenv [here](https://docs.python-guide.org/dev/virtualenvs/#:~:text=virtualenv%20is%20a%20tool%20to,standalone%2C%20in%20place%20of%20Pipenv.)


**Note** that this project was made with Python 3.7.0, other Python versions weren't tested with this project. It is strongly advised that you work with the Python version that was used for this project. Other Python 3 versions too might work tho.
Don't have Python 3 installed? Get it [here](https://www.python.org/downloads/)


## Frontend Project setup

Navigate into the frontend folder

### installs all project dependencies
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Website
you could shorten your urls with shortster [here](https://shter.netlify.app/)


find the documentation for the API backend [here](https://shter.herokuapp.com/docs)
**Note** that even though the ``` /<shortcode> ``` endpoint for handling the redirect
isn't on the documentation page, it works perfectly.


## License
[MIT](https://choosealicense.com/licenses/mit/)
