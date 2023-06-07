# Побудуйте візуалізацію тензорного поля
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
import glyph_visualization_lib as gvl

def main():
    x = np.linspace(1, 3, 8)
    y = np.linspace(1, 3, 8)
    z = np.linspace(1, 3, 8)
    X, Y, Z = np.meshgrid(x, y, z)

    stress_tensor = np.array([
        [np.log(X)/np.sin(X),   np.sqrt(X)/Y,           np.sqrt(Y)/Z],
        [np.sqrt(X)/Y,          np.log(Y)/np.sin(Y),    np.sqrt(Z)/X],
        [np.sqrt(Y)/Z,          np.sqrt(Z)/X,           np.log(Z)/np.sin(Z)]
    ])

    vm_stress = gvl.get_von_Mises_stress(stress_tensor)
    glyph_radius = 0.1
    limits = [np.min(vm_stress), np.max(vm_stress)]
    colormap = plt.get_cmap('rainbow', 120)
    fig = mlab.figure(bgcolor=(1, 1, 1))
    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')

    for i in range(x.size):
        for j in range(y.size):
            for k in range(z.size):
                center = [x[i], y[j], z[k]]
                data = stress_tensor[:, :, i, j, k]
                color = colormap(gvl.get_colormap_ratio_on_stress(vm_stress[i, j, k], limits))[:3]

                """
                glyph_type = {0: 'cuboid', 1: 'cylinder', 2: 'ellipsoid', 3: 'superquadric'}
                if glyph_type == 3 (superquadric) 
                there are glyph shape type
                0 - superquadrics, 
                1 - Kindlmann_glyph, 
                2 - Kindlmann_modified_glyph
                """

                x_g, y_g, z_g = gvl.get_glyph_data(center, data, limits, glyph_points=12, glyph_radius=glyph_radius,
                                                   glyph_type=3,
                                                   superquadrics_option=1)
                mlab.mesh(x_g, y_g, z_g, color=color)
    mlab.move(forward=1.8)
    mlab.savefig("superquadric-Kindlmann_modified-viz.png", size=(100, 100))
    mlab.show()

    pass


if __name__ == '__main__':
    main()