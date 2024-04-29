from flask import Flask, render_template, request, jsonify,redirect, url_for
import numpy as np
import os
from flask_mysqldb import MySQL,MySQLdb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split



UPLOAD_FOLDER = './static/images'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'firstaidthroughai'
path = os.getenv("PATH")
mysql = MySQL(app)




### INDEX PAGE
@app.route('/')
def indexpage():
    return render_template("index.html")



### HOME PAGE
@app.route("/homepage",methods = ['GET','POST'])
def option():
     button_clicked = request.form['Submit']
     if button_clicked == 'DOCTOR LOGIN':
          return redirect(url_for('doctorlogin'))
     elif button_clicked == 'PATIENT LOGIN':
          return redirect(url_for('user_login'))
     



###
@app.route("/doctorlogin")
def doctorlogin():
     return render_template("doctorlogin.html")

@app.route("/userlogin")
def user_login():
     return render_template("login.html")



### DOCTOR LOGIN WITH THEIR CREDENTIALS
@app.route("/doctorlogin",methods=['GET','POST'])
def doctormain():
    admin_name = request.form['textfield']
    admin_pass = request.form['textfield2']
    if admin_name == 'admin' and admin_pass == 'admin':
        return render_template("doctormain.html")
    else:
        return "something wrong........."



### DOCTOR MAIN PAGE
@app.route('/doctormain',methods = ['GET','POST'])
def doctor_main_page_options():
    if request.method == 'POST':
        button_clicked = request.form['Submit']
        if button_clicked == 'View Patient Information':
            return redirect(url_for('patientinfo'))

        elif button_clicked == 'Upload Solution':
            return redirect(url_for('uploadsolution'))

        elif button_clicked == 'Logout':
            return render_template('index.html')

### SHOW PATIENT INFORMATION
@app.route('/patientinfo')
def patientinfo():
    try:
        sqlstr = "select * from patientregister"
        print(sqlstr)   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute(sqlstr)
        mysql.connection.commit()
        users = cursor.fetchall()
        drow = cursor.rowcount
        cursor.close()
        print(users)
        return render_template('patientinfo.html',users=users)
    except Exception as ex:
        print (ex)
    return "something is wrong"  



### UPLOAD SOLUTION
@app.route('/uploadsolutiondata',methods=['GET','POST'])
def uploadsolution():
    if request.method == 'POST':
        incident = request.form['select']
        first = request.form['textfield']
        final = request.form['textarea']
        link = request.form['textfield3']
        print(incident)
        print(first)
        print(final)
        try:
            sqlstr = '''insert into doctorsolution(incident,firstaid,finalaid,link) values(%s,%s,%s,%s)'''
            print(sqlstr)   
            cursor = mysql.connection.cursor()
            cursor.execute(sqlstr,(incident,first,final,link))
            mysql.connection.commit()
            cursor.close()
            return 'SOLUTION UPLOAD SUCCESSFULLY'
        except Exception as ex:
            print (ex)
    return render_template('uploadsolution.html')





### USER LOGIN WITH THEIR CREDENTIALS
@app.route("/userlogin",methods=['GET','POST'])
def userlogin():
    admin_name = request.form['textfield']
    admin_pass = request.form['textfield2']
    try:
        sqlstr = "select * from patientregister where patientname=%s and password=%s"
        print(sqlstr)   
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr,(admin_name,admin_pass))
        print(admin_name)
        print(admin_pass)
        cursor.close()
        msg = ""
        if cursor.rowcount == 0:
            msg = 0 
        else:
            msg = 1  
    except Exception as ex:
        print (ex)
    if msg==1:
        return render_template("welcome.html")
    else:
        return "something wrong........."


### CHOOSE PREDICTION
@app.route("/chooseprediction",methods = ['GET','POST'])
def prediction_option():
     button_clicked = request.form['Submit']
     if button_clicked == 'Patient Registration':
          return redirect(url_for('newuser'))

     elif button_clicked == 'View First-Aid':
         return redirect(url_for('viewmedicine'))

     elif button_clicked == 'Diabates Prediction':
          return redirect(url_for('diabetes'))

     elif button_clicked == 'Parkinson Prediction':
          return redirect(url_for('parkinson'))

     elif button_clicked == 'Heart Disease Prediction':
          return redirect(url_for('heart'))

     elif button_clicked == 'View Graph Analysis':
          return render_template('graph.html')





### VIEW FIRST-AID INFORMATION
@app.route('/solutioninfo')
def viewmedicine():
    try:
        sqlstr = "select * from doctorsolution"
        print(sqlstr)   
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute(sqlstr)
        mysql.connection.commit()
        users = cursor.fetchall()
        drow = cursor.rowcount
        cursor.close()
        print(users)
        return render_template('viewsolution.html',users=users)
    except Exception as ex:
        print (ex)
    return "something is wrong"



### REGISTER A NEW PATIENT
@app.route("/registration",methods=['GET','POST'])
def newuser():
     if request.method == 'POST':
          patid = request.form['textfield']
          patname = request.form['textfield2']
          area = request.form['select']
          gender = request.form['RadioGroup1']
          ptype = request.form['RadioGroup2']
          sick = request.form['select2']
          age = request.form['textfiel6']
          password = request.form['textfield7']
          
          try :
            sqlstr = '''insert into patientregister(patientid,patientname,area,gender,patienttype,sick,age,password) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
            print(sqlstr)   
            cursor = mysql.connection.cursor()
            cursor.execute(sqlstr,(patid,patname,area,gender,ptype,sick,age,password))
            mysql.connection.commit()
            cursor.close()
            return 'register successfully'
          except Exception as ex:
            print (ex)
     return render_template('register.html')



### DIABETES DISEASE PREDICTION
@app.route("/diabatesprediction",methods = ['GET','POST'])
def diabetes():
    if request.method == 'POST':
        dataset = pd.read_csv("diabetes.csv")
        x = dataset.iloc[:,:-1].values 
        y = dataset.iloc[:,-1].values 
        print("x=",x)
        print("y=",y)
        from sklearn.model_selection import train_test_split 
        x_train,x_test,y_train,y_test = train_test_split(x ,y, test_size = 0.25 ,random_state = 0)
        #printing the spliited dataset
        print("x_train=",x_train)
        print("x_test=",x_test)
        print("y_train=",y_train)
        print("y_test=",y_test)
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors = 5, metric = 'euclidean' , p = 2)
        knn.fit(x_train, y_train)
        print('K NEAREST NEIGHBOUR ACCURACY LEVEL:', knn.score(x_train, y_train))
        Y_predict=knn.predict(x_test) # predicted output
        print(Y_predict)
        ### READING INPUT
        glucose = request.form['textfield']
        bp      = request.form['textfield2']
        skin    = request.form['textfield3']
        insulin = request.form['textfield4']
        bmi     = request.form['textfield5']
        dia     = request.form['textfield6']
        age     = request.form['textfield7']
        
        knn = knn.predict([[glucose,bp,skin,insulin,bmi,dia,age]])
        print(knn)
        if knn == 0:
            a = "this person does not have a diabates"
        else:
            a = "this person have a diabates"
        str(glucose)
        str(bp)
        str(skin)
        str(insulin)
        str(bmi)
        str(dia)
        str(age)
        return render_template("diabatesoutput.html",glucose=glucose,bp=bp,skin=skin,insulin=insulin,bmi=bmi,dia=dia,age=age, OUTPUT = a)
    return render_template("diabetes.html")





### PARKINSON DISEASE PREDICTION
@app.route("/parkinsonprediction",methods = ['GET','POST'])
def parkinson():
    if request.method == 'POST':
        dataset = pd.read_csv("ParkinsonsDisease.csv")
        x = dataset.iloc[:,:-1].values 
        y = dataset.iloc[:,-1].values 
        print("x=",x)
        print("y=",y)
        from sklearn.model_selection import train_test_split 
        x_train,x_test,y_train,y_test = train_test_split(x ,y, test_size = 0.25 ,random_state = 0)
        #printing the spliited dataset
        print("x_train=",x_train)
        print("x_test=",x_test)
        print("y_train=",y_train)
        print("y_test=",y_test)
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors = 5, metric = 'euclidean' , p = 2)
        knn.fit(x_train, y_train)
        print('K NEAREST NEIGHBOUR ACCURACY LEVEL:', knn.score(x_train, y_train))
        Y_predict=knn.predict(x_test) # predicted output
        print(Y_predict)
        ### READING INPUT
        glucose = request.form['textfield']
        bp      = request.form['textfield2']
        skin    = request.form['textfield3']
        insulin = request.form['textfield4']
        bmi     = request.form['textfield5']
        dia     = request.form['textfield6']
        age     = request.form['textfield7']
        
        knn = knn.predict([[glucose,bp,skin,insulin,bmi,dia,age]])
        print(knn)
        if knn == 0:
            a = "this person does not have a parkinson"
        else:
            a = "this person have a parkinson"
        str(glucose)
        str(bp)
        str(skin)
        str(insulin)
        str(bmi)
        str(dia)
        str(age)
        return render_template("parkinsonoutput.html",glucose=glucose,bp=bp,skin=skin,insulin=insulin,bmi=bmi,dia=dia,age=age, OUTPUT = a)
    return render_template("parkinson.html")




### HEART DISEASE PREDICTION
@app.route("/heartprediction",methods = ['GET','POST'])
def heart():
    if request.method == 'POST':
        dataset = pd.read_csv("heart.csv")
        x = dataset.iloc[:,:-1].values 
        y = dataset.iloc[:,-1].values 
        print("x=",x)
        print("y=",y)
        from sklearn.model_selection import train_test_split 
        x_train,x_test,y_train,y_test = train_test_split(x ,y, test_size = 0.25 ,random_state = 0)
        #printing the spliited dataset
        print("x_train=",x_train)
        print("x_test=",x_test)
        print("y_train=",y_train)
        print("y_test=",y_test)
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors = 5, metric = 'euclidean' , p = 2)
        knn.fit(x_train, y_train)
        print('K NEAREST NEIGHBOUR ACCURACY LEVEL:', knn.score(x_train, y_train))
        Y_predict=knn.predict(x_test) # predicted output
        print(Y_predict)
        ### READING INPUT
        glucose = request.form['textfield']
        bp      = request.form['textfield2']
        skin    = request.form['textfield3']
        insulin = request.form['textfield4']
        bmi     = request.form['textfield5']
        dia     = request.form['textfield6']
        age     = request.form['textfield7']
        
        knn = knn.predict([[glucose,bp,skin,insulin,bmi,dia,age]])
        print(knn)
        if knn == 0:
            a = "this person does not have a heart disease"
        else:
            a = "this person have a heart disease"
        str(glucose)
        str(bp)
        str(skin)
        str(insulin)
        str(bmi)
        str(dia)
        str(age)
        return render_template("heartoutput.html",glucose=glucose,bp=bp,skin=skin,insulin=insulin,bmi=bmi,dia=dia,age=age,OUTPUT = a)
    return render_template("heart.html")








if __name__=="__main__":
    app.run(debug=True)
