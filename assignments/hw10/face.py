"""
Name: Sean Faust
HW10.py

Problem: This homework has me creating methods for the class 'Face'.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        smile = self.mouth.clone()
        mouth_center = self.mouth.getCenter()
        left_smile = Line(smile.getP1(), (mouth_center.getX(), mouth_center.getY() * 1.15))
        right_smile = Line(smile.getP2(), (mouth_center.getX(), mouth_center.getY() * 1.15))
        left_smile.draw(self.window)
        right_smile.draw(self.window)

    def shock(self):
        shock = self.left_eye.clone()
        shock_point = self.mouth.getCenter()
        self.mouth.undraw()
        shock.move(shock_point.getX(), shock_point.getY())
        shock.draw(self.window)


    def wink(self):
        eye_center = self.left_eye.getCenter()
        eye_len = self.left_eye.getRadius()
        wink = Line((eye_center.getX() - eye_len, eye_center.getY()),
                    (eye_center.getX() + eye_len, eye_center.getY()))
        self.left_eye.undraw()
        wink.draw(self.window)
