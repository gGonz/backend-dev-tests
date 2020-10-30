# 04 Point of sale test

Write a very basic Django project that uses Django Rest Framework to provide a RESTful API for a point of sale that lets you track the inventory of products and the orders done.

Use the provided project boilerplate and add the code needed to pass all the unit tests provided in both `modules.inventory.tests` and `modules.orders.tests`.

Use at least the models provided in both `modules.inventory.models` and `modules.orders.models`, but feel free to add any extra model if needed.

The API must use **JSON** format and should provide the following endpoints and functionalities:

### `/api/products/`

* List all existing products
* Create a new product
* Retrieve an existing product
* Update an existing product

Note that **deleting a product is not allowed**.

A product must allow you to save:

* The description of the product
* The unit price of the product in cents
* The available stock of the product

### `/api/orders/`

* List all existing orders
* Create a new order
* Retrieve an existing order

Note that **updating or deleting a product is not allowed**.

A order must allow you to save/calculate:

* The list of items that were purchased
* The quantity of each item
* The total amount earned by the order in cents

Note that when a order is created, the corresponding products' stock must be updated.

## Instructions

1. Install the requirements with `pip install -r requirements.txt`
2. Run your tests with `python src/manage.py test src`
3. Commit your work when the command above reports an OK result
