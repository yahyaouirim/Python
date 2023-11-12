use user_db;
show tables;
insert into users (first_name, last_name, email) values ('Rim', 'Yahyaoui', 'rimyahyaoui@gmail.com');
insert into users (first_name, last_name, email) values ('Kouba', 'Chorfi', 'koubachorfi@gmail.com');
insert into users (first_name, last_name, email) values ('Alaa', 'taeib', 'alaataeib@gmail.com');
select *from users;
select * from users where email='rimyahyaoui@gmail.com';
select * from users where id=3;
update users set  last_name='Pancakes' where id=3;
delete from users where id=2;
select * from users order by (first_name);
select * from users order by (first_name) desc;






