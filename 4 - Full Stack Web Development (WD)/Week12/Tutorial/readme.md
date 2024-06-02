# IMPORTANT CHANGES 
### CodeExample2
**controller.js**
- The `_id` is being added to the JWT payload in the `loginUser` function, this will allow us to access the user ID without having to pass it as a param in our request 
- The `getUser` function is using the id in the JWT to get data from the database, we return an object with that includes the user id which will be used in the frontend application to update using the update route that required the :id param

