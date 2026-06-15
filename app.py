import streamlit as st

st.set_page_config(page_title="Grade Calculator", page_icon="🎓")

st.title("🎓 Student Grade Calculator")
st.markdown("---")

# Student Information
st.header("Student Information")

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
branch = st.text_input("Department")

st.header("Subject Marks")

sub1 = st.number_input("Python", 0, 100)
sub2 = st.number_input("Java", 0, 100)
sub3 = st.number_input("Database", 0, 100)
sub4 = st.number_input("Computer Network", 0, 100)
sub5 = st.number_input("Web Technology", 0, 100)

if st.button("Calculate Result"):

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    st.success("Result Generated Successfully!")

    st.subheader("Student Report Card")

    st.write("**Name:**", name)
    st.write("**Roll Number:**", roll)
    st.write("**Department:**", branch)

    st.write("### Marks")
    st.write("Python:", sub1)
    st.write("Java:", sub2)
    st.write("Database:", sub3)
    st.write("Computer Network:", sub4)
    st.write("Web Technology:", sub5)

    st.write("### Result")
    st.write("Total Marks:", total, "/500")
    st.write("Percentage:", round(percentage, 2), "%")
    st.write("Grade:", grade)

    if percentage >= 40:
        st.balloons()
        st.success("PASS ✅")
    else:
        st.error("FAIL ❌")