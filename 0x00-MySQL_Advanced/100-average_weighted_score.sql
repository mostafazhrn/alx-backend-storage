-- this script shall create a stored procedure ComputeAverag...
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE weighted_score FLOAT;
    SET weighted_score = (SELECT SUM(score * weight) / SUM(weight)
    FROM users AS U JOIN corrections as C ON U.id = C.user_id
    JOIN projects AS P ON C.project_id = P.id
    WHERE U.id = user_id);
UPDATE users SET average_weighted_score = weighted_score WHERE id = user_id;
END//
DELIMITER ;
