import matplotlib.pyplot as plt
import numpy as np

# Helper function to rotate a point around the origin
def rotate_point(point, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([
        [np.cos(angle_radians), -np.sin(angle_radians)],
        [np.sin(angle_radians),  np.cos(angle_radians)]
    ])
    return rotation_matrix @ point

# Generate regular pentagon points centered at origin
def regular_pentagon(radius=1, start_angle=90):
    points = []
    for i in range(5):
        angle = start_angle + i * 72  # 360 / 5 = 72 degrees
        x, y = rotate_point(np.array([radius, 0]), angle)
        points.append((x, y))
    return points

# Get pentagon points
pentagon = regular_pentagon(radius=2)
labels = ['P', 'Q', 'R', 'S', 'T']

# Coordinates for U (point on segment ST, approx 1/3 along ST from S to T)
S = np.array(pentagon[3])
T = np.array(pentagon[4])
U = S + (T - S) * (1/3)

# Extract coordinates
x_vals, y_vals = zip(*pentagon)
x_vals += (x_vals[0],)  # Close the pentagon loop
y_vals += (y_vals[0],)

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x_vals, y_vals, 'k-', lw=1.5)  # Pentagon outline

# Plot triangle PUT
P = np.array(pentagon[0])
triangle_PUT_x = [P[0], U[0], T[0], P[0]]
triangle_PUT_y = [P[1], U[1], T[1], P[1]]
ax.plot(triangle_PUT_x, triangle_PUT_y, 'r--', lw=2, label='Triangle PUT')
ax.fill(triangle_PUT_x, triangle_PUT_y, color='red', alpha=0.1)

# Mark points
for i, (x, y) in enumerate(pentagon):
    ax.text(x, y + 0.1, labels[i], ha='center', fontsize=12, fontweight='bold')
ax.plot(U[0], U[1], 'bo')
ax.text(U[0], U[1] - 0.15, 'U', ha='center', fontsize=12, fontweight='bold')

# Highlight angle QPU = 90° visually (right angle triangle)
ax.text((P[0]+U[0])/2, (P[1]+U[1])/2 + 0.1, "90°", color="blue", fontsize=10)

# Axis settings
ax.set_aspect('equal')
ax.axis('off')
plt.title("Regular Pentagon PQRST and Triangle PUT", fontsize=14)
plt.legend()
plt.show()
