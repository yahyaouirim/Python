-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
use books_sql;
insert into users (first_name, last_name) values('Jane', 'Amsden'), ('Emily', 'Dixon'), 
('Theodore', 'Dostoevsky'),  ( 'William', 'Shapiro'),  ('Lao', 'Xiu');
-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
insert into books (title, num_of_pages) values('C Sharp', 194), ('Java', 225), 
('Python', 165),  ( 'PHP', 130),  ('Ruby', 122);

-- Query: Change the name of the C Sharp book to C#
update books set title='C#' where id=1; 
-- Query: Change the first name of the 4th user to Bill
update users set first_name='Bill' where id=4; 
-- Query: Have the first user favorite the first 2 books
insert into favorites values(1, 1),(1, 2);
-- Query: Have the second user favorite the first 3 books
insert into favorites values(2, 1),(2, 2),(2, 3);
-- Query: Have the third user favorite the first 4 books
insert into favorites values(3, 1),(3, 2),(3, 3),(3, 4);
-- Query: Have the fourth user favorite all the books
insert into favorites values(4, 1),(4, 2),(4, 3),(4, 4),(4, 5);
select* from users;
select* from books;
select * from favorites;
-- Query: Retrieve all the users who favorited the 3rd book
select * from users left join favorites on users.id=favorites.user_id  left join books on favorites.book_id= books.id where book_id=3;
-- Query: Remove the first user of the 3rd book's favorites
delete from favorites where (user_id=1 and book_id=3);
-- Query: Have the 5th user favorite the 2nd book
insert into favorites values (5, 2);
-- Find all the books that the 3rd user favorited
select * from books join favorites on books.id=favorites.book_id join users on favorites.user_id=users.id where users.id=3;
-- Query: Find all the users that favorited to the 5th book
select * from users join favorites on users.id=favorites.user_id join books on favorites.book_id=books.id where books.id=5;





