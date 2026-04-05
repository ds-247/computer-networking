from faker import Faker
import random
import csv
from datetime import datetime, timedelta, date


def _random_date_between(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, max(delta.days, 0)))


def generate_customers(n, start_id=1, seed=None):
    if seed is not None:
        random.seed(seed)
    fake = Faker()
    if seed is not None:
        fake.seed_instance(seed)
    rows = []
    today = date.today()
    earliest = today - timedelta(days=365 * 90)
    created_earliest = today - timedelta(days=365 * 12)
    for i in range(n):
        cid = start_id + i
        name = fake.name().split()
        first = name[0]
        last = name[-1]
        dob = _random_date_between(earliest, today - timedelta(days=365 * 18))
        city = fake.city()
        created_at = _random_date_between(created_earliest, today)
        rows.append((cid, first, last, dob.isoformat(), city, created_at.isoformat()))
    return rows


def generate_accounts(n, customer_ids, start_id=1, seed=None):
    if seed is not None:
        random.seed(seed + 1)
    account_types = ['checking', 'savings', 'money_market', 'business']
    statuses = ['active', 'closed', 'dormant', 'suspended']
    rows = []
    cid_list = list(customer_ids)
    m = len(cid_list)
    assigned = []
    for i in range(n):
        aid = start_id + i
        if i < m:
            cust = cid_list[i]
        else:
            cust = random.choice(cid_list)
        acct_type = random.choices(account_types, weights=[50,40,5,5])[0]
        if acct_type == 'checking':
            bal = round(random.gauss(2000, 5000), 2)
        elif acct_type == 'savings':
            bal = round(random.gauss(12000, 20000), 2)
        else:
            bal = round(random.gauss(5000, 10000), 2)
        bal = max(0.0, round(bal, 2))
        status = random.choices(statuses, weights=[85,8,5,2])[0]
        opened_date = _random_date_between(date.today() - timedelta(days=365*12), date.today()).isoformat()
        rows.append((aid, cust, acct_type, f"{bal:.2f}", status, opened_date))
        assigned.append(aid)
    return rows


def generate_transactions(n, account_ids, start_id=1, seed=None):
    if seed is not None:
        random.seed(seed + 2)
    txn_types = ['deposit', 'withdrawal', 'transfer', 'payment', 'fee']
    statuses = ['completed', 'pending', 'failed', 'reversed']
    rows = []
    now = datetime.now()
    earliest = now - timedelta(days=365 * 5)
    for i in range(n):
        tid = start_id + i
        acct = random.choice(account_ids)
        ttype = random.choices(txn_types, weights=[35,35,15,10,5])[0]
        if ttype == 'fee':
            amt = round(random.uniform(0.5, 50.0), 2)
        elif ttype == 'withdrawal':
            amt = round(random.expovariate(1/200) + 1, 2)
        elif ttype == 'deposit':
            amt = round(random.expovariate(1/500) + 1, 2)
        elif ttype == 'transfer':
            amt = round(random.expovariate(1/800) + 5, 2)
        else:
            amt = round(random.expovariate(1/300) + 1, 2)
        txn_date = earliest + timedelta(seconds=random.randint(0, int((now - earliest).total_seconds())))
        status = random.choices(statuses, weights=[90,6,3,1])[0]
        rows.append((tid, acct, ttype, f"{amt:.2f}", txn_date.strftime('%Y-%m-%d %H:%M:%S'), status))
    return rows


def generate_loans(n, customer_ids, start_id=1, seed=None):
    if seed is not None:
        random.seed(seed + 3)
    loan_types = ['personal', 'mortgage', 'auto', 'student', 'business']
    statuses = ['active', 'paid', 'defaulted', 'delinquent']
    rows = []
    for i in range(n):
        lid = start_id + i
        cust = random.choice(list(customer_ids))
        ltype = random.choices(loan_types, weights=[25,30,20,15,10])[0]
        if ltype == 'mortgage':
            amt = round(random.uniform(80000, 600000), 2)
            rate = round(random.uniform(2.5, 5.5), 2)
        elif ltype == 'auto':
            amt = round(random.uniform(5000, 80000), 2)
            rate = round(random.uniform(3.0, 9.0), 2)
        elif ltype == 'student':
            amt = round(random.uniform(1000, 120000), 2)
            rate = round(random.uniform(1.0, 6.0), 2)
        elif ltype == 'business':
            amt = round(random.uniform(10000, 500000), 2)
            rate = round(random.uniform(3.0, 12.0), 2)
        else:
            amt = round(random.uniform(500, 50000), 2)
            rate = round(random.uniform(4.0, 16.0), 2)
        status = random.choices(statuses, weights=[70,20,5,5])[0]
        rows.append((lid, cust, ltype, f"{amt:.2f}", f"{rate:.2f}", status))
    return rows


def generate_cards(n, customer_ids, start_id=1, seed=None):
    if seed is not None:
        random.seed(seed + 4)
    card_types = ['Visa', 'Mastercard', 'Amex', 'Discover']
    rows = []
    for i in range(n):
        cid = start_id + i
        cust = random.choice(list(customer_ids))
        ctype = random.choices(card_types, weights=[45,45,7,3])[0]
        if ctype == 'Amex':
            limit_amt = round(random.uniform(2000, 50000), 2)
        else:
            limit_amt = round(random.uniform(500, 30000), 2)
        issued_date = _random_date_between(date.today() - timedelta(days=365*8), date.today()).isoformat()
        rows.append((cid, cust, ctype, f"{limit_amt:.2f}", issued_date))
    return rows


def _write_csv(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)


if __name__ == '__main__':
    suggested = {
        'customers': 2000,
        'accounts': 3500,
        'transactions': 5000,
        'loans': 1500,
        'cards': 2000,
    }
    seed = 42
    customers = generate_customers(suggested['customers'], start_id=1, seed=seed)
    customer_ids = [r[0] for r in customers]
    accounts = generate_accounts(suggested['accounts'], customer_ids, start_id=1, seed=seed)
    account_ids = [r[0] for r in accounts]
    transactions = generate_transactions(suggested['transactions'], account_ids, start_id=1, seed=seed)
    loans = generate_loans(suggested['loans'], customer_ids, start_id=1, seed=seed)
    cards = generate_cards(suggested['cards'], customer_ids, start_id=1, seed=seed)
    _write_csv('customers.csv', ['customer_id','first_name','last_name','dob','city','created_at'], customers)
    _write_csv('accounts.csv', ['account_id','customer_id','account_type','balance','status','opened_date'], accounts)
    _write_csv('transactions.csv', ['txn_id','account_id','txn_type','amount','txn_date','status'], transactions)
    _write_csv('loans.csv', ['loan_id','customer_id','loan_type','loan_amount','interest_rate','status'], loans)
    _write_csv('cards.csv', ['card_id','customer_id','card_type','limit_amount','issued_date'], cards)
    print('Wrote CSVs: customers.csv, accounts.csv, transactions.csv, loans.csv, cards.csv')
