-- Update db to v1.1 from v1.0
-- Sun, 7 Oct 2018, 16:55:55
-- Model: pyclub    Version: 1.1

USE 'pyclub';
ALTER TABLE user
    ADD IF NOT EXIST UNIQUE (email);

ALTER TABLE event_membership
    CHANGE COLUMN event_club_idclub own_club_id int(11);

ALTER TABLE user 
    ADD COLUMN email_confirm tinyint(1) NOT NULL;