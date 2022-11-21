--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE market_db;




--
-- Drop roles
--

DROP ROLE "user";


--
-- Roles
--

CREATE ROLE "user";
ALTER ROLE "user" WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md57cb454f16772e66186a8b39142d739a2';






--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 13.7 (Debian 13.7-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: user
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO "user";

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: user
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: user
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: user
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "market_db" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 13.7 (Debian 13.7-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: market_db; Type: DATABASE; Schema: -; Owner: user
--

CREATE DATABASE market_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE market_db OWNER TO "user";

\connect market_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "user";

--
-- Name: categories; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.categories (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.categories OWNER TO "user";

--
-- Name: items; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.items (
    id uuid DEFAULT gen_random_uuid() NOT NULL,
    title text NOT NULL,
    cost double precision NOT NULL
);


ALTER TABLE public.items OWNER TO "user";

--
-- Name: items_categories; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.items_categories (
    item_id uuid NOT NULL,
    category_id uuid NOT NULL
);


ALTER TABLE public.items_categories OWNER TO "user";

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.alembic_version (version_num) FROM stdin;
944778bc5ad6
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.categories (id, title) FROM stdin;
b20f6c34-6d02-48c9-a1d8-f73659bd6a24	оргтехника
e60e39a0-cb3c-4b82-bf24-7fc484b92e3b	принтеры
21f9d8c1-217e-4a3b-863d-c6405921da97	компьютеры
0eedd06b-1e3d-4a04-90ce-8f1ddfa47089	ноутбуки
90b63e20-b045-4096-b0d5-210b33bb02f6	одежда
\.


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.items (id, title, cost) FROM stdin;
504fae5c-93b2-42a2-af9f-d25b9c3575c9	принтер epson 1	15999
aa3f56cb-98c7-48a9-b641-1b8d64ee9345	ноутбук lenovo 1	80999
ad15955a-1cff-49bc-b4e5-00236d566680	валенок	100
eddfd393-7b00-4477-bb29-577a5ba5cc79	чебурашка	100
460dd131-8cb8-4edb-bef4-687b41b9d29f	ноутбук ASUS 1	99999.99
f45e9772-75ae-4342-8a8e-1268cef0cc7a	компьютер ...	89999
a709b548-c874-4363-a461-b81337114077	варежки шерстянные	199
\.


--
-- Data for Name: items_categories; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.items_categories (item_id, category_id) FROM stdin;
504fae5c-93b2-42a2-af9f-d25b9c3575c9	b20f6c34-6d02-48c9-a1d8-f73659bd6a24
504fae5c-93b2-42a2-af9f-d25b9c3575c9	e60e39a0-cb3c-4b82-bf24-7fc484b92e3b
aa3f56cb-98c7-48a9-b641-1b8d64ee9345	b20f6c34-6d02-48c9-a1d8-f73659bd6a24
aa3f56cb-98c7-48a9-b641-1b8d64ee9345	21f9d8c1-217e-4a3b-863d-c6405921da97
aa3f56cb-98c7-48a9-b641-1b8d64ee9345	0eedd06b-1e3d-4a04-90ce-8f1ddfa47089
ad15955a-1cff-49bc-b4e5-00236d566680	90b63e20-b045-4096-b0d5-210b33bb02f6
460dd131-8cb8-4edb-bef4-687b41b9d29f	b20f6c34-6d02-48c9-a1d8-f73659bd6a24
460dd131-8cb8-4edb-bef4-687b41b9d29f	21f9d8c1-217e-4a3b-863d-c6405921da97
460dd131-8cb8-4edb-bef4-687b41b9d29f	0eedd06b-1e3d-4a04-90ce-8f1ddfa47089
f45e9772-75ae-4342-8a8e-1268cef0cc7a	b20f6c34-6d02-48c9-a1d8-f73659bd6a24
f45e9772-75ae-4342-8a8e-1268cef0cc7a	21f9d8c1-217e-4a3b-863d-c6405921da97
a709b548-c874-4363-a461-b81337114077	90b63e20-b045-4096-b0d5-210b33bb02f6
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: items_categories items_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.items_categories
    ADD CONSTRAINT items_categories_pkey PRIMARY KEY (item_id, category_id);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- Name: ix_categories_title; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX ix_categories_title ON public.categories USING btree (title);


--
-- Name: ix_items_categories_category_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_items_categories_category_id ON public.items_categories USING btree (category_id);


--
-- Name: ix_items_categories_item_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_items_categories_item_id ON public.items_categories USING btree (item_id);


--
-- Name: ix_items_title; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX ix_items_title ON public.items USING btree (title);


--
-- Name: items_categories items_categories_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.items_categories
    ADD CONSTRAINT items_categories_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: items_categories items_categories_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.items_categories
    ADD CONSTRAINT items_categories_item_id_fkey FOREIGN KEY (item_id) REFERENCES public.items(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 13.7 (Debian 13.7-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: user
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO "user";

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: user
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

