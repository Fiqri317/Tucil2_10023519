import matplotlib.pyplot as plt
import time

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Optimisasi untuk mengurangi perhitungan
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def brute_force_quadratic_bezier(points, iterations):
    curve_points = []
    n = len(points)  # Jumlah titik kontrol

    for i in range(iterations + 1):
        t = i / iterations  # Parameter t berjalan dari 0 sampai 1
        x, y = 0, 0
        for j, (px, py) in enumerate(points):
            # Menghitung koefisien binomial
            b = binomial(n - 1, j) * (1 - t)**(n - 1 - j) * t**j
            x += px * b
            y += py * b
        curve_points.append((x, y))

    return curve_points

def plot_curve(points, curve_points):
    # Memplot titik kontrol
    plt.plot([p[0] for p in points], [p[1] for p in points], 'ro-', label='Control Points')
    # Memplot kurva Bézier
    plt.plot([p[0] for p in curve_points], [p[1] for p in curve_points], 'b-', label='Quadratic Bezier Curve')
    plt.legend()
    plt.title('Bezier Curve')
    plt.show()

def main():
    # Meminta pengguna memasukkan koordinat untuk tiga titik kontrol
    points = []
    for i in range(3):
        point = tuple(map(float, input(f"Enter coordinates for point {i+1} (x y): ").split()))
        points.append(point)

    iterations = int(input("Enter the number of iterations: "))

    # Mulai mengukur waktu
    start_time = time.time()

    # Menghitung titik-titik pada kurva Bézier dan memplotnya
    curve_points = brute_force_quadratic_bezier(points, iterations)
    
    # Selesai mengukur waktu
    end_time = time.time()
    
    # Memplot kurva
    plot_curve(points, curve_points)
    
    # Menampilkan waktu eksekusi
    print(f"Execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
