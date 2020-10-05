from openforcefield.tests.test_forcefield import create_ethanol
mol = create_ethanol()
from openforcefield.utils.toolkits import *
AmberToolsToolkitWrapper().assign_fractional_bond_orders(mol)
print(mol.get_bond_between(1, 2).fractional_bond_order)
