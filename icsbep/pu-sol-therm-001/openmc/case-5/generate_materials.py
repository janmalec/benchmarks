import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu238', 2.1250e-08)
mat.add_nuclide('Pu239', 3.3509e-04)
mat.add_nuclide('Pu240', 1.6395e-05)
mat.add_nuclide('Pu241', 1.0667e-06)
mat.add_nuclide('Pu242', 3.1347e-08)
mat.add_nuclide('N14', 2.7350e-03)
mat.add_nuclide('H1', 6.0371e-02)
mat.add_nuclide('O16', 3.7728e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.7428e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 25 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6655e-02)
mat.add_nuclide('O16', 3.3327e-02)
mats.append(mat)

mats.export_to_xml()
