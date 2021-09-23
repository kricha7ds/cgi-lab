#!/usr/bin/env python3
import os
import json
import time
import templates

# print("Set-Cookie: UserID = XYZ;\r\n")
# print("Set-Cookie:Password = XYZ123;\r\n")
# print("Set-Cookie:Expires = ")
# print("Set-Cookie:Domain = ")
print("Set-Cookie: lastvisit=" + str(time.time()))
print("Content-Type: text/html\r\n\r\n")
print
print("<title>Test CGI</title>")
print("<p>Hello World CMPUT 404!</p>")


print(templates.login_page())
# print(os.environ)
# json_object = json.dumps(dict(os.environ), indent = 4)