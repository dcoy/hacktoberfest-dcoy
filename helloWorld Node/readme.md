This example assumes that you have node installed already.

If you need to confirm run the following:
    
    node --version

If node is installed you will see something like the fllowing:

    v.4.2.6

Follow the [installation](https://nodejs.org/en/download/) instructions for your system if you do not have node installed.

---

Now that you have node installed you should be ready to go.

First create a .js file for your Node application, in your favorite editor.  Let's call it 'helloNode.js'

Inside helloNode.js we will use the **require** directive to load the necessary node modules that we will need.  In this case the **http** module and store the returned instance in a variable as follows:
    var http = require("http");

Next use the *http* variable that was just created and call **http.createServer()**.  This method is used to create a server instance which we will bind to pot 8080, using the **listen** method.  We will pass a function into *createServer* thta will take in a *request* and *response* parameter.  Use the *response* object passed in to write out the *Hello World* message:

    http.createServer(function (request, response) {
    // Send the HTTP header
    // HTTP Status: 200 : OK
    // Content Type: text/plain
    response.writeHead(200, {'Content-Type':   'text/plain'});

    // Send the response body as "Hello World"
    response.end('Hello World\n');
    }).listen(8080);

    // Console will print the message
    console.log('Server running at http://localhost:8080/');

Save helloNode.js.  Open a command prompt or terminal window and navigate to the directory where helloNode.js is saved

At the prompt run:
     
     node helloNode.js

You should see the following:
    
    Server running at http://localhost:8080/

Open a browser and go to the address, where you should see your node app running
