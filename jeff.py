import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests

url = "https://www.themebeta.com/media/cache/728/files/chrome/images/201703/13/61e3b36560ca16125d879b922fdcf642.png"
img = Image.open(requests.get(url, stream=True).raw)
img = np.array(img)
plt.imshow(img)
plt.show()

img_g = img [0:1000,0:360]
img_d = img [0:1000, 361:800]
img_gi = np.fliplr(img_g)
img_di = np.fliplr(img_d)


img_der = np.hstack((img, img_g, img_gi, img_di, img_d))
plt.imshow(img_der)
plt.show()

img_test = np.rot90 (img)
plt.imshow(img_test)
plt.show()

img_test2 = np.flipud (img)
plt.imshow(img_test2)
plt.show()

