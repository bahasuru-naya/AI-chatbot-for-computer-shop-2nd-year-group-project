from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace <db_password> with the actual password
uri = "mongodb+srv://gpsd:helloworld@gpsd0.3fvcw.mongodb.net/?retryWrites=true&w=majority&appName=gpsd0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Step 1: Create a new database
db = client['loan_database']

# Step 2: Create collections (e.g., customers, loans, payments)
customers = db["customers"]
loans = db["loans"]
repayments = db["repayments"]
collateral = db["collateral"]
employees = db["employees"]
branches = db["branches"]
loan_applications = db["loan_applications"]
payments_schedule = db["payments_schedule"]


# Step 3: Insert sample data into the collections
customers.insert_many([
    {"customer_id": "CUST001", "first_name": "John", "last_name": "Doe", "date_of_birth": "1985-04-15", "address": "123 Main St, Cityville", "phone": "555-1234", "email": "johndoe@example.com", "national_id": "123456789"},
    {"customer_id": "CUST002", "first_name": "Jane", "last_name": "Smith", "date_of_birth": "1990-08-22", "address": "456 Oak St, Townsville", "phone": "555-5678", "email": "janesmith@example.com", "national_id": "987654321"},
    {"customer_id": "CUST003", "first_name": "Robert", "last_name": "Brown", "date_of_birth": "1982-11-30", "address": "789 Pine St, Cityville", "phone": "555-7890", "email": "robert.brown@example.com", "national_id": "234567890"},
    {"customer_id": "CUST004", "first_name": "Emily", "last_name": "Davis", "date_of_birth": "1975-06-14", "address": "321 Cedar St, Townsville", "phone": "555-3456", "email": "emily.davis@example.com", "national_id": "345678901"},
    {"customer_id": "CUST005", "first_name": "Michael", "last_name": "Wilson", "date_of_birth": "1992-10-21", "address": "654 Maple St, Cityville", "phone": "555-4321", "email": "michael.wilson@example.com", "national_id": "456789012"},
    {"customer_id": "CUST006", "first_name": "Sarah", "last_name": "Johnson", "date_of_birth": "1988-09-17", "address": "123 Elm St, Townsville", "phone": "555-8765", "email": "sarah.johnson@example.com", "national_id": "567890123"},
    {"customer_id": "CUST007", "first_name": "David", "last_name": "Moore", "date_of_birth": "1980-02-09", "address": "456 Birch St, Cityville", "phone": "555-9876", "email": "david.moore@example.com", "national_id": "678901234"},
    {"customer_id": "CUST008", "first_name": "Laura", "last_name": "Lee", "date_of_birth": "1993-01-13", "address": "789 Aspen St, Townsville", "phone": "555-3452", "email": "laura.lee@example.com", "national_id": "789012345"},
    {"customer_id": "CUST009", "first_name": "Daniel", "last_name": "Taylor", "date_of_birth": "1994-12-23", "address": "123 Spruce St, Cityville", "phone": "555-2345", "email": "daniel.taylor@example.com", "national_id": "890123456"},
    {"customer_id": "CUST010", "first_name": "Anna", "last_name": "Clark", "date_of_birth": "1987-07-29", "address": "456 Redwood St, Townsville", "phone": "555-6543", "email": "anna.clark@example.com", "national_id": "901234567"},
    {"customer_id": "CUST011", "first_name": "Peter", "last_name": "Martinez", "date_of_birth": "1979-03-15", "address": "789 Cypress St, Cityville", "phone": "555-7891", "email": "peter.martinez@example.com", "national_id": "234567891"},
    {"customer_id": "CUST012", "first_name": "Linda", "last_name": "Perez", "date_of_birth": "1983-04-10", "address": "321 Alder St, Townsville", "phone": "555-8901", "email": "linda.perez@example.com", "national_id": "345678912"},
    {"customer_id": "CUST013", "first_name": "James", "last_name": "Harris", "date_of_birth": "1978-01-20", "address": "654 Beech St, Cityville", "phone": "555-6540", "email": "james.harris@example.com", "national_id": "456789123"},
    {"customer_id": "CUST014", "first_name": "Jennifer", "last_name": "Hall", "date_of_birth": "1991-05-30", "address": "123 Willow St, Townsville", "phone": "555-1235", "email": "jennifer.hall@example.com", "national_id": "567890234"},
    {"customer_id": "CUST015", "first_name": "Mark", "last_name": "King", "date_of_birth": "1989-09-05", "address": "456 Fir St, Cityville", "phone": "555-4567", "email": "mark.king@example.com", "national_id": "678901345"},
    {"customer_id": "CUST016", "first_name": "Susan", "last_name": "Green", "date_of_birth": "1986-11-11", "address": "789 Oakwood St, Townsville", "phone": "555-3214", "email": "susan.green@example.com", "national_id": "789012456"},
    {"customer_id": "CUST017", "first_name": "George", "last_name": "Young", "date_of_birth": "1995-02-19", "address": "321 Maplewood St, Cityville", "phone": "555-4326", "email": "george.young@example.com", "national_id": "890123567"},
    {"customer_id": "CUST018", "first_name": "Jessica", "last_name": "Allen", "date_of_birth": "1981-08-12", "address": "654 Cedarwood St, Townsville", "phone": "555-5674", "email": "jessica.allen@example.com", "national_id": "901234678"},
    {"customer_id": "CUST019", "first_name": "Charles", "last_name": "Wright", "date_of_birth": "1984-10-02", "address": "123 Redwood Dr, Cityville", "phone": "555-7893", "email": "charles.wright@example.com", "national_id": "234567890"},
    {"customer_id": "CUST020", "first_name": "Karen", "last_name": "Scott", "date_of_birth": "1977-12-28", "address": "456 Elmwood Dr, Townsville", "phone": "555-8904", "email": "karen.scott@example.com", "national_id": "345678901"}
])

db.loans.insert_many([
  { "loan_id": "LOAN001", "customer_id": "CUST001", "loan_type": "personal", "principal_amount": 10000, "interest_rate": 5.5, "loan_term_months": 60, "start_date": "2023-01-15", "end_date": "2028-01-15", "loan_status": "active" },
  { "loan_id": "LOAN002", "customer_id": "CUST002", "loan_type": "mortgage", "principal_amount": 150000, "interest_rate": 3.7, "loan_term_months": 180, "start_date": "2022-05-01", "end_date": "2037-05-01", "loan_status": "approved" },
  { "loan_id": "LOAN003", "customer_id": "CUST003", "loan_type": "auto", "principal_amount": 25000, "interest_rate": 4.2, "loan_term_months": 36, "start_date": "2023-04-10", "end_date": "2026-04-10", "loan_status": "active" },
  { "loan_id": "LOAN004", "customer_id": "CUST004", "loan_type": "personal", "principal_amount": 15000, "interest_rate": 6.0, "loan_term_months": 48, "start_date": "2021-11-01", "end_date": "2025-11-01", "loan_status": "completed" },
  { "loan_id": "LOAN005", "customer_id": "CUST005", "loan_type": "mortgage", "principal_amount": 200000, "interest_rate": 3.9, "loan_term_months": 240, "start_date": "2023-06-01", "end_date": "2043-06-01", "loan_status": "approved" },
  { "loan_id": "LOAN006", "customer_id": "CUST006", "loan_type": "business", "principal_amount": 50000, "interest_rate": 7.5, "loan_term_months": 120, "start_date": "2023-07-15", "end_date": "2033-07-15", "loan_status": "active" },
  { "loan_id": "LOAN007", "customer_id": "CUST007", "loan_type": "personal", "principal_amount": 12000, "interest_rate": 5.0, "loan_term_months": 60, "start_date": "2022-01-20", "end_date": "2027-01-20", "loan_status": "active" },
  { "loan_id": "LOAN008", "customer_id": "CUST008", "loan_type": "auto", "principal_amount": 30000, "interest_rate": 4.8, "loan_term_months": 48, "start_date": "2021-10-15", "end_date": "2025-10-15", "loan_status": "completed" },
  { "loan_id": "LOAN009", "customer_id": "CUST009", "loan_type": "business", "principal_amount": 75000, "interest_rate": 6.2, "loan_term_months": 84, "start_date": "2022-08-01", "end_date": "2029-08-01", "loan_status": "active" },
  { "loan_id": "LOAN010", "customer_id": "CUST010", "loan_type": "personal", "principal_amount": 18000, "interest_rate": 5.7, "loan_term_months": 36, "start_date": "2023-05-01", "end_date": "2026-05-01", "loan_status": "approved" },
  { "loan_id": "LOAN011", "customer_id": "CUST011", "loan_type": "mortgage", "principal_amount": 250000, "interest_rate": 4.1, "loan_term_months": 360, "start_date": "2020-02-15", "end_date": "2050-02-15", "loan_status": "active" },
  { "loan_id": "LOAN012", "customer_id": "CUST012", "loan_type": "auto", "principal_amount": 22000, "interest_rate": 4.5, "loan_term_months": 36, "start_date": "2023-09-10", "end_date": "2026-09-10", "loan_status": "approved" },
  { "loan_id": "LOAN013", "customer_id": "CUST013", "loan_type": "personal", "principal_amount": 9000, "interest_rate": 6.3, "loan_term_months": 24, "start_date": "2021-04-01", "end_date": "2023-04-01", "loan_status": "completed" },
  { "loan_id": "LOAN014", "customer_id": "CUST014", "loan_type": "business", "principal_amount": 60000, "interest_rate": 7.0, "loan_term_months": 96, "start_date": "2022-06-15", "end_date": "2030-06-15", "loan_status": "active" },
  { "loan_id": "LOAN015", "customer_id": "CUST015", "loan_type": "personal", "principal_amount": 13000, "interest_rate": 5.4, "loan_term_months": 48, "start_date": "2023-03-01", "end_date": "2027-03-01", "loan_status": "approved" },
  { "loan_id": "LOAN016", "customer_id": "CUST016", "loan_type": "auto", "principal_amount": 28000, "interest_rate": 4.3, "loan_term_months": 60, "start_date": "2023-07-10", "end_date": "2028-07-10", "loan_status": "active" },
  { "loan_id": "LOAN017", "customer_id": "CUST017", "loan_type": "business", "principal_amount": 45000, "interest_rate": 7.2, "loan_term_months": 72, "start_date": "2022-03-01", "end_date": "2028-03-01", "loan_status": "delinquent" },
  { "loan_id": "LOAN018", "customer_id": "CUST018", "loan_type": "personal", "principal_amount": 17000, "interest_rate": 6.1, "loan_term_months": 60, "start_date": "2021-12-01", "end_date": "2026-12-01", "loan_status": "active" },
  { "loan_id": "LOAN019", "customer_id": "CUST019", "loan_type": "mortgage", "principal_amount": 180000, "interest_rate": 4.0, "loan_term_months": 240, "start_date": "2020-09-01", "end_date": "2040-09-01", "loan_status": "active" },
  { "loan_id": "LOAN020", "customer_id": "CUST020", "loan_type": "personal", "principal_amount": 20000, "interest_rate": 5.9, "loan_term_months": 60, "start_date": "2023-04-01", "end_date": "2028-04-01", "loan_status": "approved" }
]);


db.repayments.insert_many([
  { "repayment_id": "REPAY001", "loan_id": "LOAN001", "repayment_date": "2023-02-15", "amount_paid": 200, "principal_paid": 150, "interest_paid": 50, "remaining_balance": 9850 },
  { "repayment_id": "REPAY002", "loan_id": "LOAN001", "repayment_date": "2023-03-15", "amount_paid": 200, "principal_paid": 150, "interest_paid": 50, "remaining_balance": 9700 },
  { "repayment_id": "REPAY003", "loan_id": "LOAN002", "repayment_date": "2023-06-01", "amount_paid": 500, "principal_paid": 300, "interest_paid": 200, "remaining_balance": 149500 },
  { "repayment_id": "REPAY004", "loan_id": "LOAN002", "repayment_date": "2023-07-01", "amount_paid": 500, "principal_paid": 300, "interest_paid": 200, "remaining_balance": 149000 },
  { "repayment_id": "REPAY005", "loan_id": "LOAN003", "repayment_date": "2023-05-10", "amount_paid": 700, "principal_paid": 500, "interest_paid": 200, "remaining_balance": 24300 },
  { "repayment_id": "REPAY006", "loan_id": "LOAN003", "repayment_date": "2023-06-10", "amount_paid": 700, "principal_paid": 500, "interest_paid": 200, "remaining_balance": 23800 },
  { "repayment_id": "REPAY007", "loan_id": "LOAN004", "repayment_date": "2021-12-01", "amount_paid": 400, "principal_paid": 300, "interest_paid": 100, "remaining_balance": 14700 },
  { "repayment_id": "REPAY008", "loan_id": "LOAN004", "repayment_date": "2022-01-01", "amount_paid": 400, "principal_paid": 300, "interest_paid": 100, "remaining_balance": 14400 },
  { "repayment_id": "REPAY009", "loan_id": "LOAN005", "repayment_date": "2023-07-01", "amount_paid": 800, "principal_paid": 500, "interest_paid": 300, "remaining_balance": 199200 },
  { "repayment_id": "REPAY010", "loan_id": "LOAN005", "repayment_date": "2023-08-01", "amount_paid": 800, "principal_paid": 500, "interest_paid": 300, "remaining_balance": 198700 },
  { "repayment_id": "REPAY011", "loan_id": "LOAN006", "repayment_date": "2023-08-15", "amount_paid": 1000, "principal_paid": 750, "interest_paid": 250, "remaining_balance": 49250 },
  { "repayment_id": "REPAY012", "loan_id": "LOAN006", "repayment_date": "2023-09-15", "amount_paid": 1000, "principal_paid": 750, "interest_paid": 250, "remaining_balance": 48500 },
  { "repayment_id": "REPAY013", "loan_id": "LOAN007", "repayment_date": "2023-03-20", "amount_paid": 250, "principal_paid": 200, "interest_paid": 50, "remaining_balance": 11800 },
  { "repayment_id": "REPAY014", "loan_id": "LOAN007", "repayment_date": "2023-04-20", "amount_paid": 250, "principal_paid": 200, "interest_paid": 50, "remaining_balance": 11600 },
  { "repayment_id": "REPAY015", "loan_id": "LOAN008", "repayment_date": "2021-11-15", "amount_paid": 300, "principal_paid": 250, "interest_paid": 50, "remaining_balance": 29700 },
  { "repayment_id": "REPAY016", "loan_id": "LOAN008", "repayment_date": "2021-12-15", "amount_paid": 300, "principal_paid": 250, "interest_paid": 50, "remaining_balance": 29400 },
  { "repayment_id": "REPAY017", "loan_id": "LOAN009", "repayment_date": "2022-09-01", "amount_paid": 400, "principal_paid": 300, "interest_paid": 100, "remaining_balance": 74700 },
  { "repayment_id": "REPAY018", "loan_id": "LOAN009", "repayment_date": "2022-10-01", "amount_paid": 400, "principal_paid": 300, "interest_paid": 100, "remaining_balance": 74400 },
  { "repayment_id": "REPAY019", "loan_id": "LOAN010", "repayment_date": "2023-06-01", "amount_paid": 350, "principal_paid": 250, "interest_paid": 100, "remaining_balance": 17750 },
  { "repayment_id": "REPAY020", "loan_id": "LOAN010", "repayment_date": "2023-07-01", "amount_paid": 350, "principal_paid": 250, "interest_paid": 100, "remaining_balance": 17500 }
]);



db.collateral.insert_many([
  { "collateral_id": "COL001", "loan_id": "LOAN002", "collateral_type": "property", "description": "3-bedroom house in Townsville", "appraised_value": 180000, "date_of_valuation": "2022-04-01" },
  { "collateral_id": "COL002", "loan_id": "LOAN002", "collateral_type": "vehicle", "description": "Toyota Camry 2018", "appraised_value": 20000, "date_of_valuation": "2022-04-01" },
  { "collateral_id": "COL003", "loan_id": "LOAN003", "collateral_type": "vehicle", "description": "Honda Civic 2019", "appraised_value": 22000, "date_of_valuation": "2023-02-15" },
  { "collateral_id": "COL004", "loan_id": "LOAN004", "collateral_type": "property", "description": "Condo in Cityville", "appraised_value": 120000, "date_of_valuation": "2021-06-30" },
  { "collateral_id": "COL005", "loan_id": "LOAN005", "collateral_type": "property", "description": "5-acre farmland", "appraised_value": 250000, "date_of_valuation": "2023-01-10" },
  { "collateral_id": "COL006", "loan_id": "LOAN006", "collateral_type": "equipment", "description": "Industrial equipment set", "appraised_value": 50000, "date_of_valuation": "2023-03-22" },
  { "collateral_id": "COL007", "loan_id": "LOAN007", "collateral_type": "vehicle", "description": "Ford F-150 2020", "appraised_value": 30000, "date_of_valuation": "2022-08-15" },
  { "collateral_id": "COL008", "loan_id": "LOAN008", "collateral_type": "vehicle", "description": "Chevrolet Malibu 2018", "appraised_value": 18000, "date_of_valuation": "2021-09-01" },
  { "collateral_id": "COL009", "loan_id": "LOAN009", "collateral_type": "property", "description": "Warehouse in Industrial Area", "appraised_value": 95000, "date_of_valuation": "2022-11-05" },
  { "collateral_id": "COL010", "loan_id": "LOAN010", "collateral_type": "equipment", "description": "Restaurant kitchen setup", "appraised_value": 25000, "date_of_valuation": "2023-02-11" },
  { "collateral_id": "COL011", "loan_id": "LOAN011", "collateral_type": "property", "description": "4-bedroom villa", "appraised_value": 280000, "date_of_valuation": "2020-12-20" },
  { "collateral_id": "COL012", "loan_id": "LOAN012", "collateral_type": "vehicle", "description": "BMW 5 Series 2021", "appraised_value": 35000, "date_of_valuation": "2023-08-30" },
  { "collateral_id": "COL013", "loan_id": "LOAN013", "collateral_type": "property", "description": "Townhouse in Cityville", "appraised_value": 90000, "date_of_valuation": "2021-04-01" },
  { "collateral_id": "COL014", "loan_id": "LOAN014", "collateral_type": "equipment", "description": "Construction machinery", "appraised_value": 60000, "date_of_valuation": "2022-05-12" },
  { "collateral_id": "COL015", "loan_id": "LOAN015", "collateral_type": "property", "description": "Land plot, 2 acres", "appraised_value": 70000, "date_of_valuation": "2023-01-03" },
  { "collateral_id": "COL016", "loan_id": "LOAN016", "collateral_type": "vehicle", "description": "Tesla Model 3 2020", "appraised_value": 40000, "date_of_valuation": "2023-07-15" },
  { "collateral_id": "COL017", "loan_id": "LOAN017", "collateral_type": "equipment", "description": "Medical equipment set", "appraised_value": 55000, "date_of_valuation": "2022-09-01" },
  { "collateral_id": "COL018", "loan_id": "LOAN018", "collateral_type": "property", "description": "Office space downtown", "appraised_value": 135000, "date_of_valuation": "2021-12-01" },
  { "collateral_id": "COL019", "loan_id": "LOAN019", "collateral_type": "property", "description": "Beachfront house", "appraised_value": 220000, "date_of_valuation": "2020-09-15" },
  { "collateral_id": "COL020", "loan_id": "LOAN020", "collateral_type": "vehicle", "description": "Mercedes-Benz E-Class 2019", "appraised_value": 42000, "date_of_valuation": "2023-04-15" }
]);



db.employees.insert_many([
  { "employee_id": "EMP001", "first_name": "Alice", "last_name": "Johnson", "position": "loan officer", "branch_id": "BR001", "email": "alice.johnson@bank.com", "phone": "555-9988" },
  { "employee_id": "EMP002", "first_name": "Bob", "last_name": "Miller", "position": "branch manager", "branch_id": "BR002", "email": "bob.miller@bank.com", "phone": "555-1122" },
  { "employee_id": "EMP003", "first_name": "Clara", "last_name": "Smith", "position": "loan processor", "branch_id": "BR001", "email": "clara.smith@bank.com", "phone": "555-2233" },
  { "employee_id": "EMP004", "first_name": "David", "last_name": "Brown", "position": "loan officer", "branch_id": "BR003", "email": "david.brown@bank.com", "phone": "555-3344" },
  { "employee_id": "EMP005", "first_name": "Emma", "last_name": "Jones", "position": "loan specialist", "branch_id": "BR002", "email": "emma.jones@bank.com", "phone": "555-4455" },
  { "employee_id": "EMP006", "first_name": "Frank", "last_name": "Davis", "position": "loan officer", "branch_id": "BR001", "email": "frank.davis@bank.com", "phone": "555-5566" },
  { "employee_id": "EMP007", "first_name": "Grace", "last_name": "Garcia", "position": "branch assistant", "branch_id": "BR004", "email": "grace.garcia@bank.com", "phone": "555-6677" },
  { "employee_id": "EMP008", "first_name": "Henry", "last_name": "Martinez", "position": "loan processor", "branch_id": "BR005", "email": "henry.martinez@bank.com", "phone": "555-7788" },
  { "employee_id": "EMP009", "first_name": "Ivy", "last_name": "Clark", "position": "loan officer", "branch_id": "BR003", "email": "ivy.clark@bank.com", "phone": "555-8899" },
  { "employee_id": "EMP010", "first_name": "Jake", "last_name": "Rodriguez", "position": "loan specialist", "branch_id": "BR002", "email": "jake.rodriguez@bank.com", "phone": "555-9900" },
  { "employee_id": "EMP011", "first_name": "Kara", "last_name": "Lewis", "position": "branch manager", "branch_id": "BR003", "email": "kara.lewis@bank.com", "phone": "555-1010" },
  { "employee_id": "EMP012", "first_name": "Liam", "last_name": "Walker", "position": "loan officer", "branch_id": "BR001", "email": "liam.walker@bank.com", "phone": "555-1111" },
  { "employee_id": "EMP013", "first_name": "Mia", "last_name": "Harris", "position": "loan processor", "branch_id": "BR004", "email": "mia.harris@bank.com", "phone": "555-2222" },
  { "employee_id": "EMP014", "first_name": "Nina", "last_name": "Nelson", "position": "loan officer", "branch_id": "BR005", "email": "nina.nelson@bank.com", "phone": "555-3333" },
  { "employee_id": "EMP015", "first_name": "Oscar", "last_name": "Hall", "position": "branch assistant", "branch_id": "BR004", "email": "oscar.hall@bank.com", "phone": "555-4444" },
  { "employee_id": "EMP016", "first_name": "Paula", "last_name": "Young", "position": "loan specialist", "branch_id": "BR003", "email": "paula.young@bank.com", "phone": "555-5555" },
  { "employee_id": "EMP017", "first_name": "Quinn", "last_name": "Allen", "position": "loan officer", "branch_id": "BR001", "email": "quinn.allen@bank.com", "phone": "555-6666" },
  { "employee_id": "EMP018", "first_name": "Rita", "last_name": "King", "position": "branch manager", "branch_id": "BR002", "email": "rita.king@bank.com", "phone": "555-7777" },
  { "employee_id": "EMP019", "first_name": "Sam", "last_name": "Wright", "position": "loan processor", "branch_id": "BR003", "email": "sam.wright@bank.com", "phone": "555-8888" },
  { "employee_id": "EMP020", "first_name": "Tina", "last_name": "Lopez", "position": "loan officer", "branch_id": "BR004", "email": "tina.lopez@bank.com", "phone": "555-9999" }
]);

db.branches.insert_many([
  { "branch_id": "BR001", "branch_name": "Main Branch", "address": "789 Bank Rd, Cityville", "phone": "555-0101" },
  { "branch_id": "BR002", "branch_name": "West Branch", "address": "123 West St, Townsville", "phone": "555-0202" },
  { "branch_id": "BR003", "branch_name": "East Branch", "address": "456 East Blvd, Cityville", "phone": "555-0303" },
  { "branch_id": "BR004", "branch_name": "North Branch", "address": "789 North Ave, Cityville", "phone": "555-0404" },
  { "branch_id": "BR005", "branch_name": "South Branch", "address": "321 South St, Townsville", "phone": "555-0505" },
  { "branch_id": "BR006", "branch_name": "Central Branch", "address": "654 Central Ave, Cityville", "phone": "555-0606" },
  { "branch_id": "BR007", "branch_name": "Downtown Branch", "address": "987 Downtown Rd, Townsville", "phone": "555-0707" },
  { "branch_id": "BR008", "branch_name": "Uptown Branch", "address": "654 Uptown Rd, Cityville", "phone": "555-0808" },
  { "branch_id": "BR009", "branch_name": "Lakeside Branch", "address": "123 Lakeside Dr, Townsville", "phone": "555-0909" },
  { "branch_id": "BR010", "branch_name": "Mountain Branch", "address": "987 Mountain Rd, Cityville", "phone": "555-1001" },
  { "branch_id": "BR011", "branch_name": "Beachside Branch", "address": "321 Beachside Ave, Townsville", "phone": "555-1102" },
  { "branch_id": "BR012", "branch_name": "Parkside Branch", "address": "789 Park Ave, Cityville", "phone": "555-1203" },
  { "branch_id": "BR013", "branch_name": "Riverside Branch", "address": "456 Riverside Dr, Townsville", "phone": "555-1304" },
  { "branch_id": "BR014", "branch_name": "Harbor Branch", "address": "123 Harbor St, Cityville", "phone": "555-1405" },
  { "branch_id": "BR015", "branch_name": "Airport Branch", "address": "987 Airport Rd, Townsville", "phone": "555-1506" },
  { "branch_id": "BR016", "branch_name": "Market Branch", "address": "321 Market Ave, Cityville", "phone": "555-1607" },
  { "branch_id": "BR017", "branch_name": "Greenfield Branch", "address": "654 Greenfield Rd, Townsville", "phone": "555-1708" },
  { "branch_id": "BR018", "branch_name": "Hilltop Branch", "address": "456 Hilltop Dr, Cityville", "phone": "555-1809" },
  { "branch_id": "BR019", "branch_name": "Valley Branch", "address": "789 Valley Rd, Townsville", "phone": "555-1900" },
  { "branch_id": "BR020", "branch_name": "Sunset Branch", "address": "123 Sunset Blvd, Cityville", "phone": "555-2001" }
]);

db.loan_applications.insert_many([
 { "application_id": "APP001", "customer_id": "CUST001", "loan_type": "auto", "requested_amount": 20000, "application_date": "2023-01-10", "application_status": "pending", "assigned_employee": "EMP001" },
 { "application_id": "APP002", "customer_id": "CUST002", "loan_type": "personal", "requested_amount": 5000, "application_date": "2023-01-12", "application_status": "approved", "assigned_employee": "EMP002" },
 { "application_id": "APP003", "customer_id": "CUST003", "loan_type": "business", "requested_amount": 75000, "application_date": "2023-02-01", "application_status": "rejected", "assigned_employee": "EMP003" },
 { "application_id": "APP004", "customer_id": "CUST004", "loan_type": "mortgage", "requested_amount": 150000, "application_date": "2023-02-15", "application_status": "approved", "assigned_employee": "EMP004" },
 { "application_id": "APP005", "customer_id": "CUST005", "loan_type": "auto", "requested_amount": 18000, "application_date": "2023-03-05", "application_status": "pending", "assigned_employee": "EMP005" },
 { "application_id": "APP006", "customer_id": "CUST006", "loan_type": "personal", "requested_amount": 25000, "application_date": "2023-03-20", "application_status": "rejected", "assigned_employee": "EMP006" },
 { "application_id": "APP007", "customer_id": "CUST007", "loan_type": "business", "requested_amount": 50000, "application_date": "2023-04-10", "application_status": "approved", "assigned_employee": "EMP007" },
 { "application_id": "APP008", "customer_id": "CUST008", "loan_type": "mortgage", "requested_amount": 100000, "application_date": "2023-05-01", "application_status": "pending", "assigned_employee": "EMP008" },
 { "application_id": "APP009", "customer_id": "CUST009", "loan_type": "auto", "requested_amount": 22000, "application_date": "2023-05-15", "application_status": "approved", "assigned_employee": "EMP009" },
 { "application_id": "APP010", "customer_id": "CUST010", "loan_type": "personal", "requested_amount": 12000, "application_date": "2023-06-01", "application_status": "rejected", "assigned_employee": "EMP010" },
 { "application_id": "APP011", "customer_id": "CUST011", "loan_type": "business", "requested_amount": 80000, "application_date": "2023-06-15", "application_status": "approved", "assigned_employee": "EMP011" },
 { "application_id": "APP012", "customer_id": "CUST012", "loan_type": "mortgage", "requested_amount": 160000, "application_date": "2023-07-01", "application_status": "pending", "assigned_employee": "EMP012" },
 { "application_id": "APP013", "customer_id": "CUST013", "loan_type": "auto", "requested_amount": 20000, "application_date": "2023-07-20", "application_status": "approved", "assigned_employee": "EMP013" },
 { "application_id": "APP014", "customer_id": "CUST014", "loan_type": "personal", "requested_amount": 9000, "application_date": "2023-08-05", "application_status": "pending", "assigned_employee": "EMP014" },
 { "application_id": "APP015", "customer_id": "CUST015", "loan_type": "business", "requested_amount": 60000, "application_date": "2023-08-22", "application_status": "rejected", "assigned_employee": "EMP015" },
 { "application_id": "APP016", "customer_id": "CUST016", "loan_type": "mortgage", "requested_amount": 140000, "application_date": "2023-09-01", "application_status": "approved", "assigned_employee": "EMP016" },
 { "application_id": "APP017", "customer_id": "CUST017", "loan_type": "auto", "requested_amount": 25000, "application_date": "2023-09-15", "application_status": "pending", "assigned_employee": "EMP017" },
 { "application_id": "APP018", "customer_id": "CUST018", "loan_type": "personal", "requested_amount": 15000, "application_date": "2023-10-01", "application_status": "approved", "assigned_employee": "EMP018" },
 { "application_id": "APP019", "customer_id": "CUST019", "loan_type": "business", "requested_amount": 70000, "application_date": "2023-10-20", "application_status": "rejected", "assigned_employee": "EMP019" },
 { "application_id": "APP020", "customer_id": "CUST020", "loan_type": "mortgage", "requested_amount": 200000, "application_date": "2023-11-01", "application_status": "pending", "assigned_employee": "EMP020" }
]);


db.payments_schedule.insert_many([
 { "schedule_id": "SCHD001", "loan_id": "LOAN001", "due_date": "2023-02-15", "payment_due": 200, "status": "paid" },
 { "schedule_id": "SCHD002", "loan_id": "LOAN001", "due_date": "2023-03-15", "payment_due": 200, "status": "paid" },
 { "schedule_id": "SCHD003", "loan_id": "LOAN002", "due_date": "2023-06-01", "payment_due": 500, "status": "paid" },
 { "schedule_id": "SCHD004", "loan_id": "LOAN002", "due_date": "2023-07-01", "payment_due": 500, "status": "paid" },
 { "schedule_id": "SCHD005", "loan_id": "LOAN003", "due_date": "2023-05-10", "payment_due": 700, "status": "paid" },
 { "schedule_id": "SCHD006", "loan_id": "LOAN003", "due_date": "2023-06-10", "payment_due": 700, "status": "due" },
 { "schedule_id": "SCHD007", "loan_id": "LOAN004", "due_date": "2021-12-01", "payment_due": 400, "status": "paid" },
 { "schedule_id": "SCHD008", "loan_id": "LOAN004", "due_date": "2022-01-01", "payment_due": 400, "status": "paid" },
 { "schedule_id": "SCHD009", "loan_id": "LOAN005", "due_date": "2023-07-01", "payment_due": 800, "status": "paid" },
 { "schedule_id": "SCHD010", "loan_id": "LOAN005", "due_date": "2023-08-01", "payment_due": 800, "status": "due" },
 { "schedule_id": "SCHD011", "loan_id": "LOAN006", "due_date": "2023-08-15", "payment_due": 1000, "status": "paid" },
 { "schedule_id": "SCHD012", "loan_id": "LOAN006", "due_date": "2023-09-15", "payment_due": 1000, "status": "due" },
 { "schedule_id": "SCHD013", "loan_id": "LOAN007", "due_date": "2023-03-20", "payment_due": 250, "status": "paid" },
 { "schedule_id": "SCHD014", "loan_id": "LOAN007", "due_date": "2023-04-20", "payment_due": 250, "status": "paid" },
 { "schedule_id": "SCHD015", "loan_id": "LOAN008", "due_date": "2021-11-15", "payment_due": 300, "status": "paid" },
 { "schedule_id": "SCHD016", "loan_id": "LOAN008", "due_date": "2021-12-15", "payment_due": 300, "status": "paid" },
 { "schedule_id": "SCHD017", "loan_id": "LOAN009", "due_date": "2022-09-01", "payment_due": 400, "status": "overdue" },
 { "schedule_id": "SCHD018", "loan_id": "LOAN009", "due_date": "2022-10-01", "payment_due": 400, "status": "due" },
 { "schedule_id": "SCHD019", "loan_id": "LOAN010", "due_date": "2023-06-01", "payment_due": 350, "status": "paid" },
 { "schedule_id": "SCHD020", "loan_id": "LOAN010", "due_date": "2023-07-01", "payment_due": 350, "status": "due" }
]);


db.customers.create_index("customer_id", unique=True)
db.loans.create_index("loan_id", unique=True)
db.loans.create_index("customer_id")
db.repayments.create_index("loan_id")
db.collateral.create_index("loan_id")
db.loan_applications.create_index([("customer_id", 1), ("application_date", -1)])


print("Data inserted successfully!")
