# 

##                               facebook_comments_analysis 

A REST API based applications with following salient features:

### [Frontend](https://github.com/adarsh2104/facebook_comments_analysis/tree/main/frontend-app): React.JS 


1. Home Page:
  * A Form where the user can specify the keyword and start the search.
  * Previous search keywords are shown as search suggestions.

<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/facebook_comments_analysis/blob/main/Visuals/01.Home_page.png"></img></p>

2.Query Search:
  * Added a loader componenst to show processing request [react-loader](https://www.npmjs.com/package/react-loader)
<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/facebook_comments_analysis/blob/main/Visuals/02.Send_query_request.png"></img></p>

3.Results Page:
  * Comments arranged in tabular format with percentage of sentiment scores.
  * Cummalative sentiment is dispalayed along with the search term.

<p align="center"><img width="100%" height="700px" src="https://github.com/adarsh2104/facebook_comments_analysis/blob/main/Visuals/03.Results_page.png"></img></p>


### [Backend](https://github.com/adarsh2104/facebook_comments_analysis/tree/main/request_client): Python + Djnago REST + Django REST

4.[Views](https://github.com/adarsh2104/facebook_comments_analysis/blob/main/request_client/views.py):
 * Class Based API Views for GET and POST requests.
 * Model Serializers for serializing/deserializing objects of PostComment and SearchKeyword Models.

5.[Models](https://github.com/adarsh2104/facebook_comments_analysis/blob/main/request_client/models.py):
 * Models for saving Search Keywords and PostComments
 * Implemented Foreign Key relation between the models.
6.[Utils](https://github.com/adarsh2104/facebook_comments_analysis/tree/main/request_client/utils):
 * Selenium based request client for collecting comments from Facebook posts and getting matching results
 * Text analyzer implemented using [NTLK package](https://www.nltk.org/)




