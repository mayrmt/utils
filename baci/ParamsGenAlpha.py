#! /usr/bin/env python

# A script to calculate the time integration parameters for generalized alpha time integration 
# for both, structure and fluid.
# 
# Generalized-alpha time integration for structural dynamics follows "Chung, J. & Hulbert, G. A Time Integration Algorithm for Structural Dynamics With Improved Numerical Dissipation: The Generalized-alpha Method Journal of Applied Mechanics, 1993, 60, 371-375"
# 
# Generalized-alpha time integration for fluid dynamics follows "Jansen, K.E.; Whiting, C.H. & Hulbert, G.M. A generalized-alpha method for integrating the filtered Navier--Stokes equations with a stabilized finite element method Computer Methods in Applied Mechanics and Engineering, 2000, 190, 305-319"
# 
# Call: ParamsGenAlpha.py rho_structure rho_fluid
# 
# Input parameters:
# 	rho_structure	spectral radius for structural time integration
# 	rho_fluid	spectral radius for fluid time integration
#
# Author: Matthias Mayr (02/2012)
#

# import input arguments
import sys
rho_struct = float(sys.argv[1])
rho_fluid = float(sys.argv[2])

# compute time integration parameters for structural gen-alpha
alpha_F_struct = rho_struct / (rho_struct + 1.0)
alpha_M_struct = (2.0*rho_struct - 1.0)/(rho_struct + 1.0)
gamma_struct = 0.5 - alpha_M_struct + alpha_F_struct
beta_struct = 0.25 * pow(1 - alpha_M_struct + alpha_F_struct,2)

# compute time integration parameters for fluid gen-alpha
alpha_F_fluid = 1.0 / (1.0 + rho_fluid)
alpha_M_fluid = 0.5 * (3.0 - rho_fluid)/(1.0 + rho_fluid)
gamma_fluid = 0.5 + alpha_M_fluid - alpha_F_fluid

# print time integration parameters to console
print("\nStructure:")
print("ALPHA_F\t\t\t\t" + str(alpha_F_struct))
print("ALPHA_M\t\t\t\t" + str(alpha_M_struct))
print("BETA\t\t\t\t" + str(beta_struct))
print("GAMMA\t\t\t\t" + str(gamma_struct))
print("\n")
print("Fluid:")
print("ALPHA_M\t\t\t\t" + str(alpha_M_fluid))
print("ALPHA_F\t\t\t\t" + str(alpha_F_fluid))
print("GAMMA\t\t\t\t" + str(gamma_fluid))
print("\n")



