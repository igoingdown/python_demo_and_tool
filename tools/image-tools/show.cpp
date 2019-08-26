#include <cv.h>
#include <cvaux.h>
#include <highgui.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;
using namespace cv;

void showImages() {
    string image_dir = "./Images/";
    for (int i = 0; i < 100; i++) {
    	Mat image;
    	namedWindow("good picture");
        image = imread(image_dir + to_string(i) + ".jpg");
        imshow(to_string(i), image);
        waitKey(100);
    }
}

int main(void) {
    showImages();
    return 0;
}
