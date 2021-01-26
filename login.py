#!/usr/bin/env python3

import os
import json
import sys
import secret
import templates
#need to construct html and print at the end because we need to Set-Cookie before html is printed
html = """
        <!doctype html>
        <html>
        <body>
        """
print('Content-Type: text/html')
cookies = os.environ.get("HTTP_COOKIE", 0)

if cookies != "":
    key, val = cookies.split("=")
    cookieUsername, cookiePassword = val.split("&")
    # Code for getting POST data taken from lab 3 tips
    posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
    if posted_bytes:
        posted = sys.stdin.read(int(posted_bytes))
        for line in posted.splitlines():
            username, password = line.split("&")
            username = username.split("=")[1]
            password = password.split("=")[1]
            if username == cookieUsername and password == cookiePassword:
                html += templates.secret_page(username, password)
                html += """
                    </body>
                    </html>
                    """

#if there are no cookies then show login page
else:
    # Code for getting POST data taken from lab 3 tips
    posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
    if posted_bytes:
        posted = sys.stdin.read(int(posted_bytes))
        html += ("<p> POSTED: <pre>")
        for line in posted.splitlines():
            html += line
            html += "</pre></p>"
            username, password = line.split("&")
            username = username.split("=")[1]
            password = password.split("=")[1]
            if username == secret.username and password == secret.password:
                print("Set-Cookie: authenticated=" + username + "&" + password)

    html += templates.login_page()
    html += """
            </body>
            </html>
            """
print(html)