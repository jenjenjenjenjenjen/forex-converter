### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
Important differences between Python and Javascript include JS being used on the front end, and Python mainly being used on the back end of applications. Python uses a class-based inheritance model, while JS uses a prototype-based inheritance model.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  Two ways to try to get a missing key from a dictionary without your application crashing are:
  - Using the get() method and entering the missing key and a default value
  - The setdefault() method would also work similarly, when searching for a key that doesn't exist it will automatically assign that key to the default

- What is a unit test?  
 A unit test tests a single function or method of your application

- What is an integration test?  
  An integration test tests the functionality of an entire section of code that all works together

- What is the role of web application framework, like Flask?  
  The rold of a web application framework is to help you write clearer and more concise code, makes the development process easier, and makes debugging and maintainence easier.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
  You can determine which one is a better fit for your application depending on whether there is sensitive client information involved, if you'd like to store and access the data in the URL, or if you want the user to be able to manipulate the data that comes back via the URL

- How do you collect data from a URL placeholder parameter using Flask?  
To collect data from a URL placeholder parameter using Flask, you can add a variable to your route using <>.

- How do you collect data from the query string using Flask?  
 To collect data from the query string using Flask, you can use request.args.

- How do you collect data from the body of the request using Flask?  
To collect data from the body of the request using Flask, you can use request.data.

- What is a cookie and what kinds of things are they commonly used for?  
A cookie is a small amount of data that is collected by the browser and commonly used for the server to remember information about your visit and make the website easier to use when you revisit it. 

- What is the session object in Flask?  
 The session object in Flask is used to track session data from the browser.

- What does Flask's `jsonify()` do?  
jsonify() will turn Flask content into JSON content.
