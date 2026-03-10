import streamlit as st
import json
import os

st.set_page_config(page_title="Training Dashboard", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

h1,h2{
text-align:center;
}

.form-heading{
text-align:left;
font-weight:bold;
font-size:20px;
margin-top:25px;
}

.box{
border:1px solid #d3d3d3;
border-radius:10px;
padding:40px;
text-align:center;
font-size:20px;
cursor:pointer;
background-color:white;
color:black;
font-weight:bold;
}

/* BLUE BUTTONS */
div.stButton > button {
background-color:#0d6efd;
color:white;
font-weight:bold;
border-radius:6px;
}

</style>
""", unsafe_allow_html=True)


# ---------- USER STORAGE ----------
USER_FILE="users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE,"r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE,"w") as f:
        json.dump(users,f)


# ---------- SESSION ----------
if "users" not in st.session_state:
    st.session_state.users=load_users()

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if "page" not in st.session_state:
    st.session_state.page="login"

if "form_select" not in st.session_state:
    st.session_state.form_select="None"


# ---------- SIGNUP ----------
def signup():

    col1,col2,col3=st.columns([1,2,1])

    with col2:

        st.title("Signup")

        username=st.text_input("Username *")
        password=st.text_input("Password *",type="password")
        confirm=st.text_input("Confirm Password *",type="password")

        if st.button("Create Account"):

            if username=="" or password=="" or confirm=="":
                st.error("All fields required")

            elif password!=confirm:
                st.error("Passwords do not match")

            elif username in st.session_state.users:
                st.error("User already exists")

            else:
                st.session_state.users[username]=password
                save_users(st.session_state.users)
                st.success("Account created successfully")
                st.session_state.page="login"
                st.rerun()

        st.write("Already have an account?")

        if st.button("Go to Login"):
            st.session_state.page="login"
            st.rerun()


# ---------- LOGIN ----------
def login():

    col1,col2,col3=st.columns([1,2,1])

    with col2:

        st.title("Login")

        username=st.text_input("Username")
        password=st.text_input("Password",type="password")

        if st.button("Login"):

            if username in st.session_state.users and st.session_state.users[username]==password:
                st.session_state.logged_in=True
                st.session_state.page="dashboard"
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.write("Don't have an account?")

        if st.button("Signup"):
            st.session_state.page="signup"
            st.rerun()


# ---------- REGISTRATION FORM ----------
def registration_form():

    st.title("Nominee Registration Form")

    st.markdown('<div class="form-heading">1. Personal Details</div>',unsafe_allow_html=True)
    name=st.text_input("Name *")
    designation=st.text_input("Designation *")
    pis=st.text_input("PIS Number *")
    joining=st.date_input("Date of Joining at Present Grade *")

    st.markdown('<div class="form-heading">2. Contact Details</div>',unsafe_allow_html=True)
    mobile=st.text_input("Mobile Number *")
    email=st.text_input("Email ID *")

    st.markdown('<div class="form-heading">3. Category</div>',unsafe_allow_html=True)
    category=st.radio("Category of the nominee*",["SC","ST","GEN","OBC"],index=None)

    st.markdown('<div class="form-heading">4. Date of Birth</div>',unsafe_allow_html=True)
    dob=st.date_input("Date of Birth of the nominee*")

    st.markdown('<div class="form-heading">5. Qualification</div>',unsafe_allow_html=True)
    qualification=st.text_input("Qualification of the nominee*")

    st.markdown('<div class="form-heading">6. Group and Activity</div>',unsafe_allow_html=True)
    group=st.text_area("Group / Activity on which nominee is engaged*")

    st.markdown('<div class="form-heading">7. Assignment Period</div>',unsafe_allow_html=True)
    assignment=st.text_input("Period in the present assignment*")

    st.markdown('<div class="form-heading">8. Suitable assignment</div>',unsafe_allow_html=True)
    suitable=st.radio("Is Qualification/Experience suitable to the assignment? *",["Yes","No"],index=None)

    st.markdown('<div class="form-heading">9. Course Details</div>',unsafe_allow_html=True)
    course=st.text_input("CEP/Trg./Course Title *")
    venue=st.text_input("Training/Seminar Venue *")

    st.markdown('<div class="form-heading">10. Course Duration</div>',unsafe_allow_html=True)
    duration=st.text_input("Duration with Date of the CEP/Trg./Course/Seminar *")

    st.markdown('<div class="form-heading">11. Expenditure</div>',unsafe_allow_html=True)
    basic=st.number_input("Basic Pay *",min_value=0)
    total=st.number_input("Total Pay *",min_value=0)
    salary=st.number_input("Salary for training period *",min_value=0)
    registration=st.number_input("Registration fee(if any) *",min_value=0)
    ta=st.number_input("TA/DA *",min_value=0)

    st.markdown('<div class="form-heading">12. Training Recommendation Criteria</div>',unsafe_allow_html=True)
    st.checkbox("Improvement in Job Skill")
    st.checkbox("Improvement in Qualification")
    st.checkbox("Special Training")
    st.checkbox("For New Assignment")
    st.checkbox("Refreshment Knowledge")
    st.checkbox("Presentation of Paper")

    st.markdown('<div class="form-heading">13. Previous Similar Training</div>',unsafe_allow_html=True)
    attended=st.radio("Has nominee attended similar program in the past? *",["Yes","No"],index=None)

    if attended=="Yes":
        details=st.text_area("Please provide details of the training attended")

    st.markdown('<div class="form-heading">14. Details of trg./Course/Seminar attended during last two years</div>',unsafe_allow_html=True)
    last_training=st.text_area("Details")

    st.markdown('<div class="form-heading">15. Training Completion Form</div>',unsafe_allow_html=True)
    completion=st.radio("Have you submitted the completion form for other trg./Course attended by you? *",["Yes","No"],index=None)

    if completion=="No":
        reason=st.text_area("Please provide the reason for not submitting")

    st.markdown('<div class="form-heading">16. Signature of Nominee with Date</div>',unsafe_allow_html=True)
    sig_date=st.date_input("Date")

    declaration=st.checkbox("I hereby declare that the information given above is true and correct.")

    if st.button("Submit Registration Form"):

        required=[name,designation,pis,mobile,email,qualification,group,assignment,course,venue,duration]

        if "" in required or category is None or suitable is None or attended is None or completion is None:
            st.error("Please fill all required fields")

        elif not declaration:
            st.error("Please accept the declaration")

        else:
            st.success("Form submitted successfully")


# ---------- APPROVE TD PAGE ----------
def approve_td_page():

    st.title("Approve Training / Development")

    nominees=["Rahul Sharma","Anita Verma","Rohit Singh"]

    col1,col2,col3=st.columns([4,2,2])

    col1.markdown("**Name of the Nominee**")
    col2.markdown("**Approve**")
    col3.markdown("**Reject**")

    for i,name in enumerate(nominees):

        c1,c2,c3=st.columns([4,2,2])

        c1.write(name)

        c2.button("Approve",key=f"approve_{i}")
        c3.button("Reject",key=f"reject_{i}")


# ---------- DASHBOARD ----------
def dashboard():

    col1,col2,col3=st.columns([6,2,1])

    with col1:
        st.markdown("### Training Dashboard")

    with col2:
        form_option=st.selectbox("Forms",["Select","Nominee Registration Form","Training Completion Form"],label_visibility="collapsed")

    with col3:
        if st.button("Logout"):
            st.session_state.logged_in=False
            st.session_state.page="login"
            st.rerun()

    st.divider()

    st.sidebar.title("Menu")

    menu=st.sidebar.radio("Navigation",["Home","Apply TD","Approve TD"])

    if menu=="Approve TD":
        approve_td_page()
        return

    if form_option=="Nominee Registration Form":
        registration_form()
        return

    if form_option=="Training Completion Form":
        st.title("Training Completion Form")
        st.info("Page under development")
        return

    if menu=="Home":

        col1,col2=st.columns(2)

        with col1:
            st.markdown('<div class="box">Notices</div>',unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="box">Courses</div>',unsafe_allow_html=True)


# ---------- ROUTER ----------
if st.session_state.page=="login":
    login()

elif st.session_state.page=="signup":
    signup()

elif st.session_state.page=="dashboard" and st.session_state.logged_in:
    dashboard()
