CREATE TABLE IF NOT EXISTS item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    purchase_date DATE NOT NULL,
    position VARCHAR(255),
    related_item_id INT,
    relative_position ENUM('inside', 'above', 'below', 'left', 'right'),
    is_consumable BOOLEAN DEFAULT FALSE,
    expiry_date DATE,
    FOREIGN KEY (related_item_id) REFERENCES item(id) ON DELETE SET NULL
);
