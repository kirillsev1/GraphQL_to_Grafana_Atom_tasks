--DROP TABLE IF EXISTS missions cascade;
--DROP TABLE IF EXISTS rockets cascade;
--DROP TABLE IF EXISTS launches cascade;
CREATE TABLE IF NOT EXISTS rockets(
    id SERIAL PRIMARY KEY,
    name TEXT,
    type TEXT
);

CREATE TABLE IF NOT EXISTS missions(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS launches(
    id SERIAL PRIMARY KEY,
    rocket_id INTEGER REFERENCES rockets(id) ON DELETE CASCADE,
    mission_id INTEGER REFERENCES missions(id) ON DELETE CASCADE,
    launch_date_local TEXT
);
--
--ALTER TABLE launches OWNER TO atom_user;
--ALTER TABLE rockets OWNER TO atom_user;
--ALTER TABLE missions OWNER TO atom_user;
--GRANT UPDATE ON missions TO atom_user;
--GRANT UPDATE ON rockets TO atom_user;
--GRANT UPDATE ON launches TO atom_user;
--SELECT missions.name, rockets.name, launch_date_local FROM launches JOIN missions ON missions.id = mission_id JOIN rockets ON rocket _id=rockets.id;
