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
