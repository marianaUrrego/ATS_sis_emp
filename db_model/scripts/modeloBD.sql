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
 
create table core.usuarios (
	correo varchar(100) primary key,
	contraseña varchar (300) not null
)

create table core.departamentos (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null unique
);

create table core.aplicantes (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(30) not null ,
	correo varchar(100) not null unique,
    cv varchar(100) not null
);

create table core.titulos (
    id uuid default gen_random_uuid() primary key,
    nombre varchar(50) not null unique
);

create table core.estados (
    id integer generated always as identity primary key,
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

create table core.ofertas (
	 id uuid default gen_random_uuid() primary key,
	 nombre varchar(50) not null,
	 id_departamento uuid not null constraint departamento_fk references core.departamentos(id),
	 perfil varchar(300) not null,
	 fecha_creacion date not null
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
	descripcion varchar not null ,
	primary key (id_oferta,descripcion)
);

-- insertar todos los estados disponibles

insert into core.estados (nombre)
values('Aceptado'),('Rechazado'),('Por revisar'),('Fase de prueba'),('Fase de entrevista'),('Finalista');

-- procedimientos para la insersión de datos

create or replace procedure core.p_insertar_departamento(
    param_nombre text
)
language plpgsql
as 
$$
declare
    total_repetidos integer;
begin

    -- Se comprueban nulos o en blanco
    if param_nombre is null or length(param_nombre) = 0 
	then
    	raise exception 'El nombre no puede ser nulo o en blanco';
    end if;

    -- Se comprueban si esta repetido
    select count(id) into total_repetidos
        from core.departamentos
        where lower(nombre) = lower(param_nombre);
    
    if total_repetidos > 0  
	then
        raise exception 'Ya existe un departamento con ese nombre';
    end if;

    insert into core.departamentos (nombre)
        values (param_nombre);
end;
$$;

create or replace procedure core.insertar_requisitos_oferta(
	param_id_oferta uuid,
	param_habilidades_blandas text[],
	param_habilidades_tecnicas text[],
	param_titulos text[],
	param_experiencia text[]
)
language plpgsql
as 
$$
declare
	total_registros integer;
	id_temporal uuid;
begin
	-- se comprueba que la oferta si existe:
	select count(id) into total_registros
        from core.ofertas
		where id = param_id_oferta;
	
	if total_registros = 0  then
        raise exception 'no existe una oferta con ese id';
    end if;
	-- se ingresan todos los requisitos en las tablas:
	FOREACH item IN ARRAY param_habilidades_blandas LOOP
		begin
			select count(id) into total_registros
			from core.habilidades_blandas
			where lower(nombre) = lower(item);

			if(total_registros) = 0 then
				insert into core.habilidades_blandas(nombre) values(item);
			end if;

			select id into id_temporal
			from core.habilidades_blandas
			where lower(nombre) = lower(item);

			insert into core.habilidades_blandasxoferta(id_oferta,id_hab_blanda) values(param_id_oferta,id_temporal);
		end;
    END LOOP;

	FOREACH item IN ARRAY param_habilidades_tecnicas LOOP
		begin
			select count(id) into total_registros
			from core.habilidades_tecnicas
			where lower(nombre) = lower(item);

			if(total_registros) = 0 then
				insert into core.habilidades_tecnicas(nombre) values(item);
			end if;

			select id into id_temporal
			from core.habilidades_tecnicas
			where lower(nombre) = lower(item);

			insert into core.habilidades_tecnicasxoferta(id_oferta,id_hab_tecnica) values(param_id_oferta,id_temporal);
		end;
    END LOOP;

	FOREACH item IN ARRAY param_titulos LOOP
		begin
			select count(id) into total_registros
			from core.titulos
			where lower(nombre) = lower(item);

			if(total_registros) = 0 then
				insert into core.titulos(nombre) values(item);
			end if;

			select id into id_temporal
			from core.titulos
			where lower(nombre) = lower(item);

			insert into core.titulosxoferta(id_oferta,id_titulo) values(param_id_oferta,id_temporal);
		end;
    END LOOP;

	FOREACH item IN ARRAY param_experiencia LOOP
		begin
			select count(id) into total_registros
			from core.experiencia
			where lower(descripcion) = lower(item);

			if(total_registros) = 0 then
				insert into core.titulos(id_oferta,descripcion) values(param_id_oferta,item);
			end if;

		end;
    END LOOP;
end;
$$;


create or replace procedure core.p_insertar_oferta(
    param_nombre text,
    param_departamento text,
    param_perfil text
)
language plpgsql
as 
$$
declare
    total_registros integer;
	id_departamento uuid;
begin

    -- Se comprueban nulos o en blanco
    if param_nombre is null or length(param_nombre) = 0 then
        raise exception 'El nombre no puede ser nulo o en blanco';
	elsif param_departamento is null or length(param_departamento) = 0 then
		raise exception 'El departamento no puede ser nulo o en blanco';
	elsif param_perfil is null or length( param_perfil) = 0 then
		raise exception 'EL perfil no puede estar nulo o en blanco';
    end if;

    -- Se comprueban si esta repetido
    select count(id) into total_registros
        from core.ofertas
        where lower(nombre) = lower(param_nombre);
    
    if total_registros > 0  then
        raise exception 'Ya existe una oferta con ese nombre';
    end if;
	-- se comprueba que exista el departamento
	select count(id) into total_registros
    from core.departamentos
    where lower(nombre) = lower(param_departamento);
   	
    if total_registros = 0 then
        raise exception 'No existe un departamento registrado con ese nombre';
    end if;
   
	select id into id_departamento 
	from core.departamentos
	where lower(nombre) = lower(param_departamento);

    insert into core.ofertas (nombre,id_departamento, perfil)
        values (param_nombre, id_departamento,param_perfil, CURRENT_DATE);
end;
$$;


CREATE OR REPLACE PROCEDURE core.p_insertar_aplicacion(IN param_nombre text, IN param_correo text, IN param_cv text, IN param_id_oferta uuid, IN param_id_estado uuid)
 LANGUAGE plpgsql
AS $procedure$
declare
	total_registros integer;
	param_id_aplicante uuid;
begin

    -- Se comprueban nulos o en blanco
    if param_nombre is null or length(param_nombre) = 0 then
    	raise exception 'El nombre no puede ser nulo o en blanco';
	elsif param_correo is null or length(param_correo) = 0 then
		raise exception 'El correo electrónico no puede ser nulo';
	elsif param_cv is null or length(param_cv)= 0 then
		raise exception 'El CV no puede ser nulo o en blanco';
	elsif param_id_oferta is null then
		raise exception 'El campo de la oferta no puede ser nulo o en blanco';
	elsif param_id_estado is null then
		raise exception 'El campo de la oferta no puede ser nulo o en blanco';
    end if;

	-- se comprueba si la oferta existe
	select count(id) into total_registros
	from core.ofertas
	where id = param_id_oferta;

	if total_registros = 0 then
		raise exception 'No existe una oferta con este ID' ;
	end if;
	
	-- se comprueba si existe una aplicación de la persona a la oferta
	select count(id) into total_registros
    from core.aplicaciones as apc inner join core.aplicantes as apl on apc.id_aplicante = apl.id
    where id_oferta = param_id_oferta and apl.correo = param_correo ;
    
    if total_registros > 0  then
        raise exception 'Ya existe una aplicación de esta persona a la oferta seleccionada';
	end if;

	-- se comprueba si la persona ya está en la base de datos de aplicantes
	select count(id) into total_registros 
	from core.aplicantes
	where correo = param_correo;

	-- si no, se ingresa a la tabla
	if total_registros = 0 then
		insert into core.aplicantes (nombre,cv,correo)
        values (param_nombre,param_cv,param_correo);
	end if;
	-- se obtiene el id del aplicante
	select id into param_id_aplicante
		from core.aplicantes
		where nombre = param_nombre;
	-- se insertan los datos en la tabla
	insert into core.aplicaciones(id_aplicante,id_oferta, fecha_aplicacion,id_estado)
	values (param_id_aplicante ,param_id_oferta, CURRENT_DATE,param_id_estado);

end;
$procedure$
;
