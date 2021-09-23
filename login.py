#!/usr/bin/env python3
import cgi
import cgitb
import time
import os
import templates
# import Cookies
from secret import username, password

localtime = time.asctime(time.localtime(time.time()))

print("Set-Cookie: lastvisit=" + str(time.time()))
print("Content-Type: text/html\r\n\r\n")
print()
print("<title>Test CGI</title>")
print("<p>Hello World CMPUT 404!</p>")
print()
print(templates.login_page())
# print("\r\n\r\n")

form = cgi.FieldStorage()

form_user = form.getvalue('username')
form_pwd = form.getvalue('password')

if form_user == username and form_pwd == password:
    # print("Set-Cookie: Username= %s" % username)
    # print("Set-Cookie: Password= %s" % password)
    # cookie_string = os.environ.get('HTTP_COOKIE')
    # print("<p><b>Username</b> %s <b>Password</b> %s</p>" % (form_user, form_pwd))
    # print(os.environ.get('HTTP_COOKIE'))
    print(templates.secret_page(form_user, form_pwd))
else:
    print("\r\n\r\n")
    print("<p>Sorry, you have provided invalid credentials.</p>")
# print("<p><b>Username</b> %s <b>Password</b> %s</p>" % (username, pwd))
# print(os.environ)
print()
print()
print("</body>")
print("</html>")

