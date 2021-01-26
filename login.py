import os
import json
import sys
import secret
import templates

print('Content-Type: text/html')
print(f"Set-Cookie: authenticated=username")

print("""
    <!doctype html>
    <html>
    <body>
""")
print(templates.login_page())
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print("<p> POSTED: <pre>")
    
    for line in posted.splitlines():
        print(line)
        username, password = line.split("&")
        username = username.split("=")[1]
        password = password.split("=")[1]
    print("</pre></p>")
    print("""
    </body>
    </html>
    """)
    print(username)
    print(password)
    if username == secret.username and password == secret.password:
        print(templates.secret_page(username,password))
