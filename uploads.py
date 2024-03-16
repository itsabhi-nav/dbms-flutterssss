import os

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Your existing code to handle form submission
        
        # Handle file upload and save the photo path to the MongoDB document
        photo_path = None
        if 'photo' in request.files:
            photo_file = request.files['photo']
            if photo_file.filename != '':
                if not os.path.exists('uploads'):
                    os.makedirs('uploads')  # Create the 'uploads' directory if it doesn't exist
                photo_path = os.path.join('uploads', photo_file.filename)
                photo_file.save(photo_path)
            new_user['Photo'] = photo_path

        # Your existing code to insert user data into MongoDB

    else:
        return render_template('add_user.html')
