from flask import *
from covid import Covid
from covid_india import states
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
app = Flask(__name__)
@app.route('/')
def covid():
	covid = Covid(source="worldometers")
	covid.get_data()
	active = covid.get_total_active_cases()
	confirmed = covid.get_total_confirmed_cases()
	recovered = covid.get_total_recovered()
	deaths = covid.get_total_deaths()
	y=states.getdata('Total')
  
	Total=y["Total"]
	Active1=y["Active"]
	Cured=y["Cured"]
	Death=y["Death"]
	return render_template("index1.html",val1=active,val2=confirmed,val3=recovered,val4=deaths,val5=Total,val6=Active1,val7=Cured,val8=Death)
@app.route('/tracker')	
def tracker():
	return render_template("covid19.html")		
@app.route('/socialdistancing')	
def socialdistancing():
	return render_template("blog.html")	
@app.route('/educate')	
def educate():
	return render_template("educate.html")	
@app.route('/immunity',methods=['GET', 'POST'])	
def immunity():
	if request.method == 'POST':
			name=request.form['name']
			email=request.form['email']
			qn1=request.form['qn1']
			qn2=request.form['qn2']
			qn3=request.form['qn3']
			qn4=request.form['qn4']
			qn5=request.form['qn5']
			qn6=request.form['qn6']
			qn7=request.form['qn7']
			qn8=request.form['qn8']
			qn9=request.form['qn9']
			qn10=request.form['qn10']
			sum1=int(qn2)+int(qn5)
			sum2=int(qn1)+int(qn3)+int(qn4)+int(qn6)+int(qn7)+int(qn8)+int(qn9)+int(qn10)
			if(sum1>=8 and sum2<=16):
				return render_template("good.html")
			elif(sum1>=5 and sum1<8 and sum2>16 and sum2<=24):
				return render_template("average.html")
			else:
				return render_template("bad.html")
			print (name,email,qn1,qn2,qn3,qn10)
	return render_template("immunitycheck.html")		
if __name__ == '__main__':
	app.debug=True
	app.run()
