-- Update db to v1.2 from v1.1
-- Sun, 30 Oct 2018, 08:28:55
-- Model: pyclub    Version: 1.2

ALTER TABLE event_membership
    DROP FOREIGN KEY fk_user_has_event_event1;

ALTER TABLE event_membership
    DROP COLUMN own_club_id;

ALTER TABLE user
    ALTER email_confirm SET DEFAULT 0;

ALTER TABLE club
    ADD COLUMN name varchar(100) NOT NULL UNIQUE;
    ADD COLUMN owner_id INT NOT NULL DEFAULT 0;

ALTER TABLE organization
    ADD UNIQUE (name);
    ADD COLUMN owner_id INT NOT NULL DEFAULT 0;

ALTER TABLE event
    ADD COLUMN owner_id INT NOT NULL DEFAULT 0;