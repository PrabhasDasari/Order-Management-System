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
    UserId INT FOREIGN KEY REFERENCES [User](UserId)
);

-- Create OrderProduct table to represent the many-to-many relationship between Order and Product
CREATE TABLE OrderProduct (
    OrderId INT,
    ProductId INT,
    Quantity INT,
    PRIMARY KEY (OrderId, ProductId),
    FOREIGN KEY (OrderId) REFERENCES [Order](OrderId),
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
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/b4675eb8-fcae-4269-850d-05ca4fcca5b5)
  
4: Get All Products
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/2bd5995b-617d-41e4-b0a7-494e30dc6519)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/90d8132f-b8dc-451e-a8b0-e980cdf4dc8f)

5: Get Orders by User
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/7e168b1c-a27a-472b-b706-bd118c9a82a0)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/55a10554-5168-451e-9cf2-9093cfb6b75d)

6: Cancel Order
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/5f026a3d-e518-4679-8af5-ad2f40110243)
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/f161a7ae-2f26-4849-bb64-b463893bed18)

7: User Not Found Exception
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/ecdff243-6a67-4675-a1af-1a67994ed48c)
  
8: Order Not Found Exception
  ![image](https://github.com/PrabhasDasari/Order-Management-System/assets/124909746/b7f6ca82-f8c4-4a35-8dd9-d45c084ca052)

