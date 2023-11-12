use lead_gen_business;
show tables;
select * from clients;
select * from clients limit 2,3;
insert into clients (first_name, last_name, email, joined_datetime) values('Manissa', 'Gomez', 'manissagomez@gmail.com', now());
insert into clients (first_name, last_name, email, joined_datetime) values('Michael', 'Garera', 'michaelgarera@gmail.com', now());
update clients set last_name='Rodregos' where id =12;
delete from clients where id=11;
set sql_safe_updates=0;

