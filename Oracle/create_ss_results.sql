CREATE TABLE "SS_RESULTS"
(
'RESULT_ID' NUMBER  
'SURVEY_ID' NUMBER,
 'QUESTION_NUMBER' NUMBER,
 'ANSWER' VARCHAR2(255 CHAR),
 'SUBMITTED_BY' VARCHAR2(255 CHAR),
 'SUBMITTED_ON' TIMESTAMP,
CONSTRAINT "RESULT_ID_PK" PRIMARY KEY ("RESULT_ID")
USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
STOARGE (INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645)
PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
TABLESPACE "DWH_DATA" ENABLE
) SEGMENT CREATION IMMEDIATE
PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
.NOCOMPRESS LOGGING
STORAGE (INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645)
BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT
TABLESPACE "DWH_DATA"

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