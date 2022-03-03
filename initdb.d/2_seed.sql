USE pysports;

INSERT INTO team (team_name, mascot)
VALUES ('Team Gandalf', 'White Wizards'),
       ('Team Sauron', 'Orcs');

INSERT INTO player (first_name, last_name, team_id)
VALUES ('Thorin', 'Oakenshield', 1),
       ('Frodo', 'Baggins', 1),
       ('Bilbo', 'Baggins', 1),
       ('Saurumon', 'The White', 2),
       ('Angmar', 'the Witch King', 2),
       ('Azog', 'The Defiler', 2);