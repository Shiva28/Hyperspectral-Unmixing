import os
import math
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import NMF_tools as nmft

ip_endmember_names = ["Alfalfa", "Corn-notill", "Corn-mintill", "Corn", "Grass-pasture", "Grass-trees", "Grass-pasture-mowed", "Hay-windrowed", "Oats", "Soybean-notill", "Soybean-mintill", "Soybean-clean", "Wheat", "Woods", "Buildings-Grass-Trees-Drives", "Stone-Steel-Tower"]

slsA_endmember_names = ["Brocoli_green_weeds_1", "Corn_senesced_green_weeds", "Lettuce_romaine_4wk", "Lettuce_romaine_5wk", "Lettuce_romaine_6wk", "Lettuce_romaine_7wk"]

paviaU_endmember_names = ["Asphalt", "Meadows", "Gravel", "Trees", "Painted metal sheets", "Bare Soil", "Bitumen", "Self-Blocking Bricks", "Shadows"]

# name = 'salinasA_corrected'
# endmember_names = slsA_endmember_names

name = 'indian_pines_corrected'
endmember_names = ip_endmember_names

# name = 'paviaU'
# endmember_names = paviaU_endmember_names


# Plot graphs
nmft.plot_NMF_data(name, endmember_names)