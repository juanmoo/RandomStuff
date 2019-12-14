import numpy as np
from numpy.linalg import svd
from PIL import Image

image_path = 'lion_cropped.jpg'

image = np.array(Image.open(image_path))
r, g, b = image.T

gray = np.uint8(.21 * r + .72 * g + .07 * b)
gray3 = np.array([gray] * 3).T
gray_im = Image.fromarray(gray3)

gray_im.save('gray.png')


# SVD decomp
u, d, vh = svd(gray)
padding = np.zeros((2, 1), dtype=np.uint8)
d = d.reshape((206, 1))
d = np.vstack((d, padding))
diag = np.diag(d.T[0])[:-2]


svd = np.uint8(u @ diag @ vh)
svd3 = np.array([svd] * 3).T
svd_im = Image.fromarray(svd3)
svd_im.save('svd.png')


# Eliminate small singular components
d_prime = np.array(d)
L = len(d_prime)
for i in range(5, len(d_prime)):
    d_prime[i] = 0


diag_prime = np.diag(d_prime.T[0])[:-2]

print(diag_prime.shape)


svd1 = np.uint8((u @ diag_prime @ vh))
svd1_3 = np.array([svd1] * 3).T
svd1_im = Image.fromarray(svd1_3)
svd1_im.save('svd1.png')
