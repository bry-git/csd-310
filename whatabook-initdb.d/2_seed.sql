USE whatabook;

INSERT INTO user (first_name, last_name)
VALUES
    ('vince', 'vega'),
    ('robert', 'paulson'),
    ('tyler', 'durden');

INSERT INTO book (book_name, details, author)
VALUES
    ('The Great Gatsby', 'The novel chronicles an era that Fitzgerald himself dubbed the "Jazz Age". Following the shock and chaos of World War I, American society enjoyed unprecedented levels of prosperity during the roaring 20s', 'F. Scott Fitzgerald'),
    ('The Adventures of Huckleberry Finn', 'Revered by all of the towns children and dreaded by all of its mothers, Huckleberry Finn is indisputably the most appealing child-hero in American literature', 'Mark Twain'),
    ('Hamlet', 'The Tragedy of Hamlet, Prince of Denmark, or more simply Hamlet, is a tragedy by William Shakespeare, believed to have been written between 1599 and 1601.', 'William Shakespeare'),
    ('Moby Dick', ' First published in 1851, Melvilles masterpiece is, in Elizabeth Hardwicks words, "the greatest novel in American literature." The saga of Captain Ahab and his monomaniacal pursuit of the white whale', 'Herman Melville'),
    ('Don Quixote', 'Alonso Quixano, a retired country gentleman in his fifties, lives in an unnamed section of La Mancha with his niece and a housekeeper. He has become obsessed with books of chivalry', 'Miguel de Cervantes'),
    ('One Hundred Years of Solitude', 'One of the 20th century''s enduring works, One Hundred Years of Solitude is a widely beloved and acclaimed novel known throughout the world', 'Gabriel Garcia Marquez'),
    ('King Lear', 'King Lear is a tragedy by William Shakespeare, believed to have been written between 1603 and 1606. It is considered one of his greatest works.', 'William Shakespeare'),
    ('The Odyssey', 'The Odyssey is one of two major ancient Greek epic poems attributed to Homer. It is, in part, a sequel to the Iliad, the other work traditionally ascribed to Homer.', 'Homer'),
    ('Pride and Prejudice', 'The book is narrated in free indirect speech following the main character Elizabeth Bennet as she deals with matters of upbringing, marriage, moral rightness and education in her aristocratic society', 'Jane Austen');

INSERT INTO wishlist (user_id, book_id)
VALUES
    (1, 9), (2, 8), (3, 7),
    (1, 6), (2, 5), (3, 4),
    (1, 3), (2, 2), (3, 1);

INSERT INTO store (locale)
VALUES
    ('The Strand, 828 Broadway, New York City, NY 10003-4826');