注意:题目一数据库为
主机地址:rm-bp1qre470ifl7u97e2o.mysql.rds.aliyuncs.com
端口:3306
用户名:eeyes
密码:Gan000803@
数据库名:myemployees

mysql -h rm-bp1qre470ifl7u97e2o.mysql.rds.aliyuncs.com -P 3306 -u eeyes -p Gan000803@

一、SQL基本练习(先复习SQL语法,自学连接查询,再仔细观察SQL表字段)

1. 选择姓名中有字母 a 和 e 的员工姓名
SELECT first_name, last_name
FROM employees
WHERE first_name like '%a%' OR first_name like '%e%' OR last_name like '%a%' OR last_name like '%e%'

2. 显示出表 employees 表中 first_name 以 'e'结尾的员工信息
SELECT * 
FROM employees
WHERE first_name LIKE '%e'

3. 显示出表 employees 的 manager_id 是 100,101,110 的员工姓名、职位
SELECT first_name, last_name, job_id
FROM employees
WHERE manager_id = 100 OR manager_id = 101 OR manager_id = 110 

4. 查询员工的姓名和部门号和年薪，按年薪降序 按姓名升序
SELECT first_name, last_name, job_id, salary
FROM employees
ORDER BY department_id ASC 

5. 选择工资不在 8000 到 17000 的员工的姓名和工资，按工资降序
SELECT first_name, last_name, salary
FROM employees
WHERE salary < 8000 OR salary > 17000
ORDER BY salary DESC 

6. 查询邮箱中包含 e 的员工信息，并先按邮箱的字节数降序，再按部门号升序
SELECT *
FROM employees
WHERE email LIKE '%e%'
ORDER BY LENGTH(email) DESC, department_id ASC;

7. 显示系统时间(注：日期+时间)
SELECT NOW();

8. 查询员工号，姓名，工资，以及工资提高百分之 20%后的结果（new salary）
SELECT employee_id, first_name, last_name, salary, salary*1.2 AS new_salary
FROM employees;

9. 将员工的姓名按首字母排序，并写出姓名的长度（length）
SELECT first_name, last_name, LENGTH(first_name)+LENGTH(last_name) AS length_name
FROM employees
ORDER BY first_name ASC;

10.查询员工最高工资和最低工资的差距（DIFFERENCE）
SELECT MAX(salary) - MIN(salary) AS difference
FROM employees;

11. 查询各个管理者手下员工的最低工资，其中最低工资不能低于 6000， 没有管理者的员工不计算在内
SELECT MIN(salary), manager_id
FROM employees
WHERE salary > 6000
GROUP BY manager_id;
HAVING manager_id IS NOT NULL;

12. 查询所有部门的编号，员工数量和工资平均值,并按平均工资降序

13. 查询公司员工工资的最大值，最小值，平均值，总和
SELECT MAX(salary) AS 最大值, MIN(salary) AS 最小值, 
AVG(salary) AS 平均, SUM(salary) AS 总和
FROM employees

14. 查询员工表中的最大入职时间和最小入职时间的相差天数 （DIFFRENCE）
SELECT DATEDIFF(MAX(hiredate),MIN(hiredate))
FROM employees;

15. 查询部门编号为 90 的员工个数
SELECT COUNT(first_name)
FROM employees
WHERE manager_id 
IN (SELECT manager_id FROM departments WHERE department_id =90)

16. 查询哪个城市没有部门

17. 查询部门名为 SAL 或 IT 的员工信息

二、使用pymysql将三个txt (2017_storage.txt,2018_storage.txt,2019_storage.txt)文件存入本地数据库(localhost)