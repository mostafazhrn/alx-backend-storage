-- this script shall create a stored procedure ComputeAverageWeighted...
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN DECLARE avg_sco FLOAT;
SET avg_sco = (
SELECT SUM(score * weight) / SUM(weight)
FROM users AS U
JOIN corrections AS C
ON U.id = C.user_id
JOIN projects AS P
ON C.project_id = P.id
WHERE U.id = user_id);
UPDATE users SET average_score = avg_sco WHERE id = user_id;
END //
DELIMITER;
