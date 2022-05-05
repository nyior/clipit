<h1 align="center">
	Clipit: A web url shortener with an accompanying browser extension.
</h1>

<p align="center">
	<i>
        shorten your urls for free through our web 
        interface or just install our browser extension
    </i>
</p>

<p align="center">
  <img width="150" height="150" src="./frontend/src/assets/clipit-logo.png">
</p>


## what is clipit ?
Simple! Have you worked with Bitly or Tinyurl before? Clipit 
does pretty much the same thing *and more*. It is a web application
with an accompanying browser extension that allows
you create shorter versions of those overly long smelly urls :) 
you want to share with other people. You know what? Clipit 
also comes with a [free API](http://shter.herokuapp.com/) that you could easily integrate into your projects :sparkles:

[Chrome Extension](https://chrome.google.com/webstore/detail/clipit/jbeoijelmjlhahfdlccjlemcnfegiolc) || [Edge Extension](https://microsoftedge.microsoft.com/addons/detail/clipit/hiomcmjcakkkkkknkcmkagdcnhpfjhbl)

See a quick demo of how the browser extension works [HERE](https://www.youtube.com/watch?v=n1TEdz0t5es)


## Lol Nyior what's the browser extension for? aren't you over engineering?
No not really! the browser extension would allow 
you shorten urls easily without having to visit our web platform 
or many more like it each time you want to create a short url. 
It makes shortening urls more convenient

If you like this repo, click the :star:

## what can clipit be used for?
Nyior, isn't that what you just explained in the paragraph above? 
Well yeah, but I want to be more specific. Here are the things you could 
do with clipit.

- you could submit a long URL and get an auto generated shortened version of that url
- as a user, sometimes you'd want to customize the short URL so that you could recall what URL it is referencing or give it a cool name. clipit allows you to do that too. Just submit the long url along with a custom short url you'd want the system to use.
- clipit allows you retrieve a list of all the urls you had shortened in the past
- lastly, shortster also allows you see a report of your short URLs, when it was created, how many times it was clicked, and the last time it was accessed.


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

to run the backend's test cases run the command below in the backend directory(this command should always be ran after the virtual environment has been activated. Refer to the steps above

```
manage.py test

```

to spin up the backend's local development server, run the command below(again in the backend directory and after the virtual environment has been activated)

```
manage.py runserver

```

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

## Chrome Extension Setup(web-extension folder): 

- To test if it works, visit ```chrome://extensions``` in your browser and ensure that the Developer mode checkbox in the top right-hand corner is checked.

- Click Load unpacked extension and select the directory in which your extension files live(basically, this project's folder). If the extension is valid, it will be active straight away so you can click on the extension's icon in your browser's address bar; this action should trigger a display of a pop up icon.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Website
you could shorten your urls with clipit [here](https://clipit.fun)


find the documentation for our free API [here](https://shter.herokuapp.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)
