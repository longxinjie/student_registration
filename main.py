from flask import Flask, render_template, request 
app = Flask(__name__)

#copy these 3 lines and modify it
@app.route('/')  #defining the function
def index():
    return render_template("index.html")
#when u load this, u will render the html file

@app.route('/new_student', methods=["GET", "POST"]) #handling another request path, function name and request path do not need to be the same, but just keep it the same for easy maintainance and tracking
#handle form request

#for get request is usually use args
#for post request is usually use forms 
def new_student():
    # if request.method== 'GET':  #to handle diff types of method
    
    # elif request.method== 'POST':
    if 'confirm' in request.args:
    #at the back of the url: ?key=value e.g. ?action=hello, sends the get method, so in args will show

        #returning result to user, all being handled by render template (will read in the html for u) 

  #how to return the contents of form_student.html?
        actual_name = request.form['field_name']
        actual_age = request.form['field_age']
        actual_nationality = request.form['field_nationality']
        return render_template(
            "form_student.html",
            student_name=actual_name,
            student_age = actual_age,
            student_nationality = actual_nationality,
            pagetype="confirm", 
            form_meta={
                'action': '/add_student',
                'method': 'POST'
            },
            form_data={
              'field_name': actual_name,
              'field_age': actual_age,
              'field_nationality': actual_nationality
            }
            
        )

    else:
        return render_template(
            'form_student.html',
            pagetype='new',
            form_meta={
              'action': '/new_student?confirm',
              'method': 'POST'
            },
            form_data={
              'field_name': ''
            })

@app.route('/new_student2', methods=["GET", "POST"]) 
def create_student():
    
    if 'confirm' in request.args:
        actualname = request.form['field_name']
        return render_template(
            "form_student.html",
            student_name=actualname,
            pagetype="confirm", 
            form_meta={
                'action': '/add_student',
                'method': 'POST'
            },
            form_data={
              'field_name': actualname
            }   
        )

    else:
        return render_template(
            'form_student.html',
            pagetype='new',
            form_meta={
              'action': '/new_student?confirm',
              'method': 'POST'
            },
            form_data={
              'field_name': ''
            })


@app.route('/new_cca', methods=["GET", "POST"])  #defining the function
def new_cca():
  if request.method == 'GET':
      return render_template('form_cca.html')

  elif request.method == 'POST':
      actualname = request.form['field_name']
      return render_template('confirm_cca.html', student_name=actualname)

@app.route('/add_student', methods= ['POST'])
def add_student():
    actual_name = request.form['field_name']
    actual_age = request.form['field_age']
    actual_nationality = request.form['field_nationality']
    result= f'Success! A new student has been created: {actual_name} {actual_age} {actual_nationality}'
    return result
    #for debug can do:
    # return f"{request.form}"
  
app.run(debug=True)
#configuration sever so that anyone can see and use the webApp (not secure but for now is okay)
#server show all the requests by clients

#everything from the first slash forward is the request path , left is the hostname/domainname
#404/ 200(working): status code