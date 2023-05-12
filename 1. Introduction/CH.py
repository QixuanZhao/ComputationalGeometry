import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points, x_min, x_max, y_min, y_max):
    x = np.random.uniform(x_min, x_max, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    points = np.column_stack((x, y))
    return points

def slowCH(points: np.ndarray) -> list:
    E = []
    for p in points:
        for q in points:
            if np.array_equal(p, q): continue
            pq = q - p
            valid = True
            for r in points:
                if np.array_equal(r, q) or np.array_equal(r, p): continue
                qr = r - q
                c = np.cross(pq, qr)
                if c > 0: #left
                    valid = False
            
            if valid:
                E.append((p, q))
    CH = []
    e = E.pop(0)
    CH.append(e[1])

    while len(E) > 0:
        for index, ec in enumerate(E):
            if np.array_equal(ec[0], e[1]):
                e = ec
                E.pop(index)
                break
        CH.append(e[1])
    
    return CH

points = generate_random_points(100, 0, 1, 0, 1)
print(points)

CH = slowCH(points)
CH.append(CH[0])
npCH = np.array(CH)
print(npCH)

plt.scatter(points[:, 0], points[:, 1])
plt.plot(npCH[:, 0], npCH[:, 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points')
plt.show()