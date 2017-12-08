DROP DATABASE printer;

CREATE DATABASE printer;

USE printer;


CREATE TABLE job_history(
  printer VARCHAR(50) ,
  filename VARCHAR(50) ,
  starttime VARCHAR(50)PRIMARY KEY,
  endtime VARCHAR(50),
  time_elapsed INT(50),
  status VARCHAR(15)
);

