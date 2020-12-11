# flask-devops-aws

This is a source code of the Udemy course "Python REST APIs with Flask, Docker, MongoDB, and AWS DevOps". 
Learn Python coding with RESTful API's using the Flask framework. Understand how to use MongoDB, Docker and Tensor flow.

link of Udemy course: https://www.udemy.com/course/python-rest-apis-with-flask-docker-mongodb-and-aws-devops/

Credit : El Farouk Yasser, Tim Buchalka's Learn Programming Academy

### 03-Template-Basics

Flask automatically look for HTML templates in the  `Template` directory.   

We can render templates simply by importing the 
`render_template` function from flask and return an `.html` file to the client. 

Flask passes a set of variable (e.g., `{{some variable}}`) to the HTML pages.


We want  a way to be able to use Python code in our application, 
changing and updating variables and logic and then send that information to the template. 

We can use the Jinja template engine to do this. Jinja templating lets us directly insert variable from our python code to the HTML file.

### flask-structure

This folder describes a structure to follow

Credit:

Blog: https://pythonise.com/series/learning-flask/flask-application-structure
Video: https://www.youtube.com/watch?v=-BC3V1CUKpU&list=PLF2JzgCW6-YY_TZCmBrbOpgx5pSNBD0_L&index=2
