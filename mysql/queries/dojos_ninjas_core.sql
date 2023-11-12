use dojos_and_ninjas_schema;
insert into dojos (name) values('Africa'),('America'),('France');
delete from dojos; 
insert into dojos (name) values('Tunisia'),('Moroco'),('Egypt');
insert into ninjas (first_name, last_name, age, dojo_id) 
values ('rania', 'fakraoui', 22, 4), ('nou', 'zidi', 32, 4), ('hani', 'trabelsi', 35, 4);
insert into ninjas (first_name, last_name, age, dojo_id) 
values ('Manel', 'Cholwati', 22, 5), ('Maher', 'Akrmi', 32, 5), ('Lili', 'Zitouni', 35, 5);
insert into ninjas (first_name, last_name, age, dojo_id) 
values ('Sonia', 'Jmal', 22, 6), ('Tarek', 'Chihi', 32, 6), ('Sameh', 'Zayani', 35, 6);
select* from dojos;
select* from dojos left join ninjas on dojos.id=ninjas.dojo_id where dojos.id=4;
select* from dojos left join ninjas on dojos.id=ninjas.dojo_id where dojos.id=6;
select * from dojos left join ninjas on dojos.id=ninjas.dojo_id where dojos.id=( select dojo_id from ninjas order by dojo_id desc limit 1);
select * from dojos where dojos.id=( select dojo_id from ninjas order by dojo_id desc limit 1);
