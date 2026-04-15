import fastf1

fastf1.Cache.enable_cache('cache')

def load_session(year, gp, session_type):
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    return session

def get_driver_telemetry(session, driver):
    lap = session.laps.pick_driver(driver).pick_fastest()
    telemetry = lap.get_car_data().add_distance()
    return lap, telemetry