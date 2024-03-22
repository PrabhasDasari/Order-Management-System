SQL Schemas

CREATE DATABASE OMS;
USE OMS;

-- Create User table
CREATE TABLE [User] (
    UserId INT PRIMARY KEY,
    Username NVARCHAR(100),
    Password NVARCHAR(100),
    Role NVARCHAR(50)
);
-- Create Product table
CREATE TABLE Product (
    ProductId INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Description NVARCHAR(MAX),
    Price DECIMAL(10, 2),
    QuantityInStock INT,
    Type NVARCHAR(50),
);

-- Create Order table
CREATE TABLE [Order] (
    OrderId INT IDENTITY(1, 1) PRIMARY KEY,
    UserId INT FOREIGN KEY REFERENCES [User] (UserId)
);

-- Create OrderProduct table to represent the many-to-many relationship between Order and Product
CREATE TABLE OrderProduct (
    OrderId INT,
    ProductId INT,
    Quantity INT,
    PRIMARY KEY (OrderId, ProductId),
    FOREIGN KEY (OrderId) REFERENCES [Order] (OrderId),
    FOREIGN KEY (ProductId) REFERENCES Product(ProductId)
);

Reference Screenshots
1: Adding User
![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/0d39d6d2-14a5-4f13-a053-d642175d5236)
![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/028b0f29-5bf2-4358-be19-35a059a63e4e)

2: Adding Product
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/18150c0b-2872-4b75-bc76-b2d487166986)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/61dab2a7-277b-422e-91b4-44e8a0c5f16a)

3: Create Order
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/4c775213-18a8-4b74-8071-b9dc4848ed3e)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/7cfff7f1-6eb0-466c-88fc-c9ceb615acd1)
  
4: Get All Products
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/91443b48-ea84-41e4-a77b-2c08602f40d7)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/a381e900-e17c-441a-ac39-8b63428936b5)

5: Get Orders by User
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/518a2041-bc9d-4bcc-888a-4fd84770e374)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/2c696a58-734c-47d0-aa3f-60c276abe437)

6: Cancel Order
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/54156b86-4acd-470f-b8ae-ca531319aba8)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/095e621a-30bd-412f-9382-9c8def52680a)

7: User Not Found Exception
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/65eaeb91-f28f-41ba-8937-d08de25a0e9f)

8: Order Not Found Exception
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/b7f6ca82-f8c4-4a35-8dd9-d45c084ca052)

