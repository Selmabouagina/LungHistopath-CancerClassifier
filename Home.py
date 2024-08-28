import streamlit as st
from PIL import Image
import sqlite3
from datetime import datetime
import hashlib

# Set up the layout with columns
col1, col2 = st.columns([2, 1])  # Adjust the ratio as needed
# Add the logo image above the sidebar menu
st.sidebar.image("logo.png", use_column_width=True)

# If you want to add a name alongside or under the logo, you can do so as well
st.sidebar.markdown("""
    <div style="text-align: center; padding-top: 5px;">
        <h2 style="color: #BA1132; margin-top: 0;">Medical Web App</h2>
    </div>
""", unsafe_allow_html=True)
# Custom CSS to change the background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #5E62B4; 
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #B82743; 
    }
    .testimonial-container {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 10px 0;
        margin: 20px 0;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
    }
    .testimonial-box {
        min-width: 300px;
        background-color: #f0f0f0;
        height: 200px;
        border-radius: 10px;
        text-align: center;
        padding: 20px;
        scroll-snap-align: center;
        flex-shrink: 0;
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
    }
    .testimonial-box:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    .testimonial-box h4 {
        margin-top: 10px;
        font-size: 18px;
        color: #333;
    }
    .testimonial-box p {
        font-size: 14px;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Function to register a new user
def register_user(name, email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users WHERE email = ?', (email,))
    count = c.fetchone()[0]
    if count > 0:
        st.write("An account with this email already exists.")
    else:
        c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_password))
        conn.commit()
        conn.close()
        st.write("Registration successful! You can now log in.")

# Function to handle the registration page
def register():
    st.title("Register for an Account")

    # Registration form
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if name and email and password:
            register_user(name, email, password)
        else:
            st.write("Please fill in all fields.")

# Sidebar Menu
st.sidebar.title("Menu")
menu_options = ["Home", "Book an Appointment", "Upload Image", "Learn About the Model", "About Us"]
selected_option = st.sidebar.selectbox("Choose a section:", menu_options)

if selected_option == "Home":
    
    with col1:
        st.title("Your Health is Our Focus !")
        st.write("**The lungs are not just vital organs, but a symbol of hope and resilience.**")
        register()

    with col2:
        lung_image = Image.open(r"C:/Users/MSI/Desktop/Projects/LungHistopath-CancerClassifier/LungHistopath-CancerClassifier/medical-report.png")
        st.image(lung_image, use_column_width=True)

    # Subheader with booking options
    st.markdown("""
        <h2 style='text-align: center;'>Book an Appointment</h2>
        <p style='text-align: center;'>Choose from the following options to schedule your appointment:</p>
        <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; width: 200px; text-align: center;">
                <div style="background-color: #5E62B4; color: white; padding: 5px 10px; border-radius: 50%; display: inline-block; font-size: 18px; margin-bottom: 10px;">🔍</div>
                <h4>Search Your Doctor</h4>
                <p>Find the right specialist for your needs.</p>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; width: 200px; text-align: center;">
                <div style="background-color: #5E62B4; color: white; padding: 5px 10px; border-radius: 50%; display: inline-block; font-size: 18px; margin-bottom: 10px;">🗓️</div>
                <h4>Schedule an Appointment</h4>
                <p>Choose a date and time that works best for you.</p>
            </div>
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; width: 200px; text-align: center;">
                <div style="background-color: #B82743; color: white; padding: 5px 10px; border-radius: 50%; display: inline-block; font-size: 18px; margin-bottom: 10px;">📞</div>
                <h4>Call for Support</h4>
                <p>Get assistance from our support team.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <footer style="
            background-color: #FFFFFF;
            color: white;
            padding: 20px;
            width: 100%;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
        ">
            <div style="display: inline-block;">
                <a href="#contact" style="color: black; text-decoration: none; font-weight: bold; margin-right: 20px;">Contact</a>
                <a href="#about" style="color: black; text-decoration: none; font-weight: bold; margin-right: 20px;">About</a>
                <a href="#privacy" style="color: black; text-decoration: none; font-weight: bold;">Privacy Policy</a>
            </div>
            <p style="color: black; margin-top: 10px;">© 2024 Medical Web App. All rights reserved.</p>
        </footer>
    """, unsafe_allow_html=True)




elif selected_option == "Upload Image":
    st.title("Upload a Histopathological Image")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        # Add prediction code here



elif selected_option == "Learn About the Model":
    st.title("Learn About the Model")
    st.write("This section explains how the deep learning model works.")
    st.write("Add details about CNNs, training data, etc.")
    st.image(r"C:\Users\MSI\Desktop\Projects\LungHistopath-CancerClassifier\LungHistopath-CancerClassifier\model_architecture.png", width=400)

elif selected_option == "Book an Appointment":
    # Input fields for appointment details
        name = st.text_input("Name")
        email = st.text_input("Email")
        appointment_date = st.date_input("Preferred Date")
        appointment_time = st.time_input("Preferred Time")

        appointment_datetime = datetime.combine(appointment_date, appointment_time)
        # "Book an Appointment" button
        book_button = st.button("Book an Appointment", key="appointment_button")
        
        if book_button:
            if name and email and appointment_datetime:
                # Connect to SQLite database
                conn = sqlite3.connect('appointments.db')
                c = conn.cursor()
                
                # Check if the chosen datetime is already booked
                c.execute('''
                    SELECT COUNT(*) FROM appointments WHERE date = ?
                ''', (appointment_datetime.strftime('%Y-%m-%d %H:%M:%S'),))
                count = c.fetchone()[0]

                if count > 0:
                    st.write("This time slot is already booked. Please choose a different time.")
                else:
                    # Insert appointment details into the database
                    c.execute('''
                        INSERT INTO appointments (name, email, date)
                        VALUES (?, ?, ?)
                    ''', (name, email, appointment_datetime.strftime('%Y-%m-%d %H:%M:%S')))
                    st.write("Appointment booked successfully!")

                # Commit and close the connection
                conn.commit()
                conn.close()
                
            else:
                st.write("Please fill in all fields.")
        

elif selected_option == "About Us":
    # "About Us" Section
    with col1:
        st.title("About Us")
        st.write("""
        At LungHistopath Cancer Classifier, our mission is to provide state-of-the-art AI solutions for the early detection and diagnosis of lung cancer. Our team is composed of dedicated professionals, including top oncologists and AI researchers, who work tirelessly to improve patient outcomes.
        """)
    with col2:
        st.write("""""")

    # "Our Doctors" Section with boxes
    st.markdown("<h2 style='text-align: center;'>Our Doctors</h2>", unsafe_allow_html=True)

    doctors = [
        {"name": "Dr. Alice Brown", "specialty": "Oncology", "bio": "Over 20 years of experience specializing in lung cancer treatment and research.", "contact": "alice.brown@example.com", "image": "alice_brown_image.png"},
        {"name": "Dr. Robert Green", "specialty": "Radiology", "bio": "An expert in medical imaging, advancing the field of radiology through AI solutions.", "contact": "robert.green@example.com", "image": "robert_green_image.png"},
        {"name": "Dr. Susan White", "specialty": "Pathology", "bio": "Focused on histopathology, contributing to numerous studies in early lung cancer detection.", "contact": "susan.white@example.com", "image": "susan_white_image.png"}
    ]

    # Layout the doctors in three columns
    cols = st.columns(len(doctors))

    for i, doctor in enumerate(doctors):
        with cols[i]:
            st.image(doctor['image'], use_column_width=True)  # Display the doctor's image
            st.markdown(
                f"""
                <div style='border: 1px solid #ddd; padding: 10px; border-radius: 5px;'>
                    <h4>{doctor['name']}</h4>
                    <p><strong>Specialty:</strong> {doctor['specialty']}</p>
                    <p>{doctor['bio']}</p>
                    <p><strong>Contact:</strong> {doctor['contact']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
    
    # Interactive "Client Testimonials" Section
    st.markdown("<h2 style='text-align: center;'>Client Testimonials</h2>", unsafe_allow_html=True)

    # Embed the iframe using st.markdown
    st.markdown("""
        <iframe src="https://widgets.commoninja.com/iframe/0b3b4a06-a031-4f5f-add1-7d0478f12df7" 
        width="100%" height="500px" frameborder="0" scrolling="no"></iframe>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    # Subheader: Specialist Doctor Home Visit
    with col1:
        st.image("doctor_image.png", use_column_width=True)

    # Column 2: Subheader, text, and centered button
    with col2:
        st.markdown("""
            <h3 style='text-align: center;'>We can ensure a specialist doctor to visit you at home</h3>
            <p style='text-align: center;'>Book an appointment today to get expert medical care at your convenience.</p>
        """, unsafe_allow_html=True)
        


        
        