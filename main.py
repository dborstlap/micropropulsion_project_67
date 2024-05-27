import pandas as pd

from functions import *


# Constants
I_total = 70 # Total impulse (Ns)
g0 = 9.80665  # Earth's gravitational acceleration in m/s^2

tank_margin = 1.10  # 10% safety margin
rho_T = 2810  # Density of aluminum (for tank) in kg/m^3
yield_strength = 503e6  # Yield Strength of aluminium 7075-T6
structural_margin = 2.0  # 100% safety margin
S = yield_strength/structural_margin  # Allowable stress in Pa
P = 50e5 # Tank pressure in Pa


# Function to calculate propellant mass
def calculate_propellant_mass(Isp, Itotal):
    return Itotal / (Isp * g0)

# Function to calculate propellant volume
def calculate_propellant_volume(mprop, rho_prop, tank_margin):
    return mprop / rho_prop * tank_margin

# Function to calculate tank mass
def calculate_tank_mass(Vprop, P, rho_T):
    R = ((3 * Vprop) / (4 * np.pi)) ** (1/3) # tank radius
    t = (P * R) / (2 * S) # wall thickness
    tank_mass = 4 * np.pi * R**2 * t * rho_T # mass of tank
    return tank_mass






# Path to your Excel file
file_path = 'data/thruster_data.xlsx'

# Reading the Excel file
df = pd.read_excel(file_path, sheet_name='All data')



# Add new columns for calculated values
df['Propellant Mass (kg)'] = df.apply(lambda row: calculate_propellant_mass(row['Isp (s)'], I_total), axis=1)
df['Propellant Volume (m^3)'] = df.apply(lambda row: calculate_propellant_volume(row['Propellant Mass (kg)'], 1000, tank_margin), axis=1)  # Assume rho_prop = 1000 kg/m^3 for simplification
df['Tank Mass (kg)'] = df.apply(lambda row: calculate_tank_mass(row['Propellant Volume (m^3)'], P, rho_T), axis=1)

# Assuming mthruster is given by 'Dry mass (g)' in kg
df['Thruster Mass (kg)'] = df['Dry mass (g)'] / 1000
df['Piping Mass (kg)'] = 0.3 # kg

# Calculate total dry mass
df['Dry Mass (kg)'] = df['Tank Mass (kg)'] + df['Thruster Mass (kg)'] + df['Piping Mass (kg)']

# Calculate total wet mass
df['Wet Mass (kg)'] = df['Propellant Mass (kg)'] + df['Dry Mass (kg)']

# Save to a new Excel file
output_file_path = 'data/modified_thrusters_data.xlsx'
df.to_excel(output_file_path, index=False, engine='openpyxl')

print(f"Data saved to {output_file_path}")