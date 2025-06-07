import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"  # Tambahan penting!

# ... sisa kode kamu seperti biasa


# === Bentuk dasar ===
def create_sphere(center, radius, resolution=30):
    u = np.linspace(0, 2*np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones_like(u), np.cos(v)) + center[2]
    return x, y, z

def create_cylinder(center, radius, height, resolution=30):
    theta = np.linspace(0, 2*np.pi, resolution)
    z = np.array([0, height])
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta) + center[0]
    y = radius * np.sin(theta) + center[1]
    z = z + center[2]
    return x, y, z

def create_cone(center, radius, height, resolution=30):
    theta = np.linspace(0, 2*np.pi, resolution)
    r = np.array([0, radius])
    theta, r = np.meshgrid(theta, r)
    x = r * np.cos(theta) + center[0]
    y = r * np.sin(theta) + center[1]
    z = center[2] + height * (1 - r / radius)
    return x, y, z

# === Bangun karakter ===
fig = go.Figure()

# Kepala
x, y, z = create_sphere(center=(0, 0, 2.6), radius=0.7)
fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='YlOrBr', showscale=False))

# Badan
x, y, z = create_cylinder(center=(0, 0, 1.3), radius=0.5, height=1.2)
fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Reds', showscale=False))

# Lengan
for dx in [-0.8, 0.8]:
    x, y, z = create_cylinder(center=(dx, 0, 1.5), radius=0.1, height=0.9)
    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Reds', showscale=False))

# Kaki
for dx in [-0.2, 0.2]:
    x, y, z = create_cylinder(center=(dx, 0, 0.3), radius=0.15, height=0.8)
    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Blues', showscale=False))

# Sepatu
for dx in [-0.2, 0.2]:
    x, y, z = create_sphere(center=(dx, 0, 0.1), radius=0.2)
    fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Blues', showscale=False))

# Topi
x, y, z = create_cone(center=(0, 0, 3.3), radius=0.6, height=0.9)
fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Purples', showscale=False))

# === Layout final ===
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectratio=dict(x=1, y=1, z=1.8)
    ),
    title="3D Cartoon Character – Super Cute Version",
    margin=dict(l=0, r=0, b=0, t=30)
)

fig.show()
