import datetime
import os
from pymongo import MongoClient
from email_utils import sendEmail
from flask import request

def insert_data():
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://dubeyabhinav1001:dubey@cluster0.rjzqrrm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['dbms']  
    collection = db['bday']  

    # Data to insert
    data = [
        {
            "Name": "Alice",
            "Birthday": datetime.datetime(1985, 2, 7),
            "Year": "1985",
            "Email": "alice@example.com",
            "Dialogue": "Happy Birthday Alice!",
            "Subject": "Happy Birthday!"
        },
        {
            "Name": "Bob",
            "Birthday": datetime.datetime(1992, 3, 7),
            "Year": "1992",
            "Email": "chtgpt979@gmail.com",
            "Dialogue": "Happy Birthday Bob!",
            "Subject": "Happy Birthday!"
        },
        {
            "Name": "Abhi",
            "Birthday": "1990-03-07",  # Example birthday as string
            "Year": "1990",
            "Email": "abhinavkumard.ec21@rvce.edu.in",
            "Dialogue": "Happy Birthday Abhi!",
            "Subject": "Happy Birthday!"
        }
        # Add more documents as needed
    ]

    for doc in data:
        # Check if data already exists
        existing_data = collection.find_one({"Name": doc["Name"], "Email": doc["Email"]})
        if existing_data:
            print(f"Data for {doc['Name']} with email {doc['Email']} already exists in the database. Skipping insertion.")
        else:
            collection.insert_one(doc)
            print(f"Inserted data for {doc['Name']} with email {doc['Email']}.")

        # Check if today is someone's birthday
        today = datetime.datetime.now().strftime("%d-%m")
        if isinstance(doc['Birthday'], str):
            doc['Birthday'] = datetime.datetime.strptime(doc['Birthday'], "%Y-%m-%d")
        bday = doc['Birthday'].strftime("%d-%m")
        if today == bday:
            # Retrieve GMAIL_ID and GMAIL_PSWD from environment variables
            GMAIL_ID = os.getenv('GMAIL_ID')  
            GMAIL_PSWD = os.getenv('GMAIL_PSWD')  

            # Handle file upload
            photo_path = None
            if 'photo' in request.files:
                photo_file = request.files['photo']
                if photo_file.filename != '':
                    photo_path = os.path.join('uploads', photo_file.filename)
                    photo_file.save(photo_path)

            # Send email with attached image
            sendEmail(doc['Email'], doc['Subject'], doc['Dialogue'], GMAIL_ID, GMAIL_PSWD, attachment=photo_path)
            print(f"Wished Happy Birthday to {doc['Name']}.")

    client.close()  

if __name__ == "__main__":
    insert_data()
