def calculate_force(spec_impulse, mass_flow_rate):
    """
    Calculate the force based on specific impulse and mass flow rate.
    
    Args:
        spec_impulse (float): Specific impulse in seconds.
        mass_flow_rate (float): Mass flow rate in kilograms per second.
    
    Returns:
        float: The calculated force in Newtons.
    """
    return spec_impulse * mass_flow_rate