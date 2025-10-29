create database postgres;

CREATE TABLE IF NOT EXISTS "CURRENCY_RATES"(
    id SERIAL PRIMARY KEY,
    currency_name VARCHAR(100),
    currency_code VARCHAR(3),
    rate DECIMAL(10, 4),
    effective_date DATE,
    UNIQUE (currency_code, effective_date)
);
select * from "CURRENCY_RATES";