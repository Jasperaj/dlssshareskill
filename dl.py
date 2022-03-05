import sys, os
from skillshare import Skillshare, splash
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare(cookie)
    course_url = "https://www.skillshare.com/classes/The-Art-of-Company-Valuation-Advanced-course/1780499879"
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
