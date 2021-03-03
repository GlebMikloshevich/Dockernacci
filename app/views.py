from app import app
from flask import Flask, render_template, request


@app.route('/', methods = ['GET', 'POST'])
def home():
	#return render_template('home.html', message="hello")
	message = "10"
	index2 = ""
	if request.method == 'POST':
		index = int(request.form['index'])
		index2 = str(fib(index))
	#if index > 0:
	#	message = str(10)


	return render_template('home.html', message=index2)
   #return str(fib(8))

fib_array = [1, 1]

def fib(n):
        if n < 2:
                return 1
        elif n > len(fib_array):
                return fib(n-1) + fib(n-2)
        elif n == len(fib_array):
                fib_array.append(fib_array[n-1] + fib_array[n-2])
        return(fib_array[n])




