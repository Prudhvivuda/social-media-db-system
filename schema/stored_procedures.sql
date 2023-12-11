-- 1 Creating posts
DELIMITER $$

CREATE PROCEDURE create_post(
    IN author_id CHAR(36),
    IN post_content VARCHAR(255),
    IN caption VARCHAR(255),
    IN location VARCHAR(255)
)
BEGIN
    DECLARE new_post_id CHAR(36);
    
    INSERT INTO posts (post_id, post_content, created_at, author, caption, location)
    VALUES (UUID(), post_content, NOW(), author_id, caption, location);
    
    SET new_post_id = LAST_INSERT_ID();
    
    SELECT new_post_id AS post_id;
END $$

DELIMITER ;


-- 2 Liking a post
DELIMITER $$

CREATE PROCEDURE like_post(
    IN user_id CHAR(36),
    IN post_id CHAR(36)
)
BEGIN

    DECLARE new_like_id CHAR(36);
    
    INSERT INTO likes (like_id, created_at, user_id, post_id)
    VALUES (UUID(), NOW(), user_id, post_id);
    
    SET new_like_id = LAST_INSERT_ID();
    
    SELECT new_like_id as like_id;

END $$

DELIMITER ;


-- 3
DELIMITER $$

CREATE PROCEDURE get_posts(
    IN user_id CHAR(36)
)
BEGIN

    SELECT *
    FROM posts
    WHERE author = user_id;
    
END $$

DELIMITER ;

-- 4 deleting reported profile

DELIMITER $$
CREATE PROCEDURE remove_reported_user(
    IN reported_profile_id CHAR(36),
    IN threshold INT
)
BEGIN
    DECLARE total_reports INT;

    SELECT COUNT(*) INTO total_reports
    FROM report
    WHERE reported_profile = reported_profile_id;

    IF total_reports >= threshold THEN

        DELETE FROM user WHERE user_id = reported_profile_id;

    END IF;
END $$

DELIMITER ;

-- 5 (4 with trigger)

DELIMITER $$

CREATE PROCEDURE delete_reported_user(
										IN reported_profile_id CHAR(36)
									  )
BEGIN
    DECLARE total_reports INT;

    SELECT COUNT(*) INTO total_reports
    FROM report
    WHERE reported_profile = reported_profile_id;

    IF total_reports >= 3 THEN
        DELETE FROM user WHERE user_id = reported_profile_id;
    END IF;
END $$

DELIMITER ;

-- trigger which calls SP
DELIMITER $$

CREATE TRIGGER after_insert_report
AFTER INSERT ON report
FOR EACH ROW
BEGIN

    CALL delete_reported_user(NEW.reported_profile);
END $$

DELIMITER ;


