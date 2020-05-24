use lefti_berzescuilie;

create procedure interogare2X_cursor(IN film varchar(45), OUT film_iesire text, OUT planeta_specii text)
begin
    begin
        declare filme varchar(250);
        declare director, prod varchar(450);
        declare done boolean default false;
        declare personaje, planeta, specii  text;
        declare c1 cursor for

        select distinct film_title Filmm, group_concat(distinct film_director) Director_Film, group_concat(distinct producer_name) Nume_Producator
            from starwars.film join starwars.film_producer fp on film.filmID = fp.filmID join starwars.producer using (producerID)
                where film_title = film
            group by film_title;
        declare c2 cursor for

        select film_title, group_concat(distinct people_name) Personaje,  group_concat(distinct planet_name) Nume_Planete, group_concat(distinct species_name) Specii
            from starwars.film join starwars.film_people fp on film.filmID = fp.filmID join starwars.people using (peopleID)
                join starwars.film_planet f on film.filmID = f.filmID join starwars.planet using (planetID)
                join starwars.film_species fs on film.filmID = fs.filmID join starwars.species using (speciesID)
                    where film_title=film
                        group by film_title;


        declare continue handler for not found set done = true;

        open c1;
        open c2;

        get_info_c1 : loop
            fetch c1 into filme, director, prod;
            fetch c2 into filme, personaje, planeta, specii;
                if done then
                    leave get_info_c1;
                end if;
        end loop;
        close c1;
        set film_iesire = concat('Filmul ', film, ' are directorul/directorii: ', director, ' si este produs de catre ',prod);
        set planeta_specii = concat('In filmul:', filme, ' au aparut urmatoarele personaje:', personaje, ' care se afla pe planetele: ',
            planeta, ' si care sunt din speciile:', specii);
    end;
end;


create procedure lefti_berzescuilie.Butoane(IN x varchar(150))
begin
    if x = 'Film' then
        select distinct film_title from starwars.film;
        elseif x = 'Ship' then
            select distinct starship_name from starwars.starship;
        elseif x = 'Vehicul' then
            select distinct vehicle_name from starwars.vehicle;
        elseif x = 'Specie' then
            select distinct species_name from starwars.species;
        elseif x = 'Clima' then
            select distinct planet_climate from starwars.climate;
        elseif x = 'Producatori' then
            select distinct producer_name from starwars.producer;
        elseif x = 'Planeta' then
            select distinct planet_name from starwars.planet;
    end if;
end;

call lefti_berzescuilie.Butoane('Film');
