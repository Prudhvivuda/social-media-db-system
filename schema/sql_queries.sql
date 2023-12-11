select * from user;

# Retrieve all posts with their authors and the number of likes each post has:
SELECT 
    posts.post_id,
    posts.post_content,
    user.user_name AS author_username,
    COUNT(likes.like_id) AS like_count
FROM posts
JOIN user ON posts.author = user.user_id
LEFT JOIN likes ON posts.post_id = likes.post_id
GROUP BY posts.post_id, posts.post_content, author_username;

# Find all users who have mentioned a specific user in their posts:
SELECT
    user.user_name AS mentioned_by_username,
    mentioned_users.user_name AS mentioned_user_username,
    posts.post_content
FROM mentions
JOIN user ON mentions.mentioned_by = user.user_id
JOIN user AS mentioned_users ON mentions.mentioned_user = mentioned_users.user_id
JOIN posts ON mentions.post_id = posts.post_id
WHERE mentioned_users.user_id = 'specific_user_id';

# Retrieve the latest posts from users the current user is following:
SELECT
    posts.post_id,
    posts.post_content,
    user.user_name AS author_username
FROM posts
JOIN followers ON posts.author = followers.following_user_id
JOIN user ON posts.author = user.user_id
WHERE followers.follower_user_id = 'current_user_id'
ORDER BY posts.created_at DESC
LIMIT 10;

select * from report;
