from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="contact"  # Add database name
)
mycursor = mydb.cursor()

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM mycontacts")
    mycontacts = mycursor.fetchall()
    return render_template('index.html', mycontacts=mycontacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        sql = "INSERT INTO mycontacts (name, email, phone) VALUES (%s, %s, %s)"
        val = (name, email, phone)
        mycursor.execute(sql, val)
        mydb.commit()
        flash('contact added successfully', 'success')  # Flash success message
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        sql = "UPDATE mycontacts SET name=%s, email=%s, phone=%s WHERE id=%s"
        val = (name, email, phone, contact_id)
        mycursor.execute(sql, val)
        mydb.commit()
        flash('contact updated successfully', 'success')  # Flash success message
        return redirect(url_for('index'))
    mycursor.execute("SELECT * FROM mycontacts WHERE id = %s", (contact_id,))
    contact = mycursor.fetchone()
    return render_template('edit_contact.html', contact=contact)

@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    sql = "DELETE FROM mycontacts WHERE id = %s"
    mycursor.execute(sql, (contact_id,))
    mydb.commit()
    flash('contact deleted successfully', 'success')  # Flash success message
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
