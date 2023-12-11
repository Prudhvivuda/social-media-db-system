DELIMITER $$

CREATE TRIGGER after_insert_report
AFTER INSERT ON report
FOR EACH ROW
BEGIN

    CALL delete_reported_user(NEW.reported_profile);
END $$

DELIMITER ;



DELIMITER //

CREATE TRIGGER delete_block_list
AFTER INSERT ON block_list
FOR EACH ROW
BEGIN
    DECLARE blocked_user_id CHAR(36);

    SET blocked_user_id = NEW.blocked_user;

    DELETE FROM followers
    WHERE follower_user_id = blocked_user_id OR following_user_id = blocked_user_id;

    DELETE FROM comments
    WHERE user_id = blocked_user_id;

    DELETE FROM comment_likes
    WHERE user_id = blocked_user_id;

END;
// DELIMITER ;

