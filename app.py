import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Training Dashboard", layout="wide")

# ---------- SIMPLE THEME ----------
st.markdown("""
<style>
.main {
    background-color: white;
}
.stButton>button {
    background-color: #0d6efd;
    color: white;
}
.navbar {
    background-color:#0d6efd;
    padding:10px;
    color:white;
}
.box {
    border:1px solid #d3d3d3;
    border-radius:10px;
    padding:40px;
    text-align:center;
    font-size:20px;
}
</style>
""", unsafe_allow_html=True)


# ---------- SESSION STATES ----------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# ---------- SIGNUP FUNCTION ----------
def signup():
    st.title("Signup")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):

        if password != confirm:
            st.error("Passwords do not match")

        elif username in st.session_state.users:
            st.error("User already exists")

        else:
            st.session_state.users[username] = password
            st.success("Account created successfully")
            st.session_state.page = "login"
            st.rerun()

    st.write("Already have an account?")
    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()


# ---------- LOGIN FUNCTION ----------
def login():

    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.page = "dashboard"
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.write("Don't have an account?")
    if st.button("Signup"):
        st.session_state.page = "signup"
        st.rerun()


# ---------- DASHBOARD ----------
def dashboard():

    # NAVBAR
    col1, col2, col3 = st.columns([6,2,1])

    with col1:
        st.markdown("### Training Dashboard")

    with col2:
        form_option = st.selectbox("Forms", [
            "Select",
            "Registration Form",
            "Training Completion Form"
        ])

        if form_option == "Registration Form":
            st.success("Registration Form Page")

        if form_option == "Training Completion Form":
            st.success("Training Completion Form Page")

    with col3:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()

    st.divider()

    # SIDEBAR
    st.sidebar.title("Menu")

    menu = st.sidebar.radio("Navigation", [
        "Home",
        "Apply TD",
        "Approve TD"
    ])

    # ---------- HOME ----------
    if menu == "Home":

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="box">
            Notices
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="box">
            Courses
            </div>
            """, unsafe_allow_html=True)

    # ---------- APPLY TD ----------
    elif menu == "Apply TD":
        st.title("Apply Training / Development")

        st.text_input("Employee Name")
        st.text_input("Course Name")
        st.text_area("Reason")

        if st.button("Submit Application"):
            st.success("Application Submitted")

    # ---------- APPROVE TD ----------
    elif menu == "Approve TD":

        st.title("Approve Training / Development")

        st.write("Pending Applications")

        if st.button("Approve"):
            st.success("Approved")

        if st.button("Reject"):
            st.error("Rejected")


# ---------- PAGE ROUTER ----------
if st.session_state.page == "login":
    login()

elif st.session_state.page == "signup":
    signup()

elif st.session_state.page == "dashboard" and st.session_state.logged_in:
    dashboard()