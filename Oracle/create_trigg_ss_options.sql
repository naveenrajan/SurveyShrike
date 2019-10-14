CREATE OR REPLACE TRIGGER "TRIG_SS_OPTIONS"
BEFORE INSERT ON SS_OPTIONS
FOR EACH ROW
BEGIN
	SELECT SS_OPTION_ID.SEQ.NEXTVAL
	INTO :NEW.OPTION_ID
	FROM DUAL 
END;
/


ALTER TRIGGER "TRIG_SS_OPTIONS" ENABLE;