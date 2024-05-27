import CoolProp.CoolProp as CP


# propellant_matrix = [
#     ["Propellant", "State", "Density (kg/m^3)"],
#     ["Liq. Butane", "liquid", 590],
#     ["SF6", "gas", 103],
#     ["Argon", "gas", 56.6],
#     ["R134a", "liquid", 1207],
#     ["Isobutane", "liquid", 551],
#     ["R236fa", "liquid", 1389],
#     ["SO2", "gas", 120],
#     ["Nitrogen", "gas", 45.5],
#     ["Xenon", "gas", 294],
# ]


def get_propellant_density(fluid_name, pressure_Pa, temperature_K):
    """
    Calculate the density of a propellant given its name, tank pressure, and temperature.

    Parameters:
    fluid_name (str): The name of the propellant.
    tank_pressure (float): The pressure in the tank in bar.
    temperature_K (float): The temperature in Kelvin.

    Returns:
    float or str: The density of the propellant in kg/m^3, or an error message if the calculation fails.
    """

    # Calculate the density
    density = CP.PropsSI('D', 'P', pressure_Pa, 'T', temperature_K, fluid_name)

    # Determine the phase
    phase = CP.PropsSI('Phase', 'P', pressure_Pa, 'T', temperature_K, fluid_name)
    
    # Convert phase number to human-readable state
    state_list = ["unknown", "liquid", "gas", "supercritical liquid", "supercritical gas", "supercritical fluid"]
    state = state_list[int(phase)] if 0 <= phase <= 5 else "unknown"

    return density, state



# Example usage
fluids = ['R134a', 'Nitrogen', 'Argon', 'SF6', 'Butane', 'R236fa', 'SO2', 'Isobutane', 'Xenon']
tank_pressure = 50 * 1e5 #Pa
temperature_K = 300 #K

for fluid in fluids:
    density, state = get_propellant_density(fluid, tank_pressure, temperature_K)

    print(f"The density of {fluid} at {tank_pressure/1e5} bar and {temperature_K} K is {density:.2f} kg/m^3")
    print(state)
