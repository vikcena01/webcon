CREATE OR REPLACE FUNCTION auth_admin(text,text) 
RETURNS INTEGER AS 
'
DECLARE
arg_login ALIAS FOR $1;
arg_passwd_hash ALIAS FOR $2;
loc_id INTEGER;
loc_passwd_hash TEXT;
loc_active BOOL;
BEGIN
	SELECT INTO loc_id,loc_passwd_hash,loc_active id,passwd_hash,active FROM admin WHERE login LIKE arg_login;
	IF FOUND THEN
		IF loc_active = FALSE THEN
			-- admin zablokowany
			RETURN -2;
		END IF;
		IF loc_passwd_hash = arg_passwd_hash THEN
			-- jest ok
			UPDATE admin SET last_good_login=NOW() WHERE id=loc_id;
			RETURN loc_id;
		END IF;
		UPDATE admin SET last_bad_login=NOW() WHERE id=loc_id;
		RETURN -3;
	END IF;

	-- nieznany login
	RETURN -1;
END;
' 
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION auth_user(text,text) 
RETURNS INTEGER AS 
'
DECLARE
arg_email ALIAS FOR $1;
arg_passwd_hash ALIAS FOR $2;
loc_id INTEGER;
loc_passwd_hash TEXT;
loc_active BOOL;
BEGIN
	SELECT INTO loc_id,loc_passwd_hash,loc_active id,passwd_hash,active FROM public.user WHERE email LIKE arg_email;
	IF FOUND THEN
		IF loc_active = FALSE THEN
			-- user zablokowany
			RETURN -2;
		END IF;
		IF loc_passwd_hash = arg_passwd_hash THEN
			-- jest ok
			UPDATE public.user SET last_good_login=NOW() WHERE id=loc_id;
			RETURN loc_id;
		END IF;
		UPDATE public.user SET last_bad_login=NOW() WHERE id=loc_id;
		RETURN -3;
	END IF;

	-- nieznany login
	RETURN -1;
END;
' 
LANGUAGE 'plpgsql';

