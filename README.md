## Movies & games REST API

## Overview

This API is used to recommend movies and video games. You feed the movies you like and dislike, select images of games you like and dislike, and it returns to you a list of images of the recommended movies and/or games, and their corresponding
amazon links to rent or buy them.

For details about the recommender go to:  
https://github.com/JRigelo/Recommender

Please check the webapp source code at:  
https://github.com/JRigelo/free-time-oracle

And the related website:  
http://recommender.dsoracle.com/  
(Due to a sneaky (Cpython) bug the API and so that the webapp is currently not working)


## Documentation

API strongly based on: [FaceInfo REST API](https://github.com/acu192/faceinfo). Thanks, Ryan!

And powered by Swagger-UI: [Movies and Games REST API Documentation](http://52.207.160.193:5000)

API runs in an AWS (Amazon Web Services) EC2 instance: https://aws.amazon.com/



## Technologies Used

- [python](https://www.python.org/)
- [flask](http://flask.pocoo.org/)
- [flask-swagger](https://github.com/gangverk/flask-swagger)
- [Swagger-UI](https://github.com/swagger-api/swagger-ui)
- [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/) (fla _Swagger Spec_)
    - also see http://editor.swagger.io/ for a playground to help you write Swagger Spec
