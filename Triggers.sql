CREATE TRIGGER hash_pass BEFORE INSERT ON account_system_info
    FOR EACH ROW SET NEW.password = MD5(NEW.password);
	

DROP TRIGGER log_borrow;
DELIMITER $$
CREATE TRIGGER log_borrow AFTER INSERT ON borrow_history
    FOR EACH ROW BEGIN 
    insert into log_history values (NEW.b_id, "new book borowed", 
    concat("Book with id ", NEW.b_id),
    TIMESTAMP);
END$$

