# 一、SQL基本练习(先复习SQL语法,自学连接查询,再仔细观察SQL表字段)

1. 选择姓名中有字母 a 和 e 的员工姓名

   ```sql
   SELECT first_name, last_name FROM employees
   WHERE first_name like '%a%' OR first_name like '%e%' OR last_name like '%a%' OR last_name like '%e%';
   ```

2. 显示出表 employees 表中 first_name 以 'e'结尾的员工信息

   ```sql
   SELECT * FROM employees
   WHERE first_name LIKE '%e';
   ```

3. 显示出表 employees 的 manager_id 是 100,101,110 的员工姓名、职位

   ```sql
   SELECT first_name, last_name, job_id FROM employees
   WHERE manager_id = 100 OR manager_id = 101 OR manager_id = 110 ;
   ```

4. 查询员工的姓名和部门号和年薪，按年薪降序 按姓名升序

   ```sql
   SELECT first_name, last_name, department_id, salary FROM employees
   ORDER BY salary DESC, first_name ASC;
   ```

5. 选择工资不在 8000 到 17000 的员工的姓名和工资，按工资降序

   ```sql
   SELECT first_name, last_name, salary FROM employees
   WHERE salary < 8000 OR salary > 17000
   ORDER BY salary DESC ;
   ```

6. 查询邮箱中包含 e 的员工信息，并先按邮箱的字节数降序，再按部门号升序

   ```sql
   SELECT * FROM employees
   WHERE email LIKE '%e%'
   ORDER BY LENGTH(email) DESC, department_id ASC;
   ```

7. 显示系统时间(注：日期+时间)

   ```sql
   SELECT NOW();
   ```

8. 查询员工号，姓名，工资，以及工资提高百分之 20%后的结果（new salary）

   ```sql
   SELECT employee_id, first_name, last_name, salary, salary*1.2 AS new_salary FROM employees;
   ```

9. 将员工的姓名按首字母排序，并写出姓名的长度（length）

   ```sql
   SELECT first_name, last_name, LENGTH(first_name)+LENGTH(last_name) AS name_length
   FROM employees
   ORDER BY first_name ASC;
   ```

10. 查询员工最高工资和最低工资的差距（DIFFERENCE）

    ```sql
    SELECT MAX(salary)-MIN(salary) AS DIFFERENCE FROM employees;
    ```

11. 查询各个管理者手下员工的最低工资，其中最低工资不能低于 6000， 没有管理者的员工不计算在内

    ```sql
    SELECT manager_id, MIN(salary) FROM employees
    WHERE salary > 6000 AND manager_id IS NOT NULL
    GROUP BY manager_id;
    ```

12. 查询所有部门的编号，员工数量和工资平均值,并按平均工资降序

    ```sql
    SELECT department_id, COUNT(department_id), AVG(salary) FROM employees
    WHERE department_id IS NOT NULL
    GROUP BY department_id
    ORDER BY AVG(salary) DESC;
    ```

13. 查询公司员工工资的最大值，最小值，平均值，总和

    ```sql
    SELECT MAX(salary) AS 最大值, MIN(salary) AS 最小值, AVG(salary) AS 平均, SUM(salary) AS 总和 FROM employees;
    ```

14. 查询员工表中的最大入职时间和最小入职时间的相差天（DIFFRENCE）

    ```sql
    SELECT DATEDIFF(MAX(hiredate),MIN(hiredate)) AS DIFFRENCE FROM employees;
    ```

15. 查询部门编号为 90 的员工个数

    ```sql
    SELECT COUNT(department_id) FROM employees
    WHERE department_id = 90;
    ```

16. 查询哪个城市没有部门

    ```sql
    SELECT city
    FROM locations
    LEFT JOIN departments ON locations.location_id = departments.location_id
    WHERE department_name IS NULL;
    ```

17. 查询部门名为 SAL 或 IT 的员工信息

    ```sql
    SELECT * FROM employees
    WHERE job_id LIKE 'SA%' OR job_id LIKE 'IT%';
    ```

