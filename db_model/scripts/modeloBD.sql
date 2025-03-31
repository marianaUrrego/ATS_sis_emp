-- Abastecimiento (En la consola de comandos)
--  docker pull postgres:latest
--  docker run --name CompuestosQuimicos -e POSTGRES_PASSWORD=p4ssw0rd -d -p 5453:5432 postgres:latest

psql -U postgres -- (En la consola de Docker)

create database hireflowdb;

\c hireflowdb; -- se debe realizar la conexión a la base de datos

create schema core;

create user user_db with encrypted password 'c0ntr4s3n4';

grant connect on database hireflowdb to user_db;
grant temporary on database hireflowdb to user_db;
grant usage on schema core to user_db;
grant create on schema core to user_db;
grant select, references, insert, update, delete, trigger on all tables in schema core to user_db;
grant usage, select on all sequences in schema core to user_db;
grant execute on all functions in schema core to user_db;
grant execute on all procedures in schema core to user_db;
grant usage on schema information_schema to user_db;
grant references on all tables in schema core to user_db;

create user api_connection with encrypted password '4P1R3ST';

grant connect on database hireflowdb to api_connection;
grant usage on schema core to api_connection;
grant select, insert, update, delete on all tables in schema core to api_connection;
grant execute on all procedures in schema core to api_connection;

create extension if not exists "uuid-ossp";
 -- conectandose desde el usuario user_db
 
create extension if not exists "uuid-ossp";
 -- conectandose desde el usuario user_db
 
create table core.departamentos (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null unique
);

create table core.aplicantes (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null ,
    cv varchar(100) not null
);

create table core.titulos (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(50) not null unique
);

create table core.estados (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null unique
);

create table core.habilidades_blandas (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null unique
);

create table core.habilidades_tecnicas (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null unique
);

create table core.area (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null unique
);
create table core.ofertas (
	 id uuid default gen_random_uuid() primary key,
	 nombre varchar(50) not null,
	 id_departamento uuid not null constraint departamento_fk references core.departamentos(id),
	 perfil varchar(300) not null
);
create table core.aplicaciones (
	id_aplicante uuid not null constraint aplicantes_fk references core.aplicantes(id),
	id_oferta uuid not null constraint ofertas_fk references core.ofertas(id),
	fecha_aplicacion date not null,
	id_estado uuid not null constraint estados_fk references core.estados(id),
	primary key (id_aplicante,id_oferta)
);

create table core.titulosxoferta (
	id_oferta uuid not null constraint ofertas_fk references core.ofertas(id),
	id_titulo uuid not null constraint titulo_fk references core.titulos(id),
	primary key (id_titulo,id_oferta)
);

create table core.habilidades_blandasxoferta (
	id_oferta uuid not null constraint ofertas_fk references core.ofertas(id),
	id_hab_blanda uuid not null constraint id_hab_blanda_fk references core.habilidades_blandas(id),
	primary key (id_hab_blanda,id_oferta)
);

create table core.habilidades_tecnicasxoferta (
	id_oferta uuid not null constraint ofertas_fk references core.ofertas(id),
	id_hab_tecnica uuid not null constraint hab_tecnica_fk references core.habilidades_tecnicas(id),
	primary key (id_hab_tecnica,id_oferta)
);

create table core.experiencia (
	id_oferta uuid not null constraint ofertas_fk references core.ofertas(id),
	id_area uuid not null constraint hab_tecnica_fk references core.area(id),
	anios int not null ,
	primary key (id_area,id_oferta)
);