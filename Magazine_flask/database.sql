CREATE TABLE users(
	user_id serial primary key,
	user_login varchar(50) UNIQUE,
	user_password varchar(50),
	user_role smallint default(0)
);

INSERT INTO users (user_login, user_password, user_role)
VALUES ('root', 'root', 1);

INSERT INTO users (user_login, user_password, user_role)
VALUES ('Гость', '', 0);

INSERT INTO users (user_login, user_password)
VALUES ('Ivan', 'Ivan'), ('Kolya', 'Kolya');


CREATE TABLE category(
	category_id serial primary key,
	category_title varchar(50)
);

INSERT INTO category (category_title) VALUES ('Автомобиль'), ('Ноутбук');

CREATE TABLE products (
	product_id serial primary key,
	product_title varchar(50),
	product_description varchar(200),
	product_price numeric,
	product_category smallint,
	product_photo varchar(50)
);

INSERT INTO products (product_title, product_description, product_price, product_category, product_photo)
VALUES
('Lada Granta', 'Современный, технологичный, стремительный и стильный — автомобиль, каким он должен быть.', 1200000, 1, 'granta.png'),
('Lada Vesta', 'Вместимость и оснащенность, элегантность и практичность — Vesta превосходна во всем.', 1700000, 1, 'vesta.png'),
('Lada Niva Legend', 'LADA Niva Legend — узнаваемый стиль и прославленная проходимость.', 1400000, 1, 'niva.png'),
('Aquarius AQbook NE356', 'Отечественный многофункциональный ноутбук представляет собой отличный выбор для тех, кто ищет надежное устройство', 65000, 2, 'NE356.webp'),
('Aquarius AQbook NS626', 'Обновлённый ноутбук в классическом корпусе, с процессором 12 или 13-го поколения', 70000, 2, 'NS626.webp'),
('Aquarius AQbook NS636', 'Современный лёгкий ноутбук для повседневной работы из офиса или дома', 75000, 2, 'NS636.webp')
;

CREATE TABLE carts (
	cart_id serial primary key,
	cart_user varchar(50),
	cart_product smallint,
	cart_count smallint
);

CREATE TABLE orders (
	order_id serial primary key,
	order_user varchar(50),
	order_product smallint,
	order_count smallint,
	order_day date DEFAULT CURRENT_DATE
);
