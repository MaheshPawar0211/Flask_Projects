from flask import Flask,jsonify,request
app=Flask(__name__)
departments=[ 
  {
	'name':'tcs',
	'employees':[
	{
	'name':'mahesh',
	'salary':10	
	}
	]
   }
]


#  POST - Receives data 
# This endpoint create another department in dict
@app.route('/department',methods=['POST'])
def create_department():
    request_data=request.get_json()
    new_dept={
            'name':request_data['name'],
            'employees':[]
            }
    departments.append(new_dept)
    return jsonify(new_dept)


# This end point retrieves department data based on department name    
@app.route('/department/<string:name>')
def get_department(name):
	for department in departments:
		if department['name']==name:
			return jsonify(department)
	return jsonify({'message':'dept doent exist'})



# This end point retrieves all departments in dict
@app.route('/departments',methods=['GET'])
def get_departments():
	return jsonify({'departments':departments})
# covert list into dictionary


# This end point retrieves employee details in department provided in url
@app.route('/department/<string:name>/employee',methods=['POST'])
def create_employee_in_department(name):
    request_data=request.get_json()
    for department in departments:
        if department['name']==name:
            new_employee={
                'name':request_data['name'],
                'salary':request_data['salary']
                }
            department['employees'].append(new_employee)
            return jsonify({'departments':departments})
    return jsonify({'message':'dept doent exist'})    

        
# This end point add employee details in department provided in url
@app.route('/department/<string:name>/employee',methods=['GET'])
def get_employee_in_department(name):
	for department in departments:
		if department['name']==name:
			return jsonify(
                {
                    'employees':department['employees']
                }
            )

app.run()