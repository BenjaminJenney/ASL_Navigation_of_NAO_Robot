using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Microsoft.Samples.Kinect.DiscreteGestureBasics
{
    class Matlab
    {
        private MLApp.MLApp matlab = new MLApp.MLApp();
        private string ex0;
        private string ex1;
        private string ex2;

        public Matlab()
        {
           matlab.Visible = 0;
           ex0 =  matlab.Execute("rosinit('192.168.1.161');"); //CHANGE IP!!!!!, CHECK THE IP OF THE OTHER LISTENER

            ex1 = matlab.Execute("chatpub = rospublisher('/turtle', 'std_msgs/String');");

            ex2 = matlab.Execute("msg = rosmessage(chatpub);");
        }

    }
}
