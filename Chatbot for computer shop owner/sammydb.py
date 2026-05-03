from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Replace with your actual MongoDB connection string
uri = "mongodb+srv://gpsd:helloworld@gpsd0.3fvcw.mongodb.net/?retryWrites=true&w=majority&appName=gpsd0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Create the ComputerStore database
db = client['ComputerStore']

# Create collections
appspec = db['appspec']
items = db['items']
stock = db['stock']
price = db['price']
discount = db['discount']
warranty = db['warranty']
sales = db['sales']
login = db['login']

# Insert data into appspec collection
appspec.insert_many([
    {'App_ID': '1', 'App_Name': 'far cry 1', 'App_Type': 'Video Game', 'Processor': 'Intel Pentium III', 'Storage': '4 GB', 'RAM': '256 MB', 'Video_RAM': '128 MB'},
    {'App_ID': '2', 'App_Name': 'PUBG', 'App_Type': 'Video Game', 'Processor': 'Intel Core i5', 'Storage': '50 GB', 'RAM': '16 GB', 'Video_RAM': '3GB'},
    {'App_ID': '3', 'App_Name': 'Apex Legends', 'App_Type': 'Video Game', 'Processor': 'Intel Core i3', 'Storage': '3.8GB', 'RAM': '8 GB', 'Video_RAM': '4GB'},
    {'App_ID': '4', 'App_Name': 'Adobe Premiere Pro', 'App_Type': 'Software', 'Processor': 'Intel Core i5', 'Storage': '8 GB', 'RAM': '8 GB', 'Video_RAM': '4GB'},
    {'App_ID': '5', 'App_Name': 'Counter-Strike 2', 'App_Type': 'Video Game', 'Processor': 'Intel Core i5', 'Storage': '85GB', 'RAM': '8 GB', 'Video_RAM': '4GB'},
    {'App_ID': '6', 'App_Name': 'Microsoft Word', 'App_Type': 'Productivity', 'Processor': 'Intel Core i3', 'Storage': '20GB', 'RAM': '4GB', 'Video_RAM': '1GB'},
    {'App_ID': '7', 'App_Name': 'Adobe Photoshop', 'App_Type': 'Graphics Design', 'Processor': 'AMD Ryzen 7', 'Storage': '100GB', 'RAM': '16GB', 'Video_RAM': '6GB'},
    {'App_ID': '8', 'App_Name': 'Excel', 'App_Type': 'Productivity', 'Processor': 'Intel Core i5', 'Storage': '30GB', 'RAM': '8GB', 'Video_RAM': '2GB'},
    {'App_ID': '9', 'App_Name': 'AutoCAD', 'App_Type': 'Engineering', 'Processor': 'Intel Xeon', 'Storage': '150GB', 'RAM': '32GB', 'Video_RAM': '8GB'},
    {'App_ID': '10', 'App_Name': 'FIFA 22', 'App_Type': 'Sports Game', 'Processor': 'AMD Ryzen 9', 'Storage': '75GB', 'RAM': '16GB', 'Video_RAM': '4GB'},
    {'App_ID': '11', 'App_Name': 'Chrome', 'App_Type': 'Web Browser', 'Processor': 'Intel Core i7', 'Storage': '10GB', 'RAM': '4GB', 'Video_RAM': '1GB'},
    {'App_ID': '12', 'App_Name': 'PowerPoint', 'App_Type': 'Productivity', 'Processor': 'AMD Ryzen 5', 'Storage': '25GB', 'RAM': '8GB', 'Video_RAM': '2GB'},
    {'App_ID': '13', 'App_Name': 'Adobe Illustrator', 'App_Type': 'Graphics Design', 'Processor': 'Intel Core i9', 'Storage': '120GB', 'RAM': '64GB', 'Video_RAM': '16GB'},
    {'App_ID': '14', 'App_Name': 'The Sims 4', 'App_Type': 'Simulation', 'Processor': 'Intel Core i5', 'Storage': '60GB', 'RAM': '8GB', 'Video_RAM': '2GB'},
    {'App_ID': '15', 'App_Name': 'Firefox', 'App_Type': 'Web Browser', 'Processor': 'AMD Ryzen 7', 'Storage': '15GB', 'RAM': '4GB', 'Video_RAM': '1GB'},
    {'App_ID': '16', 'App_Name': 'Visual Studio Code', 'App_Type': 'Development', 'Processor': 'Intel Core i7', 'Storage': '30GB', 'RAM': '16GB', 'Video_RAM': '2GB'},
    {'App_ID': '17', 'App_Name': 'GIMP', 'App_Type': 'Graphics Design', 'Processor': 'AMD Ryzen 5', 'Storage': '50GB', 'RAM': '8GB', 'Video_RAM': '4GB'},
    {'App_ID': '18', 'App_Name': 'Microsoft Teams', 'App_Type': 'Collaboration', 'Processor': 'Intel Core i5', 'Storage': '15GB', 'RAM': '4GB', 'Video_RAM': '1GB'},
    {'App_ID': '19', 'App_Name': 'Civilization VI', 'App_Type': 'Strategy', 'Processor': 'AMD Ryzen 7', 'Storage': '80GB', 'RAM': '12GB', 'Video_RAM': '2GB'},
    {'App_ID': '20', 'App_Name': 'Visual Studio', 'App_Type': 'Development', 'Processor': 'Intel Core i9', 'Storage': '100GB', 'RAM': '32GB', 'Video_RAM': '8GB'},
    {'App_ID': '21', 'App_Name': 'Minecraft', 'App_Type': 'Adventure', 'Processor': 'Intel Core i5', 'Storage': '50GB', 'RAM': '8GB', 'Video_RAM': '2GB'},
    {'App_ID': '22', 'App_Name': 'NetBeans', 'App_Type': 'Development', 'Processor': 'AMD Ryzen 7', 'Storage': '25GB', 'RAM': '16GB', 'Video_RAM': '4GB'},
    {'App_ID': '23', 'App_Name': 'Zoom', 'App_Type': 'Communication', 'Processor': 'Intel Core i3', 'Storage': '10GB', 'RAM': '4GB', 'Video_RAM': '1GB'},
    {'App_ID': '24', 'App_Name': 'Fortnite', 'App_Type': 'Battle Royale', 'Processor': 'AMD Ryzen 5', 'Storage': '75GB', 'RAM': '12GB', 'Video_RAM': '2GB'},
    {'App_ID': '25', 'App_Name': 'Far Cry 2', 'App_Type': 'First-person Shooter', 'Processor': 'Intel Core i5', 'Storage': '30GB', 'RAM': '6GB', 'Video_RAM': '1GB'},
    {'App_ID': '26', 'App_Name': 'GTA V', 'App_Type': 'Action-Adventure', 'Processor': 'AMD Ryzen 7', 'Storage': '100GB', 'RAM': '16GB', 'Video_RAM': '4GB'},
])

# Insert data into items collection
items.insert_many([
    {'id': 1, 'item_name': 'mouse', 'Item_Pic_Url': 'https://www.easygetproduct.com/wp-content/uploads/2019/03/9.-VicTsing-MM057-2.4G-Wireless-Portable-Mobile-Mouse-Optical-Mice-with-USB-Receiver-5-Adjustable-DPI-Levels-6-Buttons-for-Notebook-PC-Laptop-Computer-Black-1.jpg', 'Item_detail': 'The mouse provides precise control for smooth navigation. It features an ergonomic design for comfort, multiple buttons for efficient task management, and comes in both wired and wireless options. Ideal for enhancing productivity and gaming.'},
    {'id': 2, 'item_name': 'keyboard', 'Item_Pic_Url': 'https://i.pinimg.com/originals/f4/d0/a0/f4d0a0043198f01c329a32c304329750.jpg', 'Item_detail': 'The keyboard offers comfortable typing with responsive keys. It features a range of layouts and designs, including ergonomic options for reduced strain. Available in wired and wireless models, it’s essential for efficient data entry and productivity.'},
    {'id': 3, 'item_name': 'monitor', 'Item_Pic_Url': 'https://silicophilic.com/wp-content/uploads/2020/02/Screen_Darker_Than_Usual.jpg', 'Item_detail': 'The monitor delivers clear and vibrant visuals with high resolution. It offers various sizes and screen types, including LED and IPS, for enhanced color accuracy and viewing angles. Ideal for both work and entertainment, it supports multitasking and immersive experiences.'},
    {'id': 4, 'item_name': 'Lenovo IdeaPad Flex 5', 'Item_Pic_Url': 'https://mdcomputers.lk/wp-content/uploads/2023/03/71TAF2Z73uL.jpg', 'Item_detail': 'The Intel Core i3 processor is perfect for everyday computing needs. It provides smooth performance for web browsing, document editing, and media streaming, all while being energy-efficient. With integrated graphics, it supports casual gaming and HD video streaming, making it an excellent choice for home and office use.'},
    {'id': 5, 'item_name': 'Intel i3', 'Item_Pic_Url': 'https://mdcomputers.lk/wp-content/uploads/2023/03/71TAF2Z73uL.jpg', 'Item_detail': 'The Intel Core i3 processor is perfect for everyday computing needs. It provides smooth performance for web browsing, document editing, and media streaming, all while being energy-efficient. With integrated graphics, it supports casual gaming and HD video streaming, making it an excellent choice for home and office use.'},
    {'id': 6, 'item_name': 'Intel i5', 'Item_Pic_Url': 'https://www.komplett.dk/img/p/1200/1197859.jpg', 'Item_detail': 'The Intel Core i5 processor is ideal for both everyday and demanding computing tasks. It delivers robust performance for multitasking, web browsing, office applications, and multimedia activities. With integrated graphics, it supports casual gaming and HD video streaming, all while being energy-efficient. This makes it a versatile and powerful choice for home and office use.'},
    {'id': 7, 'item_name': 'Logitech M187', 'Item_Pic_Url': 'https://www.target.com.au/medias/static_content/product/images/large/18/06/A921806.jpg', 'Item_detail': 'The Logitech M187 is a compact wireless mouse offering reliable 2.4 GHz connectivity, precise tracking, and a long-lasting battery. Its small size makes it highly portable and ideal for on-the-go use.'},
    {'id': 8, 'item_name': 'Macbook M2 air', 'Item_Pic_Url': 'https://image.sofmap.com/images/product/other/2133052147947_3.jpg', 'Item_detail': 'The MacBook Air M2 features a sleek design with a powerful M2 chip, high-resolution Retina display, and long battery life, making it ideal for fast, efficient computing on the go.'},
    {'id': 9, 'item_name': 'Samsung Galaxy S24', 'Item_Pic_Url': 'https://taazapost24.com/wp-content/uploads/2023/12/Samsung-Galaxy-S24-Ultra-1.jpg', 'Item_detail': 'The Samsung Galaxy S24 combines cutting-edge performance with sleek design. It features a high-resolution display, advanced camera system, powerful processor, and long-lasting battery. With 5G connectivity, it offers fast and reliable performance for all your mobile needs.'},
    {'id': 10, 'item_name': 'Nokia 105', 'Item_Pic_Url': 'https://mobilebuyprice.com/wp-content/uploads/2023/05/Nokia-105-4G.jpg', 'Item_detail': 'The Nokia 105 is a compact, durable feature phone with a long battery life, simple interface, and reliable performance. It’s perfect for basic communication and essential features.'},
    {'id': 11, 'item_name': 'Apple MacBook Air M1', 'Item_Pic_Url': 'https://i.rtings.com/assets/products/l3QhIc1S/apple-macbook-air-13-m1-2020/design-medium.jpg?format=auto', 'Item_detail': 'The Apple MacBook Air with M1 chip features a 13.3-inch Retina display, 8-core CPU, and long battery life, making it ideal for everyday tasks and light professional work.'},
    {'id': 12, 'item_name': 'HP Pavilion Gaming Laptop', 'Item_Pic_Url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH_giBycWoHQG2CzBFYuHXWUWW-NyE_gbnPw&s', 'Item_detail': 'The HP Pavilion Gaming Laptop has a 15.6-inch Full HD display, AMD Ryzen 5 processor, and NVIDIA GeForce GTX 1650. It’s designed for gamers who need solid performance at a reasonable price.'},
    {'id': 13, 'item_name': 'Dell Inspiron 15 3000', 'Item_Pic_Url': 'https://www.lklk.lk/storage/files/lk/1125/thumb-816x460-2041adcf7cfa48e120d7c76e218fa394.jpg', 'Item_detail': 'The Dell Inspiron 15 3000 is a budget-friendly laptop with a 15.6-inch display, Intel Core i3 processor, and 8GB RAM. Perfect for students and casual users.'},
    {'id': 14, 'item_name': 'Logitech MX Master 3 Mouse', 'Item_Pic_Url': 'https://lifemobile.lk/wp-content/uploads/2022/06/Logitech-MX-Master-3S-Wireless-Mouse.png', 'Item_detail': 'The Logitech MX Master 3 is an advanced wireless mouse featuring customizable buttons, ergonomic design, and precision tracking. Ideal for productivity enthusiasts.'},
    {'id': 15, 'item_name': 'Corsair K95 RGB Mechanical Keyboard', 'Item_Pic_Url': 'https://assets.corsair.com/image/upload/f_auto,q_auto/content/CH-9000220-NA-CGK95-RGB-NA-005.png', 'Item_detail': 'The Corsair K95 RGB is a mechanical gaming keyboard with Cherry MX switches, RGB backlighting, and programmable macro keys, catering to both gamers and power users.'},
    {'id': 16, 'item_name': 'Lenovo ThinkPad T14s', 'Item_Pic_Url': 'https://capital.lv/media/catalog/product/cache/78b7d5e9d325dc0c77c021f203703bf1/f/c/fc7e9c6f-7a72-4740-a311-6f335398fde0.jpg', 'Item_detail': 'The Lenovo ThinkPad T14s is a business laptop with a 14-inch Full HD display, AMD Ryzen 7 Pro processor, and excellent build quality. Known for its durability and performance.'},
    {'id': 17, 'item_name': 'Samsung 970 EVO Plus SSD 1TB', 'Item_Pic_Url': 'https://redtech.lk/wp-content/uploads/2021/12/1TB-Samsung-970-EVO-Plus-M.2-NVMe-SSD.png', 'Item_detail': 'The Samsung 970 EVO Plus SSD offers 1TB of storage, read speeds up to 3,500MB/s, and is ideal for users seeking fast storage upgrades.'},
    {'id': 18, 'item_name': 'Acer Predator Helios 300', 'Item_Pic_Url': 'https://images-cdn.ubuy.co.id/634005433f4f712dd4290459-acer-predator-helios-300-gaming-laptop.jpg', 'Item_detail': 'The Acer Predator Helios 300 is a gaming laptop with a 15.6-inch FHD display, Intel Core i7, and NVIDIA GeForce RTX 3060. A great choice for gaming and high-performance tasks.'},
    {'id': 19, 'item_name': 'Asus ROG Strix G15', 'Item_Pic_Url': 'https://dlcdnwebimgs.asus.com/gain/494B67B0-3C89-4FAB-9DFB-3D27FCDE9058/w260', 'Item_detail': 'The Asus ROG Strix G15 is a gaming laptop with a 15.6-inch FHD display, AMD Ryzen 9 processor, and powerful NVIDIA graphics, designed for competitive gaming.'},
    {'id': 20, 'item_name': 'Microsoft Surface Go 3', 'Item_Pic_Url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoN0y4O_LplbaD-DZjEYGA6_ufTrvhtEMCrA&s', 'Item_detail': 'The Microsoft Surface Go 3 is a compact 2-in-1 tablet with a 10.5-inch display and Intel Pentium processor, perfect for portability and light tasks.'},
    {'id': 21, 'item_name': 'Razer Blade 15 Advanced', 'Item_Pic_Url': 'https://m.media-amazon.com/images/I/71kcJxMggRL._AC_UF350,350_QL50_.jpg', 'Item_detail': 'The Razer Blade 15 Advanced features a 15.6-inch QHD display, Intel Core i7 processor, and NVIDIA GeForce RTX 3070 graphics. Known for its sleek design and high performance, it’s ideal for gamers and creators.'},
    {'id': 22, 'item_name': 'Apple iMac 24-inch M1', 'Item_Pic_Url': 'https://futureworld.com.lk/wp-content/uploads/2021/08/600x600-24-SILVER-1-430x430.jpg', 'Item_detail': 'The Apple iMac with M1 chip has a stunning 24-inch Retina display, 8-core CPU, and impressive graphics performance. Perfect for creative professionals looking for a powerful and stylish all-in-one desktop.'},
    {'id': 23, 'item_name': 'Seagate Barracuda 2TB HDD', 'Item_Pic_Url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2iS09__f9kCAzs8rPRqSFcFWQ4xtXpSkDcQ&s', 'Item_detail': 'The Seagate Barracuda 2TB HDD is a reliable and high-capacity hard drive designed for desktop computers, with fast read and write speeds, ideal for storing large amounts of data.'},
    {'id': 24, 'item_name': 'Kingston A2000 NVMe SSD 500GB', 'Item_Pic_Url': 'https://m.media-amazon.com/images/I/51uBHaaB36L._AC_UF1000,1000_QL80_.jpg', 'Item_detail': 'The Kingston A2000 NVMe SSD provides 500GB of high-speed storage with read speeds up to 2,200MB/s, ideal for faster boot times and improved system performance.'},
    {'id': 25, 'item_name': 'Corsair Vengeance LPX 16GB DDR4 RAM', 'Item_Pic_Url': 'https://m.media-amazon.com/images/I/71jGZ9WpjTL.jpg', 'Item_detail': 'The Corsair Vengeance LPX 16GB DDR4 RAM runs at 3200MHz, delivering fast and reliable performance for gaming and intensive tasks, making it a popular choice among PC builders.'},
    {'id': 26, 'item_name': 'Acer Aspire 5', 'Item_Pic_Url': 'https://m.media-amazon.com/images/I/71vvXGmdKWL.jpg', 'Item_detail': 'The Acer Aspire 5 is a budget-friendly laptop with a 15.6-inch Full HD display, AMD Ryzen 5 processor, and solid performance for everyday tasks. Perfect for students and professionals on a budget.'},
    {'id': 27, 'item_name': 'Logitech G Pro X Gaming Headset', 'Item_Pic_Url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTo3-ratgx-GFqHTcXemOel5tRY4dquDo1sPw&s', 'Item_detail': 'The Logitech G Pro X headset offers crystal-clear sound quality, Blue VO!CE mic technology, and memory foam earpads for long-lasting comfort, ideal for competitive gamers.'},
    {'id': 28, 'item_name': 'HP Omen 25L Gaming Desktop', 'Item_Pic_Url': 'https://www.omen.com/content/dam/sites/omen/worldwide/desktops/omen-25l/lapras-7-customizability-future-proofing-21-c-2-w-2-omen-lapras-25-l-a-rgb-jack-black-non-odd-right-facing.png', 'Item_detail': 'The HP Omen 25L Gaming Desktop features AMD Ryzen 7, NVIDIA GeForce RTX 2060, and customizable RGB lighting, designed for high-performance gaming and creative applications.'},
    {'id': 29, 'item_name': 'Samsung Odyssey G7 27-inch Monitor', 'Item_Pic_Url': 'https://m.media-amazon.com/images/I/617FSZEJwrL._AC_UF350,350_QL80_.jpg', 'Item_detail': 'The Samsung Odyssey G7 is a curved 27-inch QHD monitor with a 240Hz refresh rate and 1ms response time, offering an immersive experience for both gaming and productivity.'},
    {'id': 30, 'item_name': 'TP-Link Archer AX50 Wi-Fi 6 Router', 'Item_Pic_Url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAljLQqkBZlKXozdnKAuY10Rzwnqq3cSuesQ&s', 'Item_detail': 'The TP-Link Archer AX50 is a high-performance Wi-Fi 6 router that offers faster speeds, greater capacity, and reduced network congestion, perfect for high-demand homes and offices.'},
])

# Insert data into stock collection
stock.insert_many([
    {'id': 1, 'stock': 10},
    {'id': 2, 'stock': 12},
    {'id': 3, 'stock': 40},
    {'id': 4, 'stock': 10},
    {'id': 5, 'stock': 100},
    {'id': 6, 'stock': 0},
    {'id': 7, 'stock': 200},
    {'id': 8, 'stock': 10},
    {'id': 9, 'stock': 10},
    {'id': 10, 'stock': 0},
    {'id': 11, 'stock': 10},
    {'id': 12, 'stock': 14},
    {'id': 13, 'stock': 40},
    {'id': 14, 'stock': 13},
    {'id': 15, 'stock': 16},
    {'id': 16, 'stock': 0},
    {'id': 17, 'stock': 240},
    {'id': 18, 'stock': 11},
    {'id': 19, 'stock': 10},
    {'id': 20, 'stock': 0},
    {'id': 21, 'stock': 10},
    {'id': 22, 'stock': 18},
    {'id': 23, 'stock': 51},
    {'id': 24, 'stock': 10},
    {'id': 25, 'stock': 170},
    {'id': 26, 'stock': 0},
    {'id': 27, 'stock': 300},
    {'id': 28, 'stock': 50},
    {'id': 29, 'stock': 10},
    {'id': 30, 'stock': 0},
])

# Insert data into price collection
price.insert_many([
    {'id': 1, 'price': 10000.00},
    {'id': 2, 'price': 12000.00},
    {'id': 3, 'price': 40000.00},
    {'id': 4, 'price': 299000.00},
    {'id': 5, 'price': 39500.00},
    {'id': 6, 'price': 58000.00},
    {'id': 7, 'price': 4350.00},
    {'id': 8, 'price': 698000.00},
    {'id': 9, 'price': 319000.00},
    {'id': 10, 'price': 8290.00},
    {'id': 11, 'price': 10000.00},
    {'id': 12, 'price': 14000.00},
    {'id': 13, 'price': 40678.00},
    {'id': 14, 'price': 13235.00},
    {'id': 15, 'price': 19008.00},
    {'id': 16, 'price': 23000.00},
    {'id': 17, 'price': 24008.00},
    {'id': 18, 'price': 11459.00},
    {'id': 19, 'price': 4400.00},
    {'id': 20, 'price': 23908.00},
    {'id': 21, 'price': 10670.00},
    {'id': 22, 'price': 18345.00},
    {'id': 23, 'price': 52316.00},
    {'id': 24, 'price': 23410.00},
    {'id': 25, 'price': 12317.00},
    {'id': 26, 'price': 20470.00},
    {'id': 27, 'price': 30000.00},
    {'id': 28, 'price': 500000.00},
    {'id': 29, 'price': 1045.00},
    {'id': 30, 'price': 2333.00},
])

# Insert data into discount collection
discount.insert_many([
    {'id': 5, 'discount_rate': 10.00},
    {'id': 6, 'discount_rate': 15.00},
    {'id': 9, 'discount_rate': 25.00},
    {'id': 11, 'discount_rate': 18.00},
    {'id': 15, 'discount_rate': 15.00},
    {'id': 17, 'discount_rate': 25.00},
    {'id': 22, 'discount_rate': 5.00},
    {'id': 26, 'discount_rate': 15.00},
    {'id': 27, 'discount_rate': 30.00},
])

# Insert data into warranty collection
warranty.insert_many([
    {'id': 5, 'warranty_in_months': 6},
    {'id': 6, 'warranty_in_months': 12},
    {'id': 9, 'warranty_in_months': 24},
    {'id': 10, 'warranty_in_months': 3},
    {'id': 12, 'warranty_in_months': 12},
    {'id': 15, 'warranty_in_months': 24},
    {'id': 17, 'warranty_in_months': 6},
    {'id': 18, 'warranty_in_months': 12},
    {'id': 20, 'warranty_in_months': 24},
    {'id': 23, 'warranty_in_months': 6},
    {'id': 24, 'warranty_in_months': 12},
    {'id': 25, 'warranty_in_months': 24},
    {'id': 27, 'warranty_in_months': 6},
    {'id': 28, 'warranty_in_months': 36},
    {'id': 29, 'warranty_in_months': 24},
])

# Insert data into sales collection
sales.insert_many([
    {'SaleID': 1, 'id': 1, 'QuantitySold': 23, 'SaleDate': '2023-10-02'},
    {'SaleID': 2, 'id': 3, 'QuantitySold': 36, 'SaleDate': '2023-11-23'},
    {'SaleID': 3, 'id': 1, 'QuantitySold': 2, 'SaleDate': '2024-01-12'},
    {'SaleID': 4, 'id': 3, 'QuantitySold': 20, 'SaleDate': '2024-06-23'},
    {'SaleID': 5, 'id': 1, 'QuantitySold': 10, 'SaleDate': '2024-07-12'},
    {'SaleID': 6, 'id': 11, 'QuantitySold': 27, 'SaleDate': '2023-10-21'},
    {'SaleID': 7, 'id': 2, 'QuantitySold': 33, 'SaleDate': '2023-11-24'},
    {'SaleID': 8, 'id': 17, 'QuantitySold': 2, 'SaleDate': '2024-02-12'},
    {'SaleID': 9, 'id': 30, 'QuantitySold': 21, 'SaleDate': '2024-06-03'},
    {'SaleID': 10, 'id': 12, 'QuantitySold': 19, 'SaleDate': '2024-07-02'},
    {'SaleID': 11, 'id': 16, 'QuantitySold': 2, 'SaleDate': '2023-01-02'},
    {'SaleID': 12, 'id': 24, 'QuantitySold': 17, 'SaleDate': '2023-01-23'},
    {'SaleID': 13, 'id': 5, 'QuantitySold': 2, 'SaleDate': '2024-01-12'},
    {'SaleID': 14, 'id': 8, 'QuantitySold': 5, 'SaleDate': '2023-06-23'},
    {'SaleID': 15, 'id': 19, 'QuantitySold': 5, 'SaleDate': '2024-07-12'},
    {'SaleID': 16, 'id': 27, 'QuantitySold': 10, 'SaleDate': '2022-10-02'},
    {'SaleID': 17, 'id': 15, 'QuantitySold': 8, 'SaleDate': '2021-11-23'},
    {'SaleID': 18, 'id': 18, 'QuantitySold': 2, 'SaleDate': '2020-01-12'},
    {'SaleID': 19, 'id': 20, 'QuantitySold': 7, 'SaleDate': '2023-06-13'},
    {'SaleID': 20, 'id': 7, 'QuantitySold': 14, 'SaleDate': '2020-07-15'},
])

# Insert data into login collection (assuming you want to insert some sample data)
login.insert_many([
    {'UserID': 1, 'UserName': 'admin', 'UserPassword': 'password123'},
    {'UserID': 2, 'UserName': 'user1', 'UserPassword': 'passuser1'},
])

print("Data inserted successfully!")
