import cv2
import numpy as np
import matplotlib.image as mpimg

class PerspectiveTransform():
    # Four source coordinates
    src = np.float32(
        [[700, 460],
        [1055, 685],
        [254, 685],
        [582, 460]])
    # Four desired coordinates
    dst = np.float32(
        [[1040, 0],
        [1040, 685],
        [250, 685],
        [250, 0]])
    color = (0, 255, 0) 
    thickness = 9
    def __init__(self):
        # Compute the perspective Transform
        self.warp_matrix = cv2.getPerspectiveTransform(self.src, self.dst)
        # Compute the inverse by swapping the input parameter
        self.unwarp_matrix = cv2.getPerspectiveTransform(self.dst, self.src)
    def draw_lines(self,img):
        color = (255, 0, 0) 
        thickness = 1
        cv2.line(img, (self.src[2][0],self.src[2][1]), (self.src[3][0],self.src[3][1]), color, thickness)
        cv2.line(img, (self.src[0][0],self.src[0][1]), (self.src[1][0],self.src[1][1]), color, thickness)
        
    def warp(self, img):
        img_size = img.shape[1], img.shape[0]
        # Compute warped image
        warped = cv2.warpPerspective(img, self.warp_matrix, img_size, flags=cv2.INTER_LINEAR)
        return warped

    def unwarp(self, img):
        img_size = img.shape[1], img.shape[0]
        # Create warped image - uses linear interpolation
        unwarped = cv2.warpPerspective(img, self.unwarp_matrix, img_size, flags=cv2.INTER_LINEAR)
        return unwarped

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    transformer = PerspectiveTransform()
    img = mpimg.imread('..\\test_images\\straight_lines1.jpg')
    transformer.draw_lines(img)
    plt.imshow(img)
#     plt.show()
    plt.clf()

    warped = transformer.warp(img)
    plt.imshow(warped)
#     plt.show()
    plt.clf()

    unwarped = transformer.unwarp(warped)
    plt.imshow(unwarped)
#     plt.show()
    plt.clf()
    
    # Plot the result
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()

    ax1.imshow(img)
    ax1.set_title('Original Image', fontsize=40)

    ax2.imshow(warped)
    ax2.set_title('Warped Result', fontsize=40)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    plt.savefig('..\\output_images\\transform_straight_lines_1.png')