CREATE VIEW activity AS
SELECT
    u.user_id,
    u.user_name,
    p.post_id,
    p.post_content,
    p.created_at AS post_created_at,
    c.comment_id,
    c.comment_content,
    c.created_at AS comment_created_at,
    l.like_id,
    l.created_at AS like_created_at
FROM user_auth u
LEFT JOIN posts p ON u.user_id = p.author
LEFT JOIN comments c ON u.user_id = c.user_id
LEFT JOIN likes l ON u.user_id = l.user_id;

CREATE VIEW trending_posts AS
SELECT
    p.post_id,
    p.post_content,
    p.created_at AS post_created_at,
    COUNT(l.like_id) AS like_count,
    COUNT(c.comment_id) AS comment_count
FROM posts p
LEFT JOIN likes l ON p.post_id = l.post_id
LEFT JOIN comments c ON p.post_id = c.post_id
GROUP BY p.post_id, p.post_content, p.created_at
ORDER BY like_count DESC, comment_count DESC;

CREATE VIEW followers_view AS
SELECT
    u.user_id AS follower_id,
    u.user_name AS follower_user_name,
    f.time_stamp,
    u2.user_id AS following_id,
    u2.user_name AS following_user_name
FROM followers f
JOIN user_auth u ON f.follower_user_id = u.user_id
JOIN user_auth u2 ON f.following_user_id = u2.user_id;

CREATE VIEW reported_content_view AS
SELECT
    r.report_id,
    r.category,
    r.report_reason,
    r.created_at AS report_created_at,
    u.user_id AS reported_by_user_id,
    u.user_name AS reported_by_user_name,
    u2.user_id AS reported_user_id,
    u2.user_name AS reported_user_name
FROM report r
JOIN user_auth u ON r.reported_by = u.user_id
JOIN user_auth u2 ON r.reported_profile = u2.user_id;



