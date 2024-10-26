CREATE_TABLE_STORE = """
CREATE TABLE IF NOT EXISTS store(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    category VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
)
"""

INSERT_STORE = """
    INSERT INTO store(name_product, category, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""