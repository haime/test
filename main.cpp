#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <iostream>
using namespace cv;


int main()
{
	VideoCapture capture( CV_CAP_OPENNI );
	for(;;)
	{
	    Mat depthMap;
	    Mat bgrImage;
	
	    capture.grab();
	
	    capture.retrieve( depthMap, CV_CAP_OPENNI_DEPTH_MAP );
	    capture.retrieve( bgrImage, CV_CAP_OPENNI_BGR_IMAGE );
	
		imshow("depthMap",depthMap);
		imshow("bgrImage", bgrImage);
	    if( waitKey( 30 ) >= 0 )
	        break;
	}
	
	return 0;
}