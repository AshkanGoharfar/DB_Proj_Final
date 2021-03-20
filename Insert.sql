-- DROP TABLE account_system_info , books, borrow_history, log_history, publisher;
-- DROP TABLE account_personal_info;
-- DROP TABLE account_system_info, books;
DROP TABLE borrow_history;


-- DELETE FROM `account_personal_info` WHERE `p_id`='1111111';

INSERT INTO books(pub_id, pub_address, pub_website) VALUES (11,'Math','educational',20,200,1,'ashkan');

INSERT INTO borrow_history(borr_id, b_id, limit_days, borr_cost, isbacked) VALUES (2,1,10,1000, 0);

INSERT INTO account_system_info (p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job)
VALUES ('2', 'asad', 'aaa', '10-02-2021', '1000', 'A', 'sdsd', '09121010101', 'Iran-Teran', 'Instructor', 'AmirKabir');

INSERT INTO books(b_id, b_title, b_category, b_num_of_pages, b_price, pub_id, b_author) VALUES (43,'Scince','educational',20,400,2,'hassan');

INSERT INTO account_system_info(p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job) 
VALUES (43, 'ash', 'kkk', '08-03-2021', 5000, 'khkh', 'khjgkgkg', '09121010198', 'Iran-Teran-4', 'student', 'AmirKabir');

INSERT INTO account_system_info (p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job)
VALUES ('3', 'bvr', 'ddd', '10-03-2021', '2000', 'naghi', 'wewe', '09121010101', 'Iran-Teran-1', 'student', 'AmirKabir');

INSERT INTO account_system_info (p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job)
VALUES ('4', 'aaad', 'bbb', '10-01-2021', '3000', 'mohammad', 'dfdfs', '09121010101', 'Iran-Teran-2', 'student', 'AmirKabir');

INSERT INTO account_system_info (p_id, username, password, created_day, budget, first_name, last_name, phone, address, user_type , uni_job)
VALUES ('5', 'ash', 'ccc', '10-01-2021', '4000', 'ali', 'arr', '09123556778', 'Iran-Teran-3', 'regular', 'AmirKabir');

-- 

select * from db_final_proj.account_system_info;

