CREATE OR REPLACE TRIGGER "TRIG_SS_RESULTS"
BEFORE INSERT ON SS_RESULTS
FOR EACH ROW
BEGIN
	SELECT SS_RESULT_ID.SEQ.NEXTVAL
	INTO :NEW.RESULT_ID
	FROM DUAL 
END;
/


ALTER TRIGGER "TRIG_SS_RESULTS" ENABLE;