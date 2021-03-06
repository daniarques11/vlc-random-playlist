--P02_VLC
--Daniel Arqués Toro, Daniel Jonathan Zurita Mena
CREATE DATABASE VLC;

USE VLC;

CREATE TABLE Artists (
    id VARCHAR(10) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) engine = InnoDB;

CREATE TABLE Band_Artists (
    band_id VARCHAR(10) NOT NULL,
    artist_id VARCHAR(10) NOT NULL,
    start_date year NOT NULL,
    end_date year,
    PRIMARY KEY (band_id, artist_id, start_date),
    FOREIGN KEY (band_id) REFERENCES Artists (id),
    FOREIGN KEY (artist_id) REFERENCES Artists (id)
) engine = InnoDB;

CREATE TABLE Albums (
    id int(10) NOT NULL,
    title VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) engine = InnoDB;

CREATE TABLE Media_Types (
    id int(2) NOT NULL,
    name VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
) engine = InnoDB;

CREATE TABLE Genres (
    id int(3) NOT NULL,
    name VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
) engine = InnoDB;

CREATE TABLE Playlists (
    id int(3) NOT NULL,
    name VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
) engine = InnoDB;

CREATE TABLE Album_Artists (
    id_album int(10) NOT NULL,
    id_artist VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_album, id_artist),
    FOREIGN KEY (id_album) REFERENCES Albums (id),
    FOREIGN KEY (id_artist) REFERENCES Artists (id)
) engine = InnoDB;

CREATE TABLE Tracks (
    id int(10) NOT NULL,
    name VARCHAR(50) NOT NULL,
    miliseconds REAL,
    bytes int(20),
    id_media_type int(2),
    id_genre int(3),
    path VARCHAR(200) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_media_type) REFERENCES Media_Types (id),
    FOREIGN KEY (id_genre) REFERENCES Genres (id)
) engine = InnoDB;

CREATE TABLE Album_Tracks (
    id_album int(10) NOT NULL,
    id_track int(10) NOT NULL,
    number_track int,
    PRIMARY KEY (id_album, id_track),
    FOREIGN KEY (id_album) REFERENCES Albums (id),
    FOREIGN KEY (id_track) REFERENCES Tracks (id)
) engine = InnoDB;

CREATE TABLE Track_Composers (
    id_track int(10) NOT NULL,
    id_artist VARCHAR(10) NOT NULL,
    year int(4),
    PRIMARY KEY (id_track, id_artist),
    FOREIGN KEY (id_track) REFERENCES Tracks (id),
    FOREIGN KEY (id_artist) REFERENCES Artists (id)
) engine = InnoDB;

CREATE TABLE Playlist_Tracks (
    id_playlist int(3) NOT NULL,
    id_track int(10) NOT NULL,
    number_track int NOT NULL,
    PRIMARY KEY (id_playlist, id_track),
    FOREIGN KEY (id_playlist) REFERENCES Playlists (id),
    FOREIGN KEY (id_track) REFERENCES Tracks (id)
) engine = InnoDB;

CREATE TABLE Track_Artists (
    id_track int(10) NOT NULL,
    id_artist VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_track, id_artist),
    FOREIGN KEY (id_track) REFERENCES Tracks (id),
    FOREIGN KEY (id_artist) REFERENCES Artists (id)
) engine = InnoDB;

insert into
    Artists
values
    ('CAT102', 'Manel'),
    ('CAT123', 'Guillem Gisbert Puig'),
    ('CAT219', 'Martí Maymo Tomàs'),
    ('CAT432', 'Roger Padilla Gutiérrez'),
    ('CAT541', 'Arnau Vallvé Socies'),
    ('US832091', 'Foreigner'),
    ('US44349', 'Lou Gramm'),
    ('EN28921', 'Mick Jones'),
    ('EN8973', 'Ian McDonald'),
    ('US2481240', 'Al Greenwood'),
    ('US2314553', 'Ed Gagliardi'),
    ('EN21245', 'Dennis Elliott'),
    ('US92113442', 'Imagine Dragons'),
    ('US9844239', 'Dan Reynolds'),
    ('US9924780', 'Wayne Sermon'),
    ('US10233120', 'Ben McKee'),
    ('US24432101', 'Daniel Platzman'),
    ('US90034511', 'John Hill'),
    ('ES7521', 'Antonio Flores');

insert into
    Band_Artists
values
    ('CAT102', 'CAT123', '2007', NULL),
    ('CAT102', 'CAT219', '2007', NULL),
    ('CAT102', 'CAT219', '2007', NULL),
    ('CAT102', 'CAT432', '2007', NULL),
    ('US832091', 'US44349', '1976', '1990'),
    ('US832091', 'US44349', '1992', '2003'),
    ('US832091', 'US44349', '2017', NULL),
    ('US832091', 'EN28921', '1976', NULL),
    ('US832091', 'EN8973', '1976', '1980'),
    ('US832091', 'EN8973', '2017', NULL),
    ('US832091', 'US2481240', '1976', '1980'),
    ('US832091', 'US2481240', '2017', NULL),
    ('US832091', 'US2314553', '1976', '1979'),
    ('US832091', 'EN21245', '1976', '1992'),
    ('US92113442', 'US9844239', '2008', NULL),
    ('US92113442', 'US9924780', '2009', NULL),
    ('US92113442', 'US10233120', '2009', NULL),
    ('US92113442', 'US24432101', '20011', NULL);

insert into
    Albums
values
    (19002, "Atletes, baixin de l'escenari"),
    (43120, 'Foreigner'),
    (1125556, 'Origins'),
    (93842, 'Antonio'),
    (19003, "Jo competeixo");

insert into
    Media_Types
values
    (1, 'mp3'),
    (2, 'wma'),
    (3, 'wmv'),
    (4, 'mp4'),
    (5, 'midi');

insert into
    Genres
values
    (15, 'Indie-pop'),
    (1, 'Rock'),
    (12, 'Pop Rock'),
    (68, 'Flamenco'),
    (32, 'Dark Metal');

insert into
    Playlists
values
    (1, 'Música variada'),
    (2, 'Català'),
    (3, 'Imagine Dragons'),
    (4, 'Rock'),
    (5, 'Toda mi música');

insert into
    Album_Artists
values
    (19002, 'CAT102'),
    (19002, 'CAT123'),
    (19002, 'CAT219'),
    (19002, 'CAT432'),
    (19002, 'CAT541'),
    (19003, 'CAT102'),
    (19003, 'CAT123'),
    (19003, 'CAT219'),
    (19003, 'CAT432'),
    (19003, 'CAT541'),
    (43120, 'US832091'),
    (43120, 'US44349'),
    (43120, 'EN28921'),
    (43120, 'US2481240'),
    (43120, 'US2314553'),
    (43120, 'EN21245'),
    (1125556, 'US92113442'),
    (1125556, 'US9924780'),
    (1125556, 'US10233120'),
    (1125556, 'US24432101'),
    (1125556, 'US9844239'),
    (93842, 'ES7521');

insert into
    Tracks
values
    (
        190029,
        'A veure què en fem',
        272000,
        3287401,
        1,
        15,
        'C:\Users\Thelpher\Desktop\DAW 1r\VLC Projecte\Musica\A veure que en fem.mp3'
    ),
    (
        431202,
        'Cold as Ice',
        199000,
        3321379,
        4,
        1,
        'C:\Users\Thelpher\Desktop\DAW 1r\VLC Projecte\Musica\Cold as Ice.mp3'
    ),
    (
        11255567,
        'Zero',
        210000,
        5320000,
        1,
        12,
        'C:\Users\Thelpher\Desktop\DAW 1r\VLC Projecte\Musica\Zero.mp4'
    ),
    (
        938421,
        'No dudaría',
        212000,
        2503295,
        3,
        68,
        'C:\Users\Thelpher\Desktop\DAW 1r\VLC Projecte\Musica\No dudaria.mp4'
    );

insert into
    Album_Tracks
values
    (19002, 190029, 9),
    (43120, 431202, 2),
    (1125556, 11255567, 7),
    (93842, 938421, 1);

insert into
    Track_Composers
values
    (190029, 'CAT123', 2013),
    (431202, 'US44349', 1977),
    (431202, 'EN28921', 1977),
    (11255567, 'US9844239', 2018),
    (11255567, 'US9924780', 2018),
    (11255567, 'US90034511', 2018),
    (938421, 'ES7521', 1980);

insert into
    Playlist_Tracks
values
    (1, 938421, 1),
    (1, 190029, 2),
    (1, 431202, 3),
    (1, 11255567, 4),
    (2, 190029, 2);

insert into
    Track_Artists
values
    (190029, 'CAT123'),
    (190029, 'CAT219'),
    (190029, 'CAT432'),
    (190029, 'CAT541'),
    (431202, 'US44349'),
    (431202, 'EN28921'),
    (431202, 'EN8973'),
    (431202, 'US2481240'),
    (431202, 'US2314553'),
    (431202, 'EN21245'),
    (11255567, 'US9844239'),
    (11255567, 'US9924780'),
    (11255567, 'US10233120'),
    (11255567, 'US24432101'),
    (11255567, 'US90034511'),
    (938421, 'ES7521');