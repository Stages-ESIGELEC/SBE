CREATE TABLE structure (
    id_structure INT NOT NULL PRIMARY KEY,
    nom VARCHAR(100),
    description VARCHAR(100000),
    description_courte VARCHAR(1000),
    logo BLOB,
    adresse VARCHAR(1000),
    contact VARCHAR(10),
    annee_creation DATE,
    type BOOLEAN,
    propriete BOOLEAN,
    id_secteur INT NOT NULL,
    id_tranche_employe INT NOT NULL,
    id_chiffre_affaire INT NOT NULL,
    FOREIGN KEY (id_secteur) REFERENCES secteur(id_secteur),
    FOREIGN KEY (id_tranche_employe) REFERENCES tranche_employe(id_tranche_employe),
    FOREIGN KEY (id_chiffre_affaire) REFERENCES chiffre_affaire(id_chiffre_affaire)
);

CREATE TABLE zone_implentation (
    id_zone INT NOT NULL PRIMARY KEY,
    zone_geographique VARCHAR(50)
);

CREATE TABLE service (
    id_structure INT NOT NULL,
    id_zone INT NOT NULL,
    PRIMARY KEY (id_structure, id_zone),
    FOREIGN KEY (id_structure) REFERENCES structure(id_structure),
    FOREIGN KEY (id_zone) REFERENCES zone_implentation(id_zone)
);

CREATE TABLE secteur (
    id_secteur INT NOT NULL PRIMARY KEY,
    valeur_secteur VARCHAR(50)
);

CREATE TABLE reseau_social (
    id_reseau INT NOT NULL PRIMARY KEY,
    type_reseau VARCHAR(50),
    url_reseau VARCHAR(1000),
    id_structure INT NOT NULL,
    FOREIGN KEY (id_structure) REFERENCES structure(id_structure)
);

CREATE TABLE tranche_employe (
    id_tranche_employe INT NOT NULL PRIMARY KEY,
    valeur_tranche VARCHAR(50)
);

CREATE TABLE tchiffre_affaire (
    id_chiffre_affaire INT NOT NULL PRIMARY KEY,
    valeur_chiffre_affaire VARCHAR(50)
);



