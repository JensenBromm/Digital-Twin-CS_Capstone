# Digital-Twin-CS_Capstone
Gulfstream Capstone Project

To begin, it's crucial to grasp the concept of a digital twin—an intricate virtual representation of a tangible object, system, or process. This digital counterpart mirrors its real-world counterpart, continually updated to mirror changes and conditions in the physical realm. Widely applied across various industries, such as manufacturing, healthcare, infrastructure, and the Internet of Things (IoT), the notion of a digital twin serves as the foundation for our project.

Our project centered around the creation of a digital twin for one of our university labs, designed to be adaptable for various spaces featuring cameras and moving objects in the future. Leveraging Unreal Engine, our team delved into multiple facets:
![image](https://github.com/JensenBromm/Digital-Twin-CS_Capstone/assets/141427577/ca7b63fe-40e4-4174-969f-23db5de30cff)



Multi-Perspective Views:
We initiated the project by establishing a top-down view, capturing footage from security cameras within the lab. Utilizing OpenCV with Python, we transformed this footage into a comprehensive top-down perspective. This not only offered enhanced visibility of the designated area but also provided accurate distance references between objects.


Object Detection Algorithms:
Implementing the YOLO (You Only Look Once) algorithm, we seamlessly integrated it with the camera footage. This enabled real-time tracking of moving objects, with data promptly relayed to a MongoDB database. The model, trained using CVAT.ai and over 500 annotated images, achieved an impressive average delay of 52ms.

Database Management:
Connecting Unreal Engine with MongoDB using C++, we established a streamlined process for data exchange. Pixel coordinates from the object detector were translated into Unreal coordinates using a defined equation: Unreal Coordinate = Scale * Pixel Coordinate - Offset.

3D Modeling Technology:
For a more refined model, especially tailored to objects resembling our robots, we employed photogrammetry. Reality Capture served as the primary tool, supplemented by LumaAI & Blender for final touches and improved results.

In summary, our project seamlessly integrated multi-perspective views, advanced object detection algorithms, efficient database management, and cutting-edge 3D modeling techniques. The digital twin created is not only adaptable but also serves as a testament to the convergence of technologies, offering a comprehensive solution for real-time monitoring and analysis within our university lab.



Team Members: Jensen Bromm, Jerome Larson, Joselin Aguirre Trujillo, and Mateo Maldonado Rojas
