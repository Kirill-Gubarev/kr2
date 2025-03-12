CREATE TABLE departments(
	id SERIAL PRIMARY KEY,
 	name VARCHAR(50),
 	manager_id INT
);

CREATE TABLE employees(
	id SERIAL PRIMARY KEY,
 	last_name VARCHAR(50),
	position VARCHAR(50)
   salary FLOAT,
   hire_date DATE,
   department_id INT REFERENCES departments(id)
);

CREATE TABLE projects(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	start_date DATE,
	end_date DATE,
	budget FLOAT
);

CREATE TABLE tasks(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	description VARCHAR(256),
	status VARCHAR(50),
   department_id INT REFERENCES departments(id),
	project_id INT REFERENCES projects(id),
	employees_id INT REFERENCES employees(id)
);

CREATE TABLE employee_projects(
	id SERIAL PRIMARY KEY,
	employee_id INT REFERENCES employees(id),
	project_id INT REFERENCES projects(id),
	role VARCHAR(50)
)
