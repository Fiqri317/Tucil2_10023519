import matplotlib.pyplot as plt
import numpy as np
import time

# Fungsi Kurva Bezier
def bezier_curve(points, t):
    P0, P1, P2 = points
    Q0 = ((1-t) * P0[0] + t * P1[0], (1-t) * P0[1] + t * P1[1])
    Q1 = ((1-t) * P1[0] + t * P2[0], (1-t) * P1[1] + t * P2[1])
    B = ((1-t) * Q0[0] + t * Q1[0], (1-t) * Q0[1] + t * Q1[1])
    return Q0, Q1, B

# Masukan titik kontrol input dan jumlah iterasi secara manual
P0 = tuple(map(float, input("Enter coordinates for point P0 (x y): ").split()))
P1 = tuple(map(float, input("Enter coordinates for point P1 (x y): ").split()))
P2 = tuple(map(float, input("Enter coordinates for point P2 (x y): ").split()))
iterations = int(input("Enter the number of iterations: "))

# Menghitung Kurva Poin
t_values = np.linspace(0, 1, iterations)
start_time = time.time()
curve_points = [bezier_curve([P0, P1, P2], t)[2] for t in t_values]
end_time = time.time()

# Mengekstrak titik spesifik pada t = 0,25
Q0, Q1, B = bezier_curve([P0, P1, P2], 0.25)

# Plotting
plt.figure(figsize=(14, 6))

# Control points
plt.plot([p[0] for p in [P0, P1, P2]], [p[1] for p in [P0, P1, P2]], 'ko-', label='Control Points')

# Kurva
plt.plot([p[0] for p in curve_points], [p[1] for p in curve_points], 'r-', label='Bezier Curve')

# Garis pada t = 0,25
plt.plot([Q0[0], Q1[0]], [Q0[1], Q1[1]], 'b-', label='Line Q0-Q1 at t=0.25')
plt.plot(B[0], B[1], 'go', label='Point B at t=0.25')

plt.title('Bezier Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# Waktu Eksekusi
print(f"Execution time: {end_time - start_time:.4f} seconds")
