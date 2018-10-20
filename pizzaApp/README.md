![Stack Builders](https://github.com/stackbuilders/nano-chat/raw/master/sb.png)

# Description

This folder contains the front-end part of the exercice. You have to develop the backend services and replace the endpoints in the JS files with your own.

For each HTML file there are a JS file with same name in the `js` folder, which makes the HTTP requests to the backend.

Search for comments like the one below in the JS files to find where to replace them with your service endpoints.

```javascript
/**
 * ****************************
 * Please change '/pizza' with
 * your service endpoint below
 * ****************************
 */
```

## Json

In the `json` folder there are some data JSON examples of the data that the server could send to the client.

  1. [create-order.json](templates/json/create-order.json) Create a pizza order 
  2. [order.json](templates/json/order.json) Individual order
  3. [orders.json](templates/json/orders.json) List of orders
  4. [statistic.json](templates/json/statistics.json) Statistics from orders 

## Installation

If you need a static server to check the HTML templates you could use [lite-server](https://github.com/johnpapa/lite-server) that we configured for you. 

Instructions to install and run the server:

You will need [Node](https://nodejs.org/en/) and [NPM](https://www.npmjs.com/). Instructions to install in [Windows](https://treehouse.github.io/installation-guides/windows/node-windows.html) and [Linux/Mac](https://nodesource.com/blog/installing-node-js-tutorial-using-nvm-on-mac-os-x-and-ubuntu/). 

  1. `cd templates`
  2. `npm install` or `yarn install`
  3. `npm start`

Open `http://localhost:3000` in your browser to try out.
