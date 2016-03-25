s_emp = (('ID', 'LAST_NAME', 'FIRST_NAME', 'USERID', 'START_DATE', 'COMMENTS', 'TITLE', 'SALARY', 'COMMISSION', 'DEPT_ID', 'MANAGER_ID'),
         ( 1, 'Martin', 'Carmen', 'martincu', '3-Mar-90', '', 'President', 4500, 0, 50, 0),
         ( 10, 'Jackson', 'Marta', 'jacksomt', '27-Feb-91', '', 'Warehouse Manager', 1507, 0, 45, 2),
         ( 11, 'Henderson', 'Colin', 'hendercs', '14-May-90', '', 'Sales Representative', 1400, 10, 31, 3),
         ( 12, 'Gilson', 'Sam', 'gilsonsj', '18-Jan-92', '', 'Sales Representative', 1490, 12.5, 32, 3),
         ( 13, 'Sanders', 'Jason', 'sanderjk', '18-Feb-91', '', 'Sales Representative', 1515, 10, 33, 3),
         ( 14, 'Dameron', 'Andre', 'dameroap', '9-Oct-91', '', 'Sales Representative', 1450, 17.5, 35, 3),
         ( 15, 'Hardwick', 'Elaine', 'hardwiem', '7-Feb-92', '', 'Stock Clerk', 1400, 0, 41, 6),
         ( 16, 'Brown', 'George', 'browngw', '8-Mar-90', '', 'Stock Clerk', 940, 0, 41, 6),
         ( 17, 'Washinton', 'Thomas', 'washintl', '9-Feb-91', '', 'Stock Clerk', 1200, 0, 42, 7),
         ( 18, 'Patterson', 'Donald', 'patterdv', '6-Aug-91', '', 'Stock Clerk', 795, 0, 42, 7),
         ( 19, 'Bell', 'Alexander', 'bellag', '26-May-91', '', 'Stock Clerk', 850, 0, 43, 8),
         ( 2, 'Smith', 'Doris', 'smithdj', '8-Mar-90', '', 'VP, Operations', 2450, 0, 41, 1),
         ( 20, 'Gantos', 'Eddie', 'gantosej', '30-Nov-90', '', 'Stock Clerk', 860, 0, 45, 9),
         ( 21, 'Stephenson', 'Blaine', 'stephebs', '17-Mar-91', '', 'Stock Clerk', 800, 0, 44, 10),
         ( 22, 'Chester', 'Eddie', 'chesteek', '30-Nov-90', '', 'Stock Clerk', 800, 0, 44, 9),
         ( 23, 'Pearl', 'Roger', 'pearlrg', '17-Oct-90', '', 'Stock Clerk', 795, 0, 34, 9),
         ( 24, 'Dancer', 'Bonnie', 'dancerbw', '17-Mar-91', '', 'Stock Clerk', 860, 0, 45, 7),
         ( 25, 'Schmitt', 'Sandra', 'schmitss', '9-May-91', '', 'Stock Clerk', 1100, 0, 45, 8),
         ( 3, 'Norton', 'Michael', 'nortonma', '17-Jun-91', '', 'VP, Sales', 2400, 0, 31, 1),
         ( 4, 'Quentin', 'Mark', 'quentiml', '7-Apr-90', '', 'VP, Finance', 2450, 0, 10, 1),
         ( 5, 'Roper', 'Joseph', 'roperjm', '4-Mar-90', '', 'VP, Administration', 2550, 0, 50, 1),
         ( 6, 'Brown', 'Molly', 'brownmr', '18-Jan-91', '', 'Warehouse Manager', 1600, 0, 41, 2),
         ( 7, 'Hawkins', 'Roberta', 'hawkinrt', '14-May-90', '', 'Warehouse Manager', 1650, 0, 42, 2),
         ( 8, 'Burns', 'Ben', 'burnsba', '7-Apr-90', '', 'Warehouse Manager', 1500, 0, 43, 2),
         ( 9, 'Catskill', 'Antoinette', 'catkiaw', '9-Feb-92', '', 'Warehouse Manager', 1700, 0, 44, 2))

s_dept = (('ID', 'NAME', 'REGION_ID'),
        (10, 'Finance', 1),
        (31, 'Sales', 1),
        (32, 'Sales', 2),
        (33, 'Sales', 3),
        (34, 'Sales', 4),
        (35, 'Sales', 5),
        (41, 'Operations', 1),
        (42, 'Operations', 2),
        (43, 'Operations', 3),
        (44, 'Operations', 4),
        (45, 'Operations', 5),
        (50, 'Administration', 1),
        )



print "\nselect * from s_dept"

print "\nselect last_name, first_name, title, salary from s_emp\n", [[i[1],i[2],i[6],i[7]] for i in s_emp[1::]]

print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40"

print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name\n",\
    sorted([[i[1],i[2],i[6],i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40], key=lambda x: x[0])

print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc"

print "\nselect last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id)\n",\
    [[i[1],i[2],i[6],i[7],j[1]] for i in s_emp[1::] for j in s_dept[1::] if i[9] == j[0]]

print "\nselect dept_id, avg(salary) from s_emp group by dept_id order by dept_id"

print "\nselect dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500\n",
#the codes in class produce spaces in result.
list1=[]
for dept in {d[9] for d in s_emp[1::]}: (lambda dept,avgSal: list1.append([dept,avgSal]) if avgSal<1500 else '')(dept,(lambda l: round(sum(l)/len(l),2))(map(float,[i[7] for i in s_emp[1::] if i[9] == dept])))
print list1

