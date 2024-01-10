
CREATE TABLE `contact`.`mycontacts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` INT NULL,
  `email` VARCHAR(25) NULL,
  `phone` VARCHAR(10) NULL,
  PRIMARY KEY (`id`));

-- bla bla
SELECT `mycontacts`.`id`,
    `mycontacts`.`name`,
    `mycontacts`.`email`,
    `mycontacts`.`phone`
FROM `contact`.`mycontacts`
where name ='reou'
;

INSERT INTO `mycontacts` (`name`, `email`,`phone`)  VALUES  ('reou',"rhaddad95200@gmail.com","0585030899");


DELETE FROM `contact`.`mycontacts` WHERE name='reou';

UPDATE `contact`.`mycontacts`
SET
`name` = 'reou',
`email` = "rhaddad95200@gmail.com",
`phone` = "0585030899"
WHERE `id` =2;
