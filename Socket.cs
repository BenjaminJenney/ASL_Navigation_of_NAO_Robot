using System.Net.Sockets;

using System.Text;

namespace Microsoft.Samples.Kinect.DiscreteGestureBasics
{
    class Socket
    {
            private int byteCount;
            private byte[] sendData;
            private NetworkStream stream;
        private TcpClient client;

        public Socket(string serverIP, int port)
        {
            client = new TcpClient(serverIP, port);
        }

        public void updateNao(string message)
            {
            
                byteCount = Encoding.ASCII.GetByteCount(message);
                sendData = new byte[byteCount];
                sendData = Encoding.ASCII.GetBytes(message);
                stream = client.GetStream();
                stream.Write(sendData, 0, sendData.Length);
        }
    }
}
