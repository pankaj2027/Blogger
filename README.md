# Step for setup of the Blogger project.

Step 1. Install python(V3.9), django(V3.1.6) and djnago restframework(V3.12.2).
        
        pip install djangorestframework

Step 2. Update your SECRET_KEY in config.py file.
       
       By default it has sqlite3 but you want to use Mysql or anyother database, then remove sqlite3 config settings from setting.py file and update the                  
        required server configuration in Config.py file as eg given for mysql in comments
        
Step 3. Now, we are done with the pre-requisites. Run the migration command to create the schema of the table by the commands given below.
        
        1. python3 manage.py makemigrations
        2. python3 manage.py migrate
       

Step 4. Create super User:
       
       1. python3 manage.py createsuperuser
        
Step 5. Run the server.
        
        python3 manage.py runserver
        
Step 6. Register the blogeer by using author_registation API via POSTMAN or django server.
       request POST : http://127.0.0.1:8000/registration/
       
       Example request body given below,update the content in <> with the real content
       BODY :   {
                  "username":"<blogger_username>",
                  "email": "<blogger@xyz.com>",
                  "first_name": "<blogger_firstname>",
                  "last_name": "<blogger_lastname>",
                  "password": "<choose your password>"
              }
              
        After the successful registration, you will be receving the response  as below   
        
        Response: Your registration has been completed Successfully!!
        
    
Step 7. Blogger can add the blog by using Blogdetail APIs:-
        request POST:-http://127.0.0.1:8000/blogdetail/
        
        Example request body given below,update the content in <> with the real content and  provide the admin credential in Authorisation (**Use basic Auth** )
        
        Body :- {
                   "title": "<blog_title>",
                   "sub_title": "<blog_subtitle>",
                   "body": "<Blog_body>"          
                  }
                  
         you will receive response
         
         Example as given below,
        Response:{
                      "msg": "Your Blog Has Been Added Successfully!!"
                  }
                  
         Blogger Can update the blog by using Blogdetail APIs
         request put:-http://127.0.0.1:8000/blogdetail/<blog_id>
         
         
         Blogger Can Delete the blog by using Blogdetail APIs
         request Delete:-http://127.0.0.1:8000/blogdetail/<blog_id>
         
                
step 8. Visitor can add the comment on  Blog by using AddComment APIs:
        request POST:-http://127.0.0.1:8000/addcomment/
        
        Body :- {
                   "blog": <blog_id>,
                   "visitor_firstName": "<visitor_firstname>",
                   "visitor_lastName": "<visitor_lastname>",
                   "comment":"<visitor_comment>" 
                   }
                   
        you will receive response
         
         Example as given below,
        Response:{
                      "msg":"Your comment has been added Successfully!!""
                  }       
                   
         
                              
  Step 9. Blogger can Approve or Reject the comment by using CommentApproveReject APIs:
         request get:-http://127.0.0.1:8000/addcomment/
         
         Example request body given below,update the content in <> with the real content and  provide the admin credential in Authorisation (**Use basic Auth** )
         
         
         Blogger get in response blog comment by the visitor
         Example:
         Response: {
                        "id": <comment_id>,
                        "blog": "<blog_title>",
                        "visitor_firstName": "<visitor_firstname>",
                        "visitor_lastName": "<visitor_lastname>",
                        "comment": "<vistor_comment_on blog>",
                        "status": "Inproces"
                    }
                    
       Now , Vistor can APPROVE or reject the comment by using CommentApproveReject API's
       request put:-http://127.0.0.1:8000/addcomment/<comment_id>
       Body:- { 
                  "status": "<Approve/Reject>"
              }

        
        
  Step 10. Blog  can display with comments by using viewblogwithcomment APIs
  
            request get:-http://127.0.0.1:8000/viewblogwithcomment/
            
            In Response : List of blog with Approve comment
            
            Example:-
                  {
                        "title": "<blog_title>",
                       "sub_title": "<blog_subtitle>",
                       "body": "<Blog_body>"  
                        "comments": [
                            {
                                "blog": <Blog_id>,
                                "visitor_firstName": "<Visitor_name>",
                                "visitor_lastName": "<visitor latsname>",
                                "comment": "<Visitor comment>"
                            }
                        ]
                    }
         
   
   
   
   
   Thankyou
