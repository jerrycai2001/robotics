# %%
import numpy as np

import matplotlib.pyplot as plt

# Synthetic 2D environment
ENV_SIZE = 100
OBSTACLES = [((30, 30), 10), ((70, 70), 8), ((50, 20), 5)]  # (center, radius)
CHEMO_SOURCE = (80, 80)

def is_obstacle(pos):
    for center, radius in OBSTACLES:
        if np.linalg.norm(np.array(pos) - np.array(center)) < radius:
            return True
    return False

def chemo_concentration(pos):
    # Simple inverse-square law
    dist = np.linalg.norm(np.array(pos) - np.array(CHEMO_SOURCE))
    return 1000 / (dist**2 + 1)

# Simulate sensors
def get_visual(pos):
    # Returns noisy position if not occluded by obstacle
    noise = np.random.normal(0, 1, 2)
    return np.array(pos) + noise

def get_lidar(pos):
    # Returns distance to nearest obstacle in 8 directions
    directions = np.array([[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]])
    dists = []
    for d in directions:
        for r in range(1, 20):
            p = np.array(pos) + d*r
            if np.any(p < 0) or np.any(p >= ENV_SIZE) or is_obstacle(p):
                dists.append(r)
                break
        else:
            dists.append(20)
    return np.array(dists) + np.random.normal(0, 0.5, 8)

def get_chemo(pos):
    # Returns noisy chemo concentration
    return chemo_concentration(pos) + np.random.normal(0, 5)

def get_imu(vel):
    # Returns noisy velocity
    return np.array(vel) + np.random.normal(0, 0.1, 2)

# %%
# Kalman Filter for 2D position and velocity
class KalmanFilter:
    def __init__(self):
        self.x = np.zeros(4)  # [x, y, vx, vy]
        self.P = np.eye(4) * 10
        self.F = np.eye(4)
        self.F[0,2] = self.F[1,3] = 1  # dt=1
        self.Q = np.eye(4) * 0.1
        self.H = np.zeros((4,4))
        self.H[:2,:2] = np.eye(2)
        self.H[2:,2:] = np.eye(2)
        self.R = np.eye(4)
        self.R[:2,:2] = np.eye(2) * 2   # vision
        self.R[2:,2:] = np.eye(2) * 0.2 # imu

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(4) - K @ self.H) @ self.P

# %%
# Drone navigation
def plan_next_step(pos, chemo, lidar):
    # Move towards chemo gradient, avoid obstacles
    grad = np.array(CHEMO_SOURCE) - np.array(pos)
    grad = grad / (np.linalg.norm(grad) + 1e-6)
    # If obstacle ahead, steer away
    if np.min(lidar[:4]) < 3:
        avoid = np.array([lidar[2] - lidar[0], lidar[3] - lidar[1]])
        grad += avoid
    grad = grad / (np.linalg.norm(grad) + 1e-6)
    return grad * 1.0  # step size

# %%
# Simulation
np.random.seed(42)
kf = KalmanFilter()
pos = np.array([10.0, 10.0])
vel = np.array([0.0, 0.0])
trajectory = [pos.copy()]
estimates = [pos.copy()]

for t in range(100):
    # Sensor readings
    vision = get_visual(pos)
    lidar = get_lidar(pos)
    chemo = get_chemo(pos)
    imu = get_imu(vel)

    # Kalman filter fusion (vision + imu)
    z = np.hstack([vision, imu])
    kf.predict()
    kf.update(z)
    est_pos = kf.x[:2]
    estimates.append(est_pos.copy())

    # Plan next step
    vel = plan_next_step(est_pos, chemo, lidar)
    next_pos = pos + vel
    if not is_obstacle(next_pos) and np.all(next_pos >= 0) and np.all(next_pos < ENV_SIZE):
        pos = next_pos
    trajectory.append(pos.copy())
    if np.linalg.norm(pos - CHEMO_SOURCE) < 3:
        print("Reached chemo source!")
        break

# %%
# Visualization
plt.figure(figsize=(8,8))
plt.xlim(0, ENV_SIZE)
plt.ylim(0, ENV_SIZE)
for center, radius in OBSTACLES:
    circle = plt.Circle(center, radius, color='gray', alpha=0.5)
    plt.gca().add_patch(circle)
plt.plot(*zip(*trajectory), label='True Trajectory', marker='o')
plt.plot(*zip(*estimates), label='KF Estimate', linestyle='--')
plt.scatter(*CHEMO_SOURCE, c='red', label='Chemo Source')
plt.legend()
plt.title("2D Drone Navigation with Multi-Modal Sensor Fusion")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
# %%
# Plot error over time
errors = [np.linalg.norm(np.array(est) - np.array(true)) for est, true in zip(estimates, trajectory)]
plt.figure(figsize=(8,4))
plt.plot(errors, label='KF Position Error')
plt.xlabel('Time Step')
plt.ylabel('Error (Euclidean Distance)')
plt.title('Kalman Filter Estimate Error Over Time')
plt.grid(True)
plt.legend()
plt.show()

# %%
# Show relative modality weights (Kalman Gain diagonals for vision vs imu)
kf_gains_vision = []
kf_gains_imu = []
kf = KalmanFilter()
pos = np.array([10.0, 10.0])
vel = np.array([0.0, 0.0])
for t in range(len(estimates)-1):
    vision = get_visual(pos)
    imu = get_imu(vel)
    z = np.hstack([vision, imu])
    kf.predict()
    # Compute Kalman Gain for this step
    S = kf.H @ kf.P @ kf.H.T + kf.R
    K = kf.P @ kf.H.T @ np.linalg.inv(S)
    # Vision: K[0,0] and K[1,1], IMU: K[2,2] and K[3,3]
    kf_gains_vision.append(np.mean([K[0,0], K[1,1]]))
    kf_gains_imu.append(np.mean([K[2,2], K[3,3]]))
    kf.update(z)
    # Simulate next pos for visualization only
    pos = trajectory[t+1]

plt.figure(figsize=(8,4))
plt.plot(kf_gains_vision, label='Vision Weight')
plt.plot(kf_gains_imu, label='IMU Weight')
plt.xlabel('Time Step')
plt.ylabel('Average Kalman Gain')
plt.title('Relative Sensor Modality Weights Over Time')
plt.legend()
plt.grid(True)
plt.show()
# %%
