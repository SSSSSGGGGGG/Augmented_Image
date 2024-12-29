from scipy.interpolate import interp1d, BarycentricInterpolator, KroghInterpolator
import numpy as np
import matplotlib.pyplot as plt

x = [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]  # Input intensities (original image)
y = [0.0, 0.15, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 1.0]  # Output intensities (desired mapping)

# Create x values for plotting the interpolation curve
x_vals = np.linspace(0, 1, 500)

# Apply different interpolation kinds
kinds = ['linear', 'nearest', 'quadratic', 'cubic']
plt.figure(figsize=(10, 8))

for i, kind in enumerate(kinds, start=1):
    # Interpolate with different methods
    curve = interp1d(x, y, kind=kind, fill_value="extrapolate")
    y_vals = curve(x_vals)
    
    # Plot the result
    plt.subplot(2, 2, i)
    plt.plot(x_vals, y_vals, label=f'{kind.capitalize()} interpolation')
    plt.scatter(x, y, color='red')  # Show control points
    plt.title(f'{kind.capitalize()} Interpolation')
    plt.xlabel('Input Intensity')
    plt.ylabel('Output Intensity')
    plt.grid(True)
    plt.legend()

# For Polynomial and Krogh Interpolation:
plt.subplot(2, 2, 4)
poly_interpolator = np.poly1d(np.polyfit(x, y, 5))  # Polynomial fit (5th degree)
poly_vals = poly_interpolator(x_vals)

krogh_interpolator = KroghInterpolator(x, y)
krogh_vals = krogh_interpolator(x_vals)

# Plot the Polynomial and Krogh interpolation
plt.plot(x_vals, poly_vals, label='Polynomial Interpolation', color='green')
plt.plot(x_vals, krogh_vals, label='Krogh Interpolation', color='purple')
plt.scatter(x, y, color='red')  # Show control points
plt.title('Polynomial and Krogh Interpolation')
plt.xlabel('Input Intensity')
plt.ylabel('Output Intensity')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
