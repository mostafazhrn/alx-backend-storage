-- this script shall create a trigger to reset valid_email
-- attribute only when email has changed
DELIMITER $$
CREATE TRIGGER reset_email BEFORE UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email != OLD.email THEN
SET NEW.valid_email = 0;
END IF;
END;
