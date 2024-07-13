# PROJECT 2
## TASK 1: SQL Injection
Using SQL injection techniques we need to login as admin.
Type username as 'admin' and any random password like 'xyz'.<br>

![](images/1.1.jpg) <br>

If the query is in the way:

    SELECT * FROM <TABLE> WHERE USERNAME='admin' AND PASSWORD='___'

So in order to login as admin we can try to comment out the rest of the command.<br>

![](images/1.2.jpg)

**USERNAME: admin'--**

## TASK 2: Cookie Manipulation
As the name suggests it is something related to cookies.
Inspect the page and look for the cookies. We can see that there is a 'taskCookie' with value 0.

![](images/2.1.jpg) <br> 

What about changing the value of cookie to 1 and refreshing the page.

![](images/2.2.jpg) <br>

Yayy! We completed it.
## TASK 3: Navigate the Secret Path
We need to get a secet path in order to complete the task.

![](images/3.1.jpg) <br>

Try adding "/secret" in front of the URL. Yeahh it worked.

![](images/3.2.jpg) <br>

Now we need to get the hidden treasure. Try adding "/hidden" in front of the URL. Task completed.

![](images/3.3.jpg) <br>

## TASK 4: Find Me
![](images/4.1.jpg) <br>

First step in any web exploitation challenge is to inspect. Inspect it and there it is, Task completed.

![](images/4.2.jpg) <br>

## TASK 5: Network
As the name suggest we need to look for the networks tab by inspecting the page.

![](images/5.1.jpg) <br>

In the networks tab we can see a different value which looks like encoded in base64.

![](images/5.2.jpg) <br>

Decoding the given value online.

![](images/5.3.jpg) <br>