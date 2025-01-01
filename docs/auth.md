### Authentication and Authorization

Authentication:
--------------
The process of validating user is called authentication.
- username and pwd combination
- token


Drf Provides servers inbuilt authentication mechanisms

1. Basic Authentication
2. session authentication
3. token authentication
4. JWT (Json Web Token) Authentication etc

Authorization:
--------------

Valid customer of ICIC Bank
- How much balance amitaab buschan has?
 - You have no authorization to access that information, access person to access that resource

The process of validating access permissions of user
- After authentication, We have to perform authorization

DRF provide permission-classed

- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly
- DjangoModelPermissions
- DjangoModelPermissionsOrAnonReadOnly

READ Operation: GET, OPTIONS, HEAD => SAFE METHOD
Write Operations: POST, PUT, PATCH => 

Token Authentication:
---------------------
Authentication can be performed by some token 

native desktop clients,mobile clients

Token must be generated for every user
Token must be validated for every user

authtoken application => inbuilt application provided by DRF

1. include authtoken application in our installed application list
2. Token table
3. migrate commanded needed
4. url pattern of authtoken 

http
1. authtoken application can validate this username and pwd
2. authtoken application will check whether the Token is already generated for this user or not
3. If a token is already generated for this user, then the existing token will be returned.
4. If token is not already genrated, then a new token willl be created and stored in tokens table and send token as the response

How to enable Authntication and Authorization(permission) for our view class/vendor

- Globally inside setting.py file
- locally




