import sys, os
from skillshare import Skillshare, splash
from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare("PHPSESSID=407aa237fa31508a488f477c7f420358")
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
