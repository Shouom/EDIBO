create database IF NOT EXISTS world;

use world;

CREATE TABLE IF NOT EXISTS Albumbs1
(	pkAlbumID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	Title NVARCHAR(160) NOT NULL,
    fkArtistId INTEGER NOT NULL,
    CONSTRAINT FK_ArtistIdAlbumbs1 FOREIGN KEY (fkArtistId) REFERENCES artists(pkArtistId)
		ON DELETE NO ACTION ON UPDATE NO ACTION);
    #Name NVARCHAR(120) NULL);

#insert into Artists(Name) values("First Artist")
#insert into Artists(Name) values("Second Artist")
UPDATE artists SET Name = 'Second One One Artist' WHERE (pkArtistId = 3);