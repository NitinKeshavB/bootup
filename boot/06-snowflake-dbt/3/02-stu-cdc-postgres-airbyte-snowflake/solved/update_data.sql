select * from datastore.data_tbl;

insert into datastore.data_tbl values(3, 'c');
insert into datastore.data_tbl values(4, 'e');
update datastore.data_tbl set val='d' where id =4;