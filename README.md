# TLN Stock Predictor
Overview of the project:- The team implemented a website, using Vue. The website prompts them with options for various possible stock predictions. The user specifies the date and company they would like the stock prediction for, then the backend takes this information to go forth and calculate the stock value for that given day. All stock predictions are made by accessing data stored on Alpha Vantage and by accessing recent tweets that are being posted about a company whether they are primarily positive or negative. This is relayed back to the front end and displayed to the user. 

Project for CS 6375 (Spring19) at The University of Texas at Dallas. 

## Project team: 
* Tanushri Singh (TTS150030)
* Lawrence Evangelista (LCE160130)
* Nickolas Ramos (NOR140030)

## Installation
Ensure that Python, npm, and flask is installed.
In order to run this project you need to install the following libraries: numpy, scikit-learn, tweepy, textblob, matplotlib. The following build setup was done through a linux terminal. 

## Build Setup

For the setup, download the zip and navigate into the Front End/ folder, and run the following command:

``` bash
# install dependencies
npm install
```
Once all the dependencies are built, you can build the template via:
``` bash
# build for production with minification
npm run build
```
Once the template is built, navigate to the folder that contains the 'r' file, and simply run the file:

``` bash
# run the file
./r
```
This will run the flask server and it will instruct you to navigate to an address in your browser.
Have fun!

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
## Running
