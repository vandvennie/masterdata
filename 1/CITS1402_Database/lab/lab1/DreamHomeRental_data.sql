insert into Branch values ('B005', '22 Deer Rd', 'London', 'SW1 4EH');
insert into Branch values ('B007', '16 Argyll', 'Aberdeen', 'AB2 3SU');
insert into Branch values ('B003', '163 Main St', 'Glasgow', 'G11 9QX');
insert into Branch values ('B004', '32 Manse Rd', 'Bristol', 'BS99 1NZ');
insert into Branch values ('B002', '56 Clover Dr', 'London', 'NW10 6EU');

insert into Staff values ('SL21', 'John','White', 'Manager', 'M','1945-10-01',30000,'B005');
insert into Staff values ('SG37', 'Ann','Beech', 'Assistant', 'F','1960-11-10',12000,'B003');
insert into Staff values ('SG14', 'David','Ford', 'Supervisor', 'M','1958-03-24',18000,'B003');
insert into Staff values ('SA9', 'Mary','Howe', 'Assistant', 'F','1970-02-19',9000,'B007');
insert into Staff values ('SG5', 'Susan','Brand', 'Manager', 'F','1940-06-03',24000,'B003');
insert into Staff values ('SL41', 'Julie','Lee', 'Assistant', 'F','1965-06-13',9000,'B005');



insert into PrivateOwner values ('CO46', 'Joe','Keogh', '2 Fergus Drive, Aberdeen', '01224-861212','jkeogh@lhh.com','*****');
insert into PrivateOwner values ('CO87', 'Carol','Farrel', '6 Acharay St, Glasgow G32 9DX', '0141-357-7419','cfarrel@gmail.com','*****');
insert into PrivateOwner values ('CO40', 'Tina','Murphy', '63 Well St, Glasgow, G42', '0141-943-1728','tinam@hotmail.com','*****');
insert into PrivateOwner values ('CO93', 'Tony','Shaw', '12 Park Pl, Glasgow, G4 0QR', '0141-225-7025','tony.shaw@ark.com','*****');

insert into Client values ('CR76', 'John','Kay', '027-774-5632', 'Flat','425','john.kay@gmail.com');
insert into Client values ('CR56', 'Aline','Stewart', '0141-848-1825', 'Flat','350','astewart@hotmail.com');
insert into Client values ('CR74', 'Mike','Ritchie', '01475-392178', 'House','750','mritchie01@yahoo.co.uk');
insert into Client values ('CR62', 'Mary','Tregear', '01224-196720', 'Flat','600','maryt@hotmail.co.uk');

insert into PropertyForRent values ('PA14', '16 Hollhead','Aberdeen', 'AB7 5SU', 'House',6,650,'CO46','SA9','B007');
insert into PropertyForRent values ('PL94', '6 Argyll St','London', 'NW2', 'Flat',4,400,'CO87','SL41','B005');
insert into PropertyForRent values ('PG4', '9 Lawrence St','Glasgow', 'G11 9QX', 'Flat',3,350,'CO40',NULL,'B003');
insert into PropertyForRent values ('PG36', '2 Manor Rd','Glasgow', 'G32 4QX', 'Flat',3,375,'CO93','SG37','B003');
insert into PropertyForRent values ('PG21', '18 Dale Rd','Glasgow', 'G12', 'House',5,600,'CO87','SG37','B003');
insert into PropertyForRent values ('PG16', '5 Novar Dr','Glasgow', 'G12 9AX', 'Flat',4,450,'CO93','SG14','B003');

insert into Viewing values ('CR56', 'PA14','2008-05-24', 'too small');
insert into Viewing values ('CR76', 'PG4','2008-04-20', 'too remote');
insert into Viewing values ('CR56', 'PG4','2008-05-26', NULL);
insert into Viewing values ('CR62', 'PA14','2008-05-14', 'no dining room');
insert into Viewing values ('CR56', 'PG56','2008-04-28', NULL);

insert into Registration values ('CR76', 'B005','SL41','2008-01-02');
insert into Registration values ('CR56', 'B003','SG37','2007-04-11');
insert into Registration values ('CR74', 'B003','SG37','2006-11-16');
insert into Registration values ('CR62', 'B007','SA9','2007-03-07');