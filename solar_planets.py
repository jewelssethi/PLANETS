import cv2

img= cv2.imread("solar.jpg")




sun=cv2.putText(img,
            "Sun",
            (20,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

mercury=cv2.putText(img,
            "MERCURY",
            (120,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

venus=cv2.putText(img,
            "VENUS",
            (200,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

earth=cv2.putText(img,
            "EARTH",
            (300,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

mars=cv2.putText(img,
            "MARS",
            (400,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

jupiter=cv2.putText(img,
            "JUPITER",
            (500,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

saturn=cv2.putText(img,
            "SATURN",
            (770,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )


uranus=cv2.putText(img,
            "URANUS",
            (950,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )

pluto=cv2.putText(img,
            "PLUTO",
            (1100,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color=(255,255,255)
            )










cv2.imshow("output",img)

cv2.imwrite("Solar.jpg",img)
            

cv2.waitKey(0)