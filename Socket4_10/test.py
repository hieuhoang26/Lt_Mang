import numpy as np

# Ma trận đầu vào
image = np.array([
    [2, 4, 2, 4, 4, 3, 3, 3],
    [4, 3, 1, 4, 2, 1, 3, 1],
    [2, 3, 1, 2, 1, 1, 3, 2],
    [4, 1, 1, 2, 2, 2, 2, 3],
    [1, 4, 1, 2, 1, 4, 3, 4],
    [2, 3, 1, 4, 1, 1, 2, 1],
    [1, 2, 2, 2, 4, 1, 3, 4],
    [1, 3, 1, 1, 4, 1, 1, 4]
])

# Bộ lọc Sobel
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

# Hàm để áp dụng bộ lọc Sobel
def apply_sobel(image):
    rows, cols = image.shape
    sobel_x_output = np.zeros((rows, cols))
    sobel_y_output = np.zeros((rows, cols))

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Tính Gx
            gx = np.sum(sobel_x * image[i - 1:i + 2, j - 1:j + 2])
            sobel_x_output[i, j] = gx

            # Tính Gy
            gy = np.sum(sobel_y * image[i - 1:i + 2, j - 1:j + 2])
            sobel_y_output[i, j] = gy

    # Tính độ lớn của gradient
    magnitude = np.sqrt(sobel_x_output**2 + sobel_y_output**2)
    magnitude = np.clip(magnitude, 0, 255)
    return sobel_x_output, sobel_y_output, magnitude

# Áp dụng bộ lọc Sobel
if __name__ == '__main__':

    sobel_x_result, sobel_y_result, magnitude_result = apply_sobel(image)

    print(magnitude_result)
