import numpy as np
from scipy.stats import lognorm
import networkx as nx
import geopandas as gpd
import matplotlib.pylab as plt
import wntr

# Create a WaterNetworkModel from an EPANET INP file
wn = wntr.network.WaterNetworkModel('networks/Net3.inp')

# # Print a basic description of the model.  The level can be 0, 1, or 2 and defines the level of detail included in the description.
wn.describe(level=1)

# # List properties and methods associated with the WaterNetworkModel (omitting private underscore names)
[name for name in dir(wn) if not name.startswith('_')]

# # Plot a basic network graphic
ax = wntr.graphics.plot_network(wn)

# # Print the names of all junctions, tanks, and reservoirs
print("Node names", wn.node_name_list)

# # Print the names of just tanks
print("Tank names", wn.tank_name_list)

# # Get a tank object
tank = wn.get_node('1')
print(type(tank))
tank

# # List properties and methods associated with the tank (omitting private underscore names)
# [name for name in dir(tank) if not name.startswith('_')]

# # Change the max level of a tank
# print("Original max level", tank.max_level)
# tank.max_level = 10
# print("New max level", tank.max_level)

# # Add a junction to the WaterNetworkModel
# wn.add_junction('new_junction', base_demand=0.0, demand_pattern=None, elevation=0.0, coordinates=None, demand_category=None)
# print(wn.junction_name_list)

# # Remove a junction from the WaterNetworkModel
# wn.remove_node('new_junction')
# print(wn.junction_name_list)

# # Print the names of all pipes, pumps, and valves
# print("Link names", wn.link_name_list)

# # Print the names of just head pumps
# print("Head pump names", wn.head_pump_name_list)

# # Get the name of links connected to a specific node
# connected_links = wn.get_links_for_node('229')
# print('Links connected to node 229 =', connected_links)

# # Get a pipe object
# pipe = wn.get_link('105')
# print(type(pipe))
# pipe

# # List properties and methods associated with the pipe (omitting private underscore names)
# [name for name in dir(pipe) if not name.startswith('_')]

# # Change the diameter of a pipe
# print("Original diameter", pipe.diameter)
# pipe.diameter = 10
# print("New diameter", pipe.diameter)

# # Add a pipe to the WaterNetworkModel
# wn.add_pipe(name="new_pipe", start_node_name="10", end_node_name="123", length=304.8, diameter=0.3048, roughness=100, minor_loss=0.0, initial_status='OPEN', check_valve=False)
# print(wn.pipe_name_list)

# # Remove a pipe from the WaterNetworkModel
# wn.remove_link("new_pipe")
# print(wn.pipe_name_list)

# # Compute expected demand
# expected_demand = wntr.metrics.expected_demand(wn)
# expected_demand.head()

# # Compute and plot average expected demand 
# AED = wntr.metrics.average_expected_demand(wn)
# print(AED.head())
# ax = wntr.graphics.plot_network(wn, node_attribute=AED, node_range=(0,0.025), title='Average expected demand (m$^3$/s)')

# # Identify junctions with zero demand
# zero_demand = AED[AED == 0].index
# print(zero_demand)
# ax = wntr.graphics.plot_network(wn, node_attribute=list(zero_demand), title='Zero demand junctions')

# # Get the demands on Junction 15
# junction = wn.get_node('15')
# junction.demand_timeseries_list

# # Get the pattern associated with the demand
# pattern = wn.get_pattern(junction.demand_timeseries_list[0].pattern_name)
# pattern

# # Modify the base value of the demand
# junction.demand_timeseries_list[0].base_value = 0.005

# # Add a new pattern to the model
# wn.add_pattern('New', [1,1,1,0,0,0,1,0,0.5,0.5,0.5,1])

# # Use the new pattern to modify the junction demand
# junction.demand_timeseries_list[0].pattern_name = "New"
# print(junction.demand_timeseries_list)

# # Add a demand to Junction 15
# junction.add_demand(base=0.015, pattern_name='1')
# print(junction.demand_timeseries_list)

# # Plot original and modified expected demands
# new_expected_demand = wntr.metrics.expected_demand(wn) 

# plt.figure()
# ax = expected_demand.loc[0:48*3600, "15"].plot()
# new_expected_demand.loc[0:48*3600, "15"].plot(ax=ax)
# tmp = ax.set_xlabel('Time (s)')
# tmp = ax.set_ylabel('Expected demand (m$^3$/s)')

# # Get a head pump object and plot the head pump curve
# pump = wn.get_link('10')
# print(type(pump))
# ax = wntr.graphics.plot_pump_curve(pump)

# # Get the head curve and print the points
# pump_curve_name = pump.pump_curve_name
# curve = wn.get_curve(pump_curve_name)
# curve.points

# # Modify the curve points and re-plot the pump curve
# curve.points = [(0.10, 20)]
# ax = wntr.graphics.plot_pump_curve(pump)

# # Add a tank volume curve to the model and assign it to a tank
# wn.add_curve('new_tank_curve', 'VOLUME', [
#    (1,  0),
#    (2,  60),
#    (3,  188),
#    (4,  372),
#    (5,  596),
#    (6,  848),
#    (7,  1114),
#    (8,  1379),
#    (9,  1631),
#    (10, 1856),
#    (11, 2039),
#    (12, 2168),
#    (13, 2228)])
# tank = wn.get_node('2')
# tank.vol_curve_name = 'new_tank_curve'
# ax = wntr.graphics.plot_tank_volume_curve(tank)

