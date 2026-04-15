import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('cache')

# Load session----

session = fastf1.get_session(2023, 'Bahrain', 'Q')
session.load()

# Get fastest lap-----

lap = session.laps.pick_driver('VER').pick_fastest()

# Get telemetry
telemetry = lap.get_car_data().add_distance()

# Plot speed
plt.plot(telemetry['Distance'], telemetry['Speed'])
plt.title("Speed vs Distance (VER)")
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.show()