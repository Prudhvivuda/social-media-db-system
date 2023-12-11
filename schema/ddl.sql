CREATE TABLE user (
    user_id CHAR(36) PRIMARY KEY,
    user_name VARCHAR(25) NOT NULL,
    email_id VARCHAR(40) UNIQUE NOT NULL,
    phone_number VARCHAR(10) UNIQUE,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    gender ENUM('Male', 'Female', 'Prefer not to say'),
    date_of_birth DATE NOT NULL,
    profile_image varchar(255),
    bio VARCHAR(255),
    is_verified BOOLEAN,
    is_active BOOLEAN,
    is_reported BOOLEAN
);

CREATE TABLE user_auth (
    user_id CHAR(36) PRIMARY KEY,
    user_name VARCHAR(25) NOT NULL,
    email_id VARCHAR(40) UNIQUE NOT NULL,
    profile_password VARCHAR(30),
    ip_address VARCHAR(45),
    login_time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE report (
    report_id CHAR(36) PRIMARY KEY,
    category ENUM('Harassment', 'Spam', 'Inappropriate Content', 'Abuse/Bullying', 'Threats', 'Impersonation'),
    report_reason VARCHAR(255),
    created_at TIMESTAMP,
    reported_by CHAR(36),
    reported_profile CHAR(36),
    FOREIGN KEY (reported_by) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (reported_profile) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE device (
    device_id INT PRIMARY KEY,
    user_id CHAR(36),
    device_type ENUM('Andriod', 'Iphone', 'Desktop', 'Smart Watch', 'Tablet', 'Laptop'),
    device_name VARCHAR(20),
    created_at TIMESTAMP,
    is_logged_in BOOLEAN,
    device_token VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE messages (
    message_id INT PRIMARY KEY,
    sender_id CHAR(36),
    receiver_id CHAR(36),
    message_type ENUM('Text', 'Image', 'Video', 'Emoji', 'Location', 'File', 'GIF', 'Audio') NOT NULL,
    message_content VARCHAR(1000) NOT NULL,
    created_at TIMESTAMP,
    attachment_url VARCHAR(255),
    location VARCHAR(255),
    ip_address VARCHAR(45),
    FOREIGN KEY (sender_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE followers (
    follower_id CHAR(36) PRIMARY KEY,
    follower_user_id CHAR(36),
    following_user_id CHAR(36),
    time_stamp TIMESTAMP,
    FOREIGN KEY (follower_user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (following_user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE posts (
    post_id CHAR(36) PRIMARY KEY,
    post_content VARCHAR(255),
    created_at TIMESTAMP,
    author CHAR(36),
    caption VARCHAR(255),
    location VARCHAR(255),
    FOREIGN KEY (author) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE video (
    video_id CHAR(36) PRIMARY KEY,
    post_id CHAR(36),
    video_url VARCHAR(255),
    video_description VARCHAR(255),
    created_at TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE photo (
    photo_id CHAR(36) PRIMARY KEY,
    post_id CHAR(36),
    photo_url VARCHAR(255),
    photo_description VARCHAR(255),
    created_at TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE likes (
    like_id INT PRIMARY KEY,
    created_at TIMESTAMP,
    user_id CHAR(36),
    post_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE bookmarks (
    bookmark_id CHAR(36) PRIMARY KEY,
    created_at TIMESTAMP,
    user_id CHAR(36),
    post_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE comments (
    comment_id CHAR(36) PRIMARY KEY,
    comment_content VARCHAR(255) NOT NULL,
    created_at TIMESTAMP,
    user_id CHAR(36),
    post_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE comment_likes (
    comment_like_id INT PRIMARY KEY,
    comment_id CHAR(36),
    user_id CHAR(36),
    created_at TIMESTAMP,
    FOREIGN KEY (comment_id) REFERENCES comments(comment_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE comment_reply (
    comment_reply_id CHAR(36) PRIMARY KEY,
    comment_id CHAR(36),
    reply_text VARCHAR(500) NOT NULL,
    post_id CHAR(36),
    user_id CHAR(36),
    created_at TIMESTAMP,
    FOREIGN KEY (comment_id) REFERENCES comments(comment_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE tag (
    tag_id INT PRIMARY KEY,
    tag_text TEXT,
    post_id CHAR(36),
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);


CREATE TABLE repost (
    repost_id INT PRIMARY KEY,
    post_id CHAR(36),
    created_at TIMESTAMP,
    user_id CHAR(36),
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE mentions (
    mention_id INT PRIMARY KEY,
    mentioned_by CHAR(36),
    mentioned_user CHAR(36),
    created_at TIMESTAMP,
    post_id CHAR(36),
    FOREIGN KEY (mentioned_by) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (mentioned_user) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE groupss (
    group_id CHAR(36) PRIMARY KEY,
    group_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP,
    count INT,
    permission BOOLEAN,
    privacy ENUM('Private', 'Public')
);

CREATE TABLE group_members (
    group_id CHAR(36),
    user_id CHAR(36),
    joined_on TIMESTAMP,
    PRIMARY KEY (group_id, user_id),
    FOREIGN KEY (group_id) REFERENCES groupss(group_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE block_list (
    id INT PRIMARY KEY,
    blocked_by CHAR(36),
    blocked_user CHAR(36),
    created_at TIMESTAMP,
    FOREIGN KEY (blocked_by) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (blocked_user) REFERENCES user(user_id) ON DELETE CASCADE
);


