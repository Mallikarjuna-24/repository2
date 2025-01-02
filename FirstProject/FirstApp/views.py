from django.shortcuts import render
from django.http import HttpResponse
import time

#FirstApp

# Create your views here.

def display(request):
    ss='''
                <center>
                        <h2 style="color:red">
                            Hello user, wellcome to Django First-Project First-App
                        </h2>
                        <hr/>
                </center>
       '''
    return HttpResponse(ss)

def show(request):
    ss='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
    <style>
        h1{
            color: brown;
        }
        h2{
            color: grey;
        }
        h3{
            color: violet;
        }
        h4{
            color: greenyellow;
        }
        h5{
            color: blue;
        }
        h6{
            color: teal;
        }
    </style>
</head>
<body>
    <center>
        <h1>Welcome to DJANGO HTML webpage</h1>
        <hr color="yellow" width="85%"/>
        <h2>Welcome to DJANGO HTML webpage</h2>
        <hr color="blue" width="75%"/>
        <h3>Welcome to DJANGO HTML webpage</h3>
        <hr color="red" width="65%"/>
        <h4>Welcome to DJANGO HTML webpage</h4>
        <hr color="green" width="55%"/>
        <h5>Welcome to DJANGO HTML webpage</h5>
        <hr color="pink" width="45%"/>
        <h6>Welcome to DJANGO HTML webpage</h6>
        <hr color="silver" width="35%"/>
    </center>
</body>
</html>
    '''
    return HttpResponse(ss)

def hello(request):
    ss='''
    <html>
		<head>
			<title>Hello brother this is Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
'''
    return HttpResponse(ss)

def datetime(request):
    print("dtime/ url is requested & datetime() is executed")
    ct=time.ctime()
    print("client requested date & time on server: ",ct)
    ss='''
    <html>
        <head>
            <style>
                h2{
                color:yellow;
                background-color:#333;
                width:70%;
                }
                h3{
                color:lightblue;
                background-color:#333;
                width:60%;
                }
                h4{
                color:grey;
                background-color:#333;
                width:50%;
                }
            </style>
        </head>
        <body>
            <center>
                <h2>Hello User Welcome To Django Webpage</h2>
                <hr color="brown" width=80% />
                <h3>Server Date & Time::''',ct,''' </h3>
                <hr color="brown" width=70% />
                <h4>''',ct,'''</h4>
            </center>
        </body>
    </html>
    '''
    return HttpResponse(ss)

def homepage(request):
    ss='''
    <html>
        <head>
            
        </head>
        <body>
            <center>
                <h1>Welcome To DEFAULT Homepage</h1>
                <hr/>
                <h2>Your Requested Page Is Not Found</h2>
                <hr/>
                <h2>Please Try Another Link or URL</h2>
            </center>
        </body>
    </html>
    '''
    return HttpResponse(ss)

def gitview(request):
    return HttpResponse("<h1>Hello User From Git(local)...!!!<h1><hr/>")