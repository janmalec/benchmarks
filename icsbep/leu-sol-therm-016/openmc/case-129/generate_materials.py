import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 7.2211e-07)
mat.add_nuclide('U235', 8.9609e-05)
mat.add_nuclide('U236', 8.9498e-08)
mat.add_nuclide('U238', 7.9816e-04)
mat.add_nuclide('H1', 5.8265e-02)
mat.add_nuclide('N14', 2.2589e-03)
mat.add_element('O', 3.7445e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Stainless steel"
mat.set_density('sum')
mat.add_element('C', 7.1567e-05)
mat.add_element('Si', 7.1415e-03)
mat.add_element('Mn', 9.9095e-03)
mat.add_element('P', 5.0879e-05)
mat.add_element('S', 1.0424e-06)
mat.add_element('Ni', 8.5600e-03)
mat.add_element('Cr', 1.6725e-02)
mat.add_element('Fe', 5.9560e-02)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 25 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6658e-02)
mat.add_element('O', 3.3329e-02)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Air"
mat.set_density('sum')
mat.add_nuclide('N14', 3.9016e-05)
mat.add_element('O', 1.0409e-05)
mats.append(mat)

mats.export_to_xml()
