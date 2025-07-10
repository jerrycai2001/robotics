
# %%
import numpy as np

import matplotlib.pyplot as plt

# %%
def conch_spiral_fractal(a=0.2, b=0.20, turns=6, points=2000, depth=4):
    theta = np.linspace(0, 2 * np.pi * turns, points)
    r = a * np.exp(b * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    def draw_spiral(x, y, depth, scale=0.5, angle=np.pi/4):
        if depth == 0:
            return
        plt.plot(x, y, color=plt.cm.viridis(depth / 6))
        # Recursive smaller spirals along the main spiral
        for i in np.linspace(0.2, 0.8, 3):
            idx = int(i * len(x))
            x0, y0 = x[idx], y[idx]
            # Rotate and scale
            x1 = scale * (x - x[idx])
            y1 = scale * (y - y[idx])
            x1r = x1 * np.cos(angle) - y1 * np.sin(angle)
            y1r = x1 * np.sin(angle) + y1 * np.cos(angle)
            draw_spiral(x1r + x0, y1r + y0, depth - 1, scale * 0.7, angle)

    plt.figure(figsize=(8, 8))
    draw_spiral(x, y, depth)
    plt.axis('equal')
    plt.axis('off')
    plt.title("Conch Shell Spiral Fractal")
    plt.show()

if __name__ == "__main__":
    conch_spiral_fractal()
# %%
# OpenGL dynamic 3D fractal rendering

angle = 0

def generate_spiral_points(a=0.2, b=0.20, turns=6, points=2000):
    theta = np.linspace(0, 2 * np.pi * turns, points)
    r = a * np.exp(b * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(x)
    return np.stack([x, y, z], axis=1)

def draw_spiral_3d(points, depth, scale=0.5, angle_offset=np.pi/4):
    if depth == 0:
        return
    glColor3f(0.2 + 0.15*depth, 0.7 - 0.1*depth, 0.9 - 0.15*depth)
    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex3f(*p)
    glEnd()
    for i in np.linspace(0.2, 0.8, 3):
        idx = int(i * len(points))
        base = points[idx]
        # Scale and rotate in 3D (about z axis)
        sub = points - base
        c, s = np.cos(angle_offset), np.sin(angle_offset)
        rot = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
        sub = scale * sub @ rot.T
        draw_spiral_3d(sub + base, depth - 1, scale * 0.7, angle_offset)

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -6)
    glRotatef(angle, 0, 1, 0)
    glRotatef(angle * 0.7, 1, 0, 0)
    pts = generate_spiral_points()
    draw_spiral_3d(pts, depth=4)
    glutSwapBuffers()

def idle():
    global angle
    angle += 0.5
    if angle > 360:
        angle -= 360
    glutPostRedisplay()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / float(h or 1), 1, 40)
    glMatrixMode(GL_MODELVIEW)

def main_opengl():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"3D Conch Spiral Fractal")
    glEnable(GL_DEPTH_TEST)
    glClearColor(1, 1, 1, 1)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    glutMainLoop()

# Uncomment to run OpenGL visualization
# if __name__ == "__main__":
#     main_opengl()