DROP DATABASE IF EXISTS pysports;

CREATE DATABASE pysports;

USE pysports;

DROP USER IF EXISTS 'pysports_user'@'%';

CREATE USER 'pysports_user'@'%' IDENTIFIED WITH mysql_native_password BY 'sqlpass';

GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'%';

# DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE TABLE team
(
    team_id   INT         NOT NULL AUTO_INCREMENT,
    team_name VARCHAR(75) NOT NULL,
    mascot    VARCHAR(75) NOT NULL,
    primary key (team_id)
);

DROP TABLE IF EXISTS player;

CREATE TABLE player
(
    player_id  INT         NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name  VARCHAR(75) NOT NULL,
    team_id    INT         NOT NULL,
    PRIMARY KEY (player_id),
    CONSTRAINT fk_team
        FOREIGN KEY (team_id) REFERENCES team (team_id)
);

SELECT team_id FROM team WHERE team_name = 'team sauron';

SELECT team_id FROM team WHERE team_name = 'team gandalf';

