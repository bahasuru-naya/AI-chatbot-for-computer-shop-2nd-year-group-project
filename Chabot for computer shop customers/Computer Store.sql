CREATE DATABASE ComputerStore;
#DROP DATABASE ComputerStore;

USE  ComputerStore;
#DROP TABLE Appspec;
CREATE TABLE Appspec(
App_ID CHAR(7) PRIMARY KEY,
App_Name  CHAR(50) NOT NULL,
App_Type CHAR(30) NOT NULL,
Processor CHAR(25) NOT NULL,
`Storage` CHAR(10) NOT NULL,
RAM CHAR(10) NOT NULL,
Video_RAM CHAR(10) NOT NULL
);

INSERT INTO Appspec VALUES('1','far cry 1','Video Game','Intel Pentium III','4 GB',' 256 MB','128 MB');
INSERT INTO Appspec VALUES('2','PUBG','Video Game',' Intel Core i5','50 GB','16 GB','3GB');
INSERT INTO Appspec VALUES('3','Apex Legends','Video Game','Intel Core i3','3.8GB',' 8 GB','4GB');
INSERT INTO Appspec VALUES('4','Adobe Premiere Pro','Software','Intel Core i5','8 GB',' 8 GB','4GB');
INSERT INTO Appspec VALUES('5','Counter-Strike 2','Video Game','Intel Core i5','85GB',' 8 GB','4GB');
INSERT INTO Appspec VALUES('6', 'Microsoft Word', 'Productivity', 'Intel Core i3', '20GB', '4GB', '1GB');
INSERT INTO Appspec VALUES('7', 'Adobe Photoshop', 'Graphics Design', 'AMD Ryzen 7', '100GB', '16GB', '6GB');
INSERT INTO Appspec VALUES('8', 'Excel', 'Productivity', 'Intel Core i5', '30GB', '8GB', '2GB');
INSERT INTO Appspec VALUES('9', 'AutoCAD', 'Engineering', 'Intel Xeon', '150GB', '32GB', '8GB');
INSERT INTO Appspec VALUES('10', 'FIFA 22', 'Sports Game', 'AMD Ryzen 9', '75GB', '16GB', '4GB');
INSERT INTO Appspec VALUES('11', 'Chrome', 'Web Browser', 'Intel Core i7', '10GB', '4GB', '1GB');
INSERT INTO Appspec VALUES('12', 'PowerPoint', 'Productivity', 'AMD Ryzen 5', '25GB', '8GB', '2GB');
INSERT INTO Appspec VALUES('13', 'Adobe Illustrator', 'Graphics Design', 'Intel Core i9', '120GB', '64GB', '16GB');
INSERT INTO Appspec VALUES('14', 'The Sims 4', 'Simulation', 'Intel Core i5', '60GB', '8GB', '2GB');
INSERT INTO Appspec VALUES('15', 'Firefox', 'Web Browser', 'AMD Ryzen 7', '15GB', '4GB', '1GB');
INSERT INTO Appspec VALUES('16', 'Visual Studio Code', 'Development', 'Intel Core i7', '30GB', '16GB', '2GB');
INSERT INTO Appspec VALUES('17', 'GIMP', 'Graphics Design', 'AMD Ryzen 5', '50GB', '8GB', '4GB');
INSERT INTO Appspec VALUES('18', 'Microsoft Teams', 'Collaboration', 'Intel Core i5', '15GB', '4GB', '1GB');
INSERT INTO Appspec VALUES('19', 'Civilization VI', 'Strategy', 'AMD Ryzen 7', '80GB', '12GB', '2GB');
INSERT INTO Appspec VALUES('20', 'Visual Studio', 'Development', 'Intel Core i9', '100GB', '32GB', '8GB');
INSERT INTO Appspec VALUES('21', 'Minecraft', 'Adventure', 'Intel Core i5', '50GB', '8GB', '2GB');
INSERT INTO Appspec VALUES('22', 'NetBeans', 'Development', 'AMD Ryzen 7', '25GB', '16GB', '4GB');
INSERT INTO Appspec VALUES('23', 'Zoom', 'Communication', 'Intel Core i3', '10GB', '4GB', '1GB');
INSERT INTO Appspec VALUES('24', 'Fortnite', 'Battle Royale', 'AMD Ryzen 5', '75GB', '12GB', '2GB');
INSERT INTO Appspec VALUES('25', 'Far Cry 2', 'First-person Shooter', 'Intel Core i5', '30GB', '6GB', '1GB');
INSERT INTO Appspec VALUES('26', 'GTA V', 'Action-Adventure', 'AMD Ryzen 7', '100GB', '16GB', '4GB');


USE ComputerStore ;
select *
from Appspec;


USE  ComputerStore;
#drop table  items;
CREATE TABLE items(
id INT PRIMARY KEY  NOT NULL AUTO_INCREMENT,
item_name CHAR(50) NOT NULL UNIQUE,
Item_Pic_Url  TEXT NOT NULL, 
Item_detail TEXT NOT NULL
);

INSERT INTO Items VALUES('1','mouse','https://www.easygetproduct.com/wp-content/uploads/2019/03/9.-VicTsing-MM057-2.4G-Wireless-Portable-Mobile-Mouse-Optical-Mice-with-USB-Receiver-5-Adjustable-DPI-Levels-6-Buttons-for-Notebook-PC-Laptop-Computer-Black-1.jpg','The mouse provides precise control for smooth navigation. It features an ergonomic design for comfort, multiple buttons for efficient task management, and comes in both wired and wireless options. Ideal for enhancing productivity and gaming.');
INSERT INTO Items VALUES('2','keyboard','https://i.pinimg.com/originals/f4/d0/a0/f4d0a0043198f01c329a32c304329750.jpg','The keyboard offers comfortable typing with responsive keys. It features a range of layouts and designs, including ergonomic options for reduced strain. Available in wired and wireless models, it’s essential for efficient data entry and productivity.');
INSERT INTO Items VALUES('3','monitor','https://silicophilic.com/wp-content/uploads/2020/02/Screen_Darker_Than_Usual.jpg','The monitor delivers clear and vibrant visuals with high resolution. It offers various sizes and screen types, including LED and IPS, for enhanced color accuracy and viewing angles. Ideal for both work and entertainment, it supports multitasking and immersive experiences.');
INSERT INTO Items VALUES('4','Lenovo IdeaPad Flex 5' ,'https://mdcomputers.lk/wp-content/uploads/2023/03/71TAF2Z73uL.jpg','The Intel Core i3 processor is perfect for everyday computing needs. It provides smooth performance for web browsing, document editing, and media streaming, all while being energy-efficient. With integrated graphics, it supports casual gaming and HD video streaming, making it an excellent choice for home and office use.' );
INSERT INTO Items VALUES('5','Intel i3' ,'https://mdcomputers.lk/wp-content/uploads/2023/03/71TAF2Z73uL.jpg','The Intel Core i3 processor is perfect for everyday computing needs. It provides smooth performance for web browsing, document editing, and media streaming, all while being energy-efficient. With integrated graphics, it supports casual gaming and HD video streaming, making it an excellent choice for home and office use.' );
INSERT INTO Items VALUES('6','Intel i5' ,'https://www.komplett.dk/img/p/1200/1197859.jpg','The Intel Core i5 processor is ideal for both everyday and demanding computing tasks. It delivers robust performance for multitasking, web browsing, office applications, and multimedia activities. With integrated graphics, it supports casual gaming and HD video streaming, all while being energy-efficient. This makes it a versatile and powerful choice for home and office use.');
INSERT INTO Items VALUES('7','Logitech M187','https://www.target.com.au/medias/static_content/product/images/large/18/06/A921806.jpg','The Logitech M187 is a compact wireless mouse offering reliable 2.4 GHz connectivity, precise tracking, and a long-lasting battery. Its small size makes it highly portable and ideal for on-the-go use.');
INSERT INTO Items VALUES('8','Macbook M2 air','https://image.sofmap.com/images/product/other/2133052147947_3.jpg','The MacBook Air M2 features a sleek design with a powerful M2 chip, high-resolution Retina display, and long battery life, making it ideal for fast, efficient computing on the go.');
INSERT INTO Items VALUES('9','Samsung Galaxy S24' ,'https://taazapost24.com/wp-content/uploads/2023/12/Samsung-Galaxy-S24-Ultra-1.jpg','The Samsung Galaxy S24 combines cutting-edge performance with sleek design. It features a high-resolution display, advanced camera system, powerful processor, and long-lasting battery. With 5G connectivity, it offers fast and reliable performance for all your mobile needs.');
INSERT INTO Items VALUES('10','Nokia 105','https://mobilebuyprice.com/wp-content/uploads/2023/05/Nokia-105-4G.jpg','The Nokia 105 is a compact, durable feature phone with a long battery life, simple interface, and reliable performance. It’s perfect for basic communication and essential features.');


USE ComputerStore ;
select *
from Items;

USE ComputerStore ;
CREATE TABLE stock(
id INT PRIMARY KEY  NOT NULL ,
stock INT NOT NULL,
constraint fk1 foreign key (id) references items(id)
);

INSERT INTO stock VALUES('1' ,'10' );
INSERT INTO stock VALUES('2','12' );
INSERT INTO stock VALUES('3','40' );
INSERT INTO stock VALUES('4' ,10 );
INSERT INTO stock VALUES('5',100 );
INSERT INTO stock VALUES('6' ,0 );
INSERT INTO stock VALUES('7',200 );
INSERT INTO stock VALUES('8',10 );
INSERT INTO stock VALUES('9',10 );
INSERT INTO stock VALUES('10',0 );

USE ComputerStore ;
select *
from stock;

CREATE TABLE price(
id INT PRIMARY KEY  NOT NULL ,
price Float(15,2),
constraint fk2 foreign key (id) references items(id)
);

INSERT INTO price VALUES('1', '10000.00' );
INSERT INTO price VALUES('2','12000.00' );
INSERT INTO price VALUES('3','40000.00' );
INSERT INTO price VALUES('4', 299000.00  );
INSERT INTO price VALUES('5', 39500.00  );
INSERT INTO price VALUES('6', 58000.00 );
INSERT INTO price VALUES('7', 4350.00  );
INSERT INTO price VALUES('8', 698000.00  );
INSERT INTO price VALUES('9', 319000.00  );
INSERT INTO price VALUES('10',8290.00 );

USE ComputerStore ;
select *
from price;

USE  ComputerStore;
#drop table  discount;
CREATE TABLE discount(
    id INT PRIMARY KEY NOT NULL,
    discount_rate FLOAT NOT NULL,    
    CONSTRAINT fk3 FOREIGN KEY (id) REFERENCES items(id)
);

INSERT INTO discount VALUES( '5', '10.00' );
INSERT INTO discount VALUES( '6', '15.00' );
INSERT INTO discount VALUES( '9', '25.00' );

USE ComputerStore ;
select *
from discount;

USE  ComputerStore;
#drop table  warranty;
CREATE TABLE warranty(
    id INT PRIMARY KEY NOT NULL,
    warranty_in_months INT NOT NULL,    
    CONSTRAINT fk4 FOREIGN KEY (id) REFERENCES items(id)
);

INSERT INTO warranty VALUES( '5', '6' );
INSERT INTO warranty VALUES( '6', '12' );
INSERT INTO warranty VALUES( '9', '24' );

USE ComputerStore ;
select *
from warranty;

USE ComputerStore ;
#drop table sales;
CREATE TABLE sales (
    SaleID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id INT,
    QuantitySold INT,
    SaleDate DATE,    
    FOREIGN KEY (id) REFERENCES items(id)
);
INSERT INTO sales VALUES( '1','1', '23','2023-10-2' );
INSERT INTO sales VALUES( '2','3', '36','2023-11-23' );
INSERT INTO sales VALUES( '3','1', '2','2024-1-12' );
INSERT INTO sales VALUES( '4','3', '20','2024-6-23' );
INSERT INTO sales VALUES( '5','1', '10','2024-7-12' );

USE ComputerStore ;
select *
from sales;

