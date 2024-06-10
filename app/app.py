import streamlit as st
import requests
import pandas as pd

# Function to get the current number of people in space and their names
def get_people_in_space():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    number_of_people = data['number']
    people = [person['name'] for person in data['people']]
    return number_of_people, people

# Function to get the current location of the International Space Station (ISS)
def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])
    return latitude, longitude

# Main function
def main():
    st.title("International Space Station Tracker")
    st.markdown("""
    This web app displays real-time information about the International Space Station (ISS).
    You can see the total number of people currently in space and their names. Additionally, you can visualize the current location of the ISS on a map.
    """)

    # Get the current number of people in space and their names
    number_of_people, people = get_people_in_space()

    st.write("### People in Space")
    st.write(f"Total number of people in space: {number_of_people}")
    st.write("Names of people in space:")
    for person in people:
        st.write(f"- {person}")

    # Get the current location of the ISS
    latitude, longitude = get_iss_location()

    st.write("### ISS Current Location")
    st.write("Latitude:", latitude)
    st.write("Longitude:", longitude)

    # Display the ISS location on a map
    st.write("### Map Showing ISS Location")
    df = pd.DataFrame({'LAT': [latitude], 'LON': [longitude]})
    st.map(df)
    st.write("""
    The map above shows the current location of the International Space Station (ISS) in real-time.
    """)

if __name__ == "__main__":
    main()