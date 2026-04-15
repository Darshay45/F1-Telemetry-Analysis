import streamlit as st
import matplotlib.pyplot as plt
from src.utils import load_session, get_driver_telemetry

st.set_page_config(page_title="F1 Telemetry Tool", layout="wide")

st.title("🏎️ F1 Telemetry Analysis Dashboard")

#Sidebar controls
st.sidebar.header("Controls")

year = st.sidebar.selectbox("Year", [2023, 2022, 2021])
gp = st.sidebar.selectbox("Grand Prix", ["Bahrain", "Monaco", "Silverstone"])
session_type = st.sidebar.selectbox("Session", ["Q", "R"])

driver1 = st.sidebar.selectbox("Driver 1", ["VER", "HAM"], index=0)
driver2 = st.sidebar.selectbox("Driver 2", ["VER", "HAM"], index=1)

#Load Session
session = load_session(year, gp, session_type)

lap1, tel1 = get_driver_telemetry(session, driver1)
lap2, tel2 = get_driver_telemetry(session, driver2)

#Layout
col1, col2 = st.columns(2)

#Speed Comparsion
with col1:
    st.subheader("Speed Comparison")
    fig, ax = plt.subplots()
    ax.plot(tel1['Distance'], tel1['Speed'], label=driver1)
    ax.plot(tel2['Distance'], tel2['Speed'], label=driver2)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Speed (km/h)")
    ax.legend()
    st.pyplot(fig)

# Throttle & Brake
with col2:
    st.subheader(f"{driver1} Throttle & Brake")
    fig2, ax2 = plt.subplots()
    ax2.plot(tel1['Distance'], tel1['Throttle'], label="Throttle")
    ax2.plot(tel1['Distance'], tel1['Brake'], label="Brake")
    ax2.legend()
    st.pyplot(fig2)

#Track Map
st.subheader("Track Map (Speed Colored)")

pos = lap1.get_pos_data()
merged = tel1.merge(pos, left_index=True, right_index=True)

fig3, ax3 = plt.subplots()
sc = ax3.scatter(merged['X'], merged['Y'], c=merged['Speed'], cmap='viridis')
plt.colorbar(sc, ax=ax3, label="Speed (km/h)")
st.pyplot(fig3)

# Insights
st.subheader("Insights")

avg_speed1 = tel1['Speed'].mean()
avg_speed2 = tel2['Speed'].mean()

if avg_speed1 > avg_speed2:
    st.success(f"{driver1} is faster on average")
else:
    st.success(f"{driver2} is faster on average")

st.write(f"{driver1}: {avg_speed1:.2f} km/h")
st.write(f"{driver2}: {avg_speed2:.2f} km/h")
