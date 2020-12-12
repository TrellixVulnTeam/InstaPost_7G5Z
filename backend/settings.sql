-- settings.sql
CREATE DATABASE instapost;
CREATE USER instapostuser WITH PASSWORD 'instapost';
GRANT ALL PRIVILEGES ON DATABASE instapost TO instapostuser;