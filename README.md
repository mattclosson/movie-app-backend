# Movie App

A movie review app where users can review movies on a 1-5 star system, follow other users, and have a list of movies they've reviewed.

## Models

User: name, email, password, hasmany(review)

Movie: title, description, hasmany(review)

Review: stars, title, body, hasone(user, movie)

## Routes

| Route         | Description   | 
| ------------- | -------------:| 
| /      | Posting a new review |
| /      | Getting all reviews |
| /[id] | Updating a review |
| /[id] | Deleting a review |
| /user      | Getting all users |
| /user/[id] | Updating a user |
| /user/[id] | Deleting a user |
| /user/login | Logging in a user |
| /user/signup | Signing up a user |
| /user/logout | Logging out a user |
| /user/token | Retrieve JWT token |
