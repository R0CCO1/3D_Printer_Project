DROP DATABASE printer;

CREATE DATABASE printer;

USE printer;

CREATE TABLE job_history(
  printer VARCHAR(50) ,
  filename VARCHAR(50) PRIMARY KEY,
  starttime VARCHAR(50),
  endtime VARCHAR(50),
  status VARCHAR(15)
);

/*INSERT INTO job_history VALUES
  ('gutenberg','ball.text','10:10','12:10','Success');
*/
