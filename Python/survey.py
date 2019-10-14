# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:56:31 2019

@author: NaveenCR
"""

import cx_Oracle
import time
import datetime
from flask import Flask,request,render_template,redirect,url_for

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#credentials to connect to Oracle Exadata are masked/hidden
CONN_INFO = {
    'host': 'xxx',
    'port': 1521,
    'user': 'xxx',
    'psw': 'xxx',
    'service': 'xxx'
}
CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)

app=Flask(__name__)

#login page
@app.route('/', methods=['GET', 'POST'])
def get_data(): 
    if request.method=='POST':
        return redirect(url_for('options'))
    return render_template('login.html')

#page to display the options
@app.route('/options', methods=['GET', 'POST'])
def options(): 
    return render_template('options.html')

#page to create a new survey for admins speciifc
@app.route('/create', methods=['GET', 'POST'])
def create(): 
    if request.method=='POST':
        #fetching all html buttons using the respective names
        survey_name=request.form['survey_name']
        your_name=request.form['your_name']
        qn1_sli=request.form['qn1_sli']
        qn2_mli=request.form['qn2_mli']
        qn3_dd=request.form['qn3_dd']
        qn4_r=request.form['qn4_r']
        qn5_cb=request.form['qn5_cb']
        #fetching the html buttons dynamically based on number of options clicked by user
        qn3_op=request.form.getlist('qn3_op')
        qn4_op=request.form.getlist('qn4_op')
        qn5_op=request.form.getlist('qn5_op')
        
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        
        #creation of cursor and execute on db
        curs.execute('INSERT into ss_survey (survey_name,created_by,created_on,is_active) VALUES \
                     (\''+str(survey_name)+'\',\''+str(your_name)+'\',\''+str(timestamp)+'\',\''+str(1)+'\')')
        
        curs.execute ('select max(survey_id) from ss_survey')
        get_surveyid = curs.fetchone()
        
        #insert all survey related details such as survey_id,question_number,question_desc
        curs.execute('Insert into ss_questions (survey_id,question_number,question_desc) values \
                     ('+str(get_surveyid[0])+',\''+str(1)+'\',\''+str(qn1_sli)+'\')')
        curs.execute('Insert into ss_questions (survey_id,question_number,question_desc) values \
                     ('+str(get_surveyid[0])+',\''+str(2)+'\',\''+str(qn2_mli)+'\')')
        curs.execute('Insert into ss_questions (survey_id,question_number,question_desc) values \
                     ('+str(get_surveyid[0])+',\''+str(3)+'\',\''+str(qn3_dd)+'\')')
        curs.execute('Insert into ss_questions (survey_id,question_number,question_desc) values \
                     ('+str(get_surveyid[0])+',\''+str(4)+'\',\''+str(qn4_r)+'\')')
        curs.execute('Insert into ss_questions (survey_id,question_number,question_desc) values \
                     ('+str(get_surveyid[0])+',\''+str(5)+'\',\''+str(qn5_cb)+'\')')

        #insert all survey related details such as survey_id,question_number,question_desc for dynamic options
        for dd_options in qn3_op:
            values = '('+str(get_surveyid[0])+','+str(3)+',\''+str(dd_options)+'\')'
            curs.execute('Insert into ss_options (survey_id,question_number,option_value) values '+ str(values))
        
        for r_options in qn4_op:
            values = '('+str(get_surveyid[0])+','+str(4)+',\''+str(r_options)+'\')'
            curs.execute('Insert into ss_options (survey_id,question_number,option_value) values '+ str(values))

        for cb_options in qn5_op:
            values = '('+str(get_surveyid[0])+','+str(5)+',\''+str(cb_options)+'\')'
            curs.execute('Insert into ss_options (survey_id,question_number,option_value) values '+ str(values))
       
        connection.commit()
        curs.close()
        return redirect(url_for('view'))
    return render_template('create.html')

#page to view all the created surveys
@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method=='GET':
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        curs.execute ('select * from ss_survey order by survey_id desc')
        get_surveylist = curs.fetchall()
        return render_template('view.html', value=get_surveylist) 

#page to view all the created surveys and respond to the clicked survey by a user
@app.route('/view_take', methods=['GET', 'POST'])
def view_take():
    if request.method=='GET':
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        curs.execute ('select * from ss_survey order by survey_id desc')
        get_surveylist = curs.fetchall()
        return render_template('view_take.html', value=get_surveylist) 

#page to view the surveys and once clicked on respective survey, will route to results specific to clicked survey	
@app.route('/view_results', methods=['GET', 'POST'])
def view_results():
    if request.method=='GET':
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        curs.execute ('select * from ss_survey order by survey_id desc')
        get_surveylist = curs.fetchall()
        return render_template('view_results.html', value=get_surveylist) 
 
# page to display the results of surveys such as options clicked for specific qn, how many users responded   
@app.route('/results', methods=['GET', 'POST'])
def results():
    survey_id=request.args.get('rowData')
    if request.method=='GET':
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        curs.execute ('select * from ss_results where survey_id='+ str(survey_id))
        get_surveylist = curs.fetchall()
        return render_template('results.html', value=get_surveylist) 

#page to display the surveys
@app.route('/survey', methods=['GET','POST'])
def survey():    
    if request.method=='GET':
        survey_id=request.args.get('rowData')
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        
        curs.execute('select survey_name from ss_survey where survey_id='+ str(survey_id))
        get_survey_name=curs.fetchone()
        
        curs.execute ('select question_number,question_desc from ss_questions \
                      where survey_id=' + str(survey_id) + ' order by question_number')
        get_qns = curs.fetchall()
    
        curs.execute('select option_value from ss_options where question_number=3 and survey_id='+ str(survey_id))
        get_dd=curs.fetchall()
    
        curs.execute('select option_value from ss_options where question_number=4 and survey_id='+ str(survey_id))
        get_r=curs.fetchall()
        
        curs.execute('select option_value from ss_options where question_number=5 and survey_id='+ str(survey_id))
        get_cb=curs.fetchall()
        
        return render_template('survey.html',qns=get_qns, dd_ops=get_dd ,r_ops=get_r ,cb_ops=get_cb, survey_name=get_survey_name)
    
    if request.method=='POST':
        return redirect(url_for('view'))

#page to take a survey		
@app.route('/take', methods=['GET','POST'])
def take():
    survey_id=request.args.get('rowData')
    user_name="Naveen CR"
    if request.method=='GET':
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        
        curs.execute('select survey_name from ss_survey where survey_id='+ str(survey_id))
        get_survey_name=curs.fetchone()
        
        curs.execute ('select question_number,question_desc from ss_questions \
                      where survey_id=' + str(survey_id) + ' order by question_number')
        get_qns = curs.fetchall()
    
        curs.execute('select option_value from ss_options where question_number=3 and survey_id='+ str(survey_id))
        get_dd=curs.fetchall()
    
        curs.execute('select option_value from ss_options where question_number=4 and survey_id='+ str(survey_id))
        get_r=curs.fetchall()
        
        curs.execute('select option_value from ss_options where question_number=5 and survey_id='+ str(survey_id))
        get_cb=curs.fetchall()
        
        return render_template('take.html',qns=get_qns, dd_ops=get_dd ,r_ops=get_r ,cb_ops=get_cb, survey_name=get_survey_name)
    
    if request.method=='POST':
        ans_1=request.form['ans_1']
        ans_2=request.form['ans_2']
        ans_3=request.form['ans_3']
        ans_4=request.form['ans_4']
        ans_5=request.form.getlist('ans_5')
        connection = cx_Oracle.connect(CONN_STR)
        curs=connection.cursor()
        
        curs.execute('Insert into ss_results (survey_id,question_number,answer,submitted_on,submitted_by) values \
                     ('+str(survey_id)+',\''+str(1)+'\',\''+str(ans_1)+'\',\''+str(timestamp)+'\',\''+str(user_name)+'\')')
        
        curs.execute('Insert into ss_results (survey_id,question_number,answer,submitted_on,submitted_by) values \
                     ('+str(survey_id)+',\''+str(2)+'\',\''+str(ans_2)+'\',\''+str(timestamp)+'\',\''+str(user_name)+'\')')
        
        curs.execute('Insert into ss_results (survey_id,question_number,answer,submitted_on,submitted_by) values \
                     ('+str(survey_id)+',\''+str(3)+'\',\''+str(ans_3)+'\',\''+str(timestamp)+'\',\''+str(user_name)+'\')')
        
        curs.execute('Insert into ss_results (survey_id,question_number,answer,submitted_on,submitted_by) values \
                     ('+str(survey_id)+',\''+str(4)+'\',\''+str(ans_4)+'\',\''+str(timestamp)+'\',\''+str(user_name)+'\')')
           
        for cb_options_ans in ans_5:
            values = '('+str(survey_id)+',\''+str(5)+'\',\''+str(cb_options_ans)+'\',\''+str(timestamp)+'\',\''+str(user_name)+'\')'
            curs.execute('Insert into ss_results (survey_id,question_number,answer,submitted_on,submitted_by) values '+ str(values))
           
        connection.commit()
        curs.close()
        return redirect(url_for('view_take'))

#main method to execute on 127.0.0.1/5000: port    
if __name__=='__main__':
    app.run(debug=True)
